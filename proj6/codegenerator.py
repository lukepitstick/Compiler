#import MIPSinstruction
import tree #from tree?
import re
datatoWrite = [] #data write section
toWrite = [] # initialize what to write
dict1 = {}
dict2 = {} #string dict


def READ_IDS(args): #was args = []
    for var in args:
        if dict1[var][1] is "INT":
            toWrite.append("li $v0, 5\nsyscall\n")
            toWrite.append("la $t0, %s\n" % var)
            toWrite.append("sw $v0, 0($t0)\n\n")
        else:
            raise CompilerError("Semantic Error: Read on invalid type")

def WRITE_IDS(t): #receives tree with head as expr_list
    for child in t.children:

        type, varlist = EXPRESSION(child,"$t0")
        for v in varlist:
            if dict1[v][0] != "True":
                raise CompilerError("Semantic Error: Write before a variable is instantiated")

        if type is "BOOL" or type is "INT":
            toWrite.append("add $a0, $t0,0\n")
            toWrite.append("li $v0, 1\nsyscall\n\n")
        elif type is "STRING":
            toWrite.append("la $a0, %s\nli $v0, 4\nsyscall\n\n"% varlist[0])

def otherReg(reg):
    if reg == "$t0":
        return ("$t1","t2")
    if reg == "$t1":
        return ("$t0", "t2")
    if reg == "$t2":
        return ("$t0", "t1")

def EXPRESSION(t,reg): #Gets tree with EXPRESSION as head
    #Temporary
    try:
        isstring = t.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].val
        if dict1[isstring][1] is "STRING":
            return ("STRING",[isstring])
    except:
        pass

    regs = otherReg(reg)
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"

    for child in t.children:
        if child.label != "OR":
            if not opFlag:
                type1, varlist1 = TERM1(child,regs[0])
                varlist += varlist1
            if opFlag:
                type2, varlist2 = TERM1(child, regs[1])
                varlist += varlist2
                if (type1 != "BOOL") | (type2 != "BOOL"):
                    raise CompilerError("Semantic Error: 'or' operand on non-bool")
                toWrite.append("or %s, %s, %s"%(regs[0],regs[0],regs[1]))
                opFlag = False
        if child.label == "OR":
            retType = "BOOL"
            opFlag = True

    toWrite.append("lw %s, %s"%(reg, regs[0]))
    return (retType, varlist)

def TERM1(t,reg): #Gets tree with TERM1 as head
    regs = otherReg(reg)
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"

    for child in t.children:
        if child.label != "AND":
            if not opFlag:
                type1, varlist1 = FACT1(child, regs[0])
                varlist += varlist1
            if opFlag:
                type2, varlist2 = FACT1(child, regs[1])
                varlist += varlist2
                if (type1 != "BOOL") | (type2 != "BOOL"):
                    raise CompilerError("Semantic Error: 'and' operand on non-bool")
                toWrite.append("and %s, %s, %s" % (regs[0], regs[0], regs[1]))
                opFlag = False
        if child.label == "AND":
            retType = "BOOL"
            opFlag = True

    toWrite.append("lw %s, %s" % (reg, regs[0]))
    return (retType, varlist)

def FACT1(t,reg): #Gets tree with FACT1 as head
    regs = otherReg(reg)
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    compareType = ""

    for child in t.children:
        if child.label == "EXP2":
            if not opFlag:
                type1, varlist1 = EXP2(child, regs[0])
                varlist += varlist1
            if opFlag:
                type2, varlist2 = EXP2(child, regs[1])
                varlist += varlist2
                if (type1 != "INT") or (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                toWrite.append("%s %s, %s, %s" % (compareType, regs[0], regs[0], regs[1]))
                opFlag = False

        if child.label == "R":
            try:
                ROP = child.children[0].label
                if ROP == "GREATEREQUAL":
                    compareType = "sge"
                elif ROP == "LESSEQUAL":
                    compareType = "sle"
                elif ROP == "EQUAL":
                    compareType = "seq"
                elif ROP == "LESSTHAN":
                    compareType = "slt"
                elif ROP == "GREATERTHAN":
                    compareType = "sgt"
                elif ROP == "NOTEQUAL":
                    compareType = "sne"
                retType = "BOOL"
                opFlag = True
            except: #No Comparison
                pass

    toWrite.append("lw %s, %s" % (reg, regs[0]))
    return (retType, varlist)

def EXP2(t,reg):
    varlist = []
    retType = "INT"
    return (retType, varlist)

def DOINFIX(s):
    vs = []
    firstFlag = True
    while s.__len__() != 0:
        elem = s.pop(0)
        if elem is "-":
            reg = "$t0"
            a2 = vs.pop()
            a1 = vs.pop()
            if not firstFlag:
                if (a1 != "$t0") & (a2 != "$t0"):
                    reg = "$t3"

            d1 = "$t1"
            d2 = "$t2"
            if re.match("\d",a1):
                toWrite.append("li $t1, %s\n" % a1)
            elif a1 == "$t0":
                d1 = "$t0"
            elif a1 == "$t3":
                d1 = "$t3"
            else:
                toWrite.append("la $s0, %s\nlw $t1, ($s0)\n" %a1)

            if re.match("\d",a2):
                toWrite.append("li $t2, %s\n" % a2)
            elif a2 == "$t0":
                d2 = "$t0"
            elif a2 == "$t3":
                d2 = "$t3"
            else:
                toWrite.append("la $s0, %s\nlw $t2, ($s0)\n" %a2)
            toWrite.append("sub %s,%s,%s\n"%(reg,d1,d2))
            vs.append(reg)
            firstFlag = False
        elif elem is "+":
            reg = "$t0"
            a1 = vs.pop()
            a2 = vs.pop()
            if not firstFlag:
                if (a1 != "$t0") & (a2 != "$t0"):
                    reg = "$t3"
            d1 = "$t1"
            d2 = "$t2"
            if re.match("\d",a1):
                toWrite.append("li $t1, %s\n" % a1)
            elif a1 == "$t0":
                d1 = "$t0"
            elif a1 == "$t3":
                d1 = "$t3"
            else:
                toWrite.append("la $s0, %s\nlw $t1, ($s0)\n" %a1)

            if re.match("\d",a2):
                toWrite.append("li $t2, %s\n" % a2)
            elif a2 == "$t0":
                d2 = "$t0"
            elif a2 == "$t3":
                d2 = "$t3"
            else:
                toWrite.append("la $s0, %s\nlw $t2, ($s0)\n" %a2)
            toWrite.append("add %s,%s,%s\n"%(reg,d1,d2))
            vs.append(reg)
            firstFlag = False
        else:
            vs.append(elem)

    if vs.__len__() == 1: #if no operations
        a = vs.pop()
        if re.match("\d",a):
            toWrite.append("li $t0, %s\n" % a)
        elif a == "$t0":
            return
        else:
            toWrite.append("la $s0, %s\nlw $t0, ($s0)\n" %a)



def ASSIGN(t):
    #recieves a tree with root t being ASSIGNMENT
    var = t.children[0].children[0].val #variable being assigned
    vartype = dict1[var][1]

    #TEMPORARY
    r = t.children[1].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
    if r.label is "BOOLLIT":
        if vartype != "BOOL":
            raise CompilerError("Semanic Error: not a bool")
        if r.val == "True":
            toWrite.append("li $t0, 1\n")
        elif r.val == "False":
            toWrite.append("li $t0, 0\n")
    elif r.label is "INTLIT":
        if vartype != "INT":
            raise CompilerError("Semanic Error: not an int")
        toWrite.append("li $t0, %s\n" % r.val)

    #Will need to add this back in
    # type, varList = EXPRESSION(t.children[1], "$t0") #Infix on expression
    # for v in varList:
    #     if dict1[v][0] != "True":
    #             raise CompilerError("Semantic Error: ASSIGN before a variable is instantiated")
    # if vartype != type:
    #     raise CompilerError("Assignment types do not match")
    # if vartype == "STRING":
    #     #Find var line in datatoWrite and make its initial value the dict2 value from varlist[0]
    # else:
    #     #Integer/bool assign

    toWrite.append("la   $s0, %s\nsw   $t0, ($s0)\n\n" % var) #store value from $t0 into var's address


# Defines what #infix does
def INFIX(t):
    #receives tree t with head as expression
    stack = []
    varList = []
    flag1 = False
    flag2 = False
    postfixFlag = False
    for child in t.children:
        postfixFlag = True
        try:
            CC = child.children[0].label
        except IndexError:
            CC = "-"
        if CC == "EXPRESSION":
            s,VV = INFIX(child.children[0])
            varList = varList + VV
            stack = stack + s
        elif child.label == "PLUS":
            flag1 = True
            postfixFlag = False
        elif child.label == "MINUS":
            flag2 = True
            postfixFlag = False
        elif CC == "INTLIT":
            stack.append(child.children[0].val)
        elif CC == "IDENT":
            stack.append(child.children[0].children[0].val)
            varList.append(child.children[0].children[0].val)

        if postfixFlag:
            if flag1:
                stack.append("+")
                flag1 = False
            if flag2:
                stack.append("-")
                flag2 = False
    return stack, varList


def postOrderDFS(tree):
    if tree.isLeaf():
        pass
    if tree.label is "STATEMENT":
        if tree.children[0].label is "READ":
            arguments = []
            for child in tree.children[1].children:
                if child.children[0].label is "ID":
                    arguments.append(child.children[0].val)
            READ_IDS(arguments)
        elif tree.children[0].label is "WRITE":
            # arguments = []
            # for child in tree.children[1].children:
            #     if child.children[0].children[0].label is "INTLIT":
            #         arguments.append(child.children[0].children[0].val)
            #     elif child.children[0].children[0].children[0].label is "ID":
            #         arguments.append(child.children[0].children[0].children[0].val)
            WRITE_IDS(tree.children[1])
        elif tree.children[0].label is "ASSIGNMENT":
            ASSIGN(tree.children[0])
        elif tree.children[0].label is "BOOLTYPE":
            DEFTYPE(tree)
        elif tree.children[0].label is "STRINGTYPE":
            DEFTYPE(tree)
        elif tree.children[0].label is "INTTYPE":
            DEFTYPE(tree)
    for child in tree.children:
        postOrderDFS(child)

def DEFTYPE(tree):
    val = tree.children[1].children[0].val
    a,b = dict1[val]
    if a == "True":
        raise CompilerError("Semanic Error: Define type twice")
    else:
        dict1[val] = ("True",b)

def findGenerateMIPSCode(t, dict): #, fname):
    global dict1
    datatoWrite.append(".data\n") #beginning of our MIP
    #Generate data section from dict
    print(str(dict))
    for var in dict:
        # print(var)
        # print(dict[var])
        # if dict[var][0] == "" or dict[var][1] == "": #unsure
        #     raise CompilerError("Semantic error: Bad Dictionary")
        if dict[var][1] == 'STRING':
            datatoWrite.append("%s: .asciiz " % var)
            datatoWrite.append(dict[var][0])
            datatoWrite.append("\n")
        elif dict[var][1] == 'BOOL':
            # if 'True' in dict[var] or 'False' in dict[var]:
            datatoWrite.append("%s: .word 4\n" % var)
            # else:
            #     raise CompilerError("Semanic Error: Variable not declared correctly!")
        elif dict[var][1] == 'INT':
            datatoWrite.append("%s: .word 4\n" % var)

        # sync dictionaries
        dict1[var] = ("False", dict[var][1])
        if dict[var][0] != "True" and dict[var][0] != "False" and dict[var][0] != "":
            dict2[var] = dict[var][0]


    print(dict1)
    print(dict2)

    toWrite.append(".text\nmain:\n")

    #initiate the actual traversal
    postOrderDFS(t)

    #gracefully exit
    toWrite.append("li   $v0, 10\nsyscall")

    #write the array to the file
    return datatoWrite + toWrite

class CompilerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
