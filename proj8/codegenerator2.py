#import MIPSinstruction
import tree #from tree?
import re
import sys
datatoWrite = [] #data write section
textToWrite = {".main":[]} # initialize main section what to write, will also add subroutines
toWrite = [] # initialize what to write (remained for compatibility)
dict1 = {} #main dict (Initiated, type)
dict2 = {} #string dict
dict3 = {}
strdict = {}
ineff = []
ldict = {}
stringnum = 0
nestedIfCounter = 0

def READ_IDS(args, subroutine=".main"): #was args = []
    for var in args:
        if dict1[var][1] == "INT":
            textToWrite[subroutine].append("li $v0, 5\nsyscall\n")
            textToWrite[subroutine].append("la $t0, %s\n" % var)
            textToWrite[subroutine].append("sw $v0, 0($t0)\n\n")
            dict1[var] = ("True","INT")
        else:
            raise CompilerError("Semantic Error: Read on invalid type: " + var)

def WRITE_IDS(t, subroutine=".main"): #receives tree with head as expr_list
    global stringnum
       # reset registers
    for register in registers:
        registers[register] = False
    for child in t.children:
        if child.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].label == "STRING":
            val = child.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[
                0].children[0].val
            stringid = "stringtmptmp" + str(stringnum)
            stringnum += 1
            datatoWrite.append("%s: .asciiz %s\n" %(stringid, val))
            textToWrite[subroutine].append("la $a0, %s\nli $v0, 4\nsyscall\n\n" % stringid)
        else:
            # reset registers
            for register in registers:
                registers[register] = False
            type, varlist, reg = EXPRESSION(child)
            v1 = ""
            for v in varlist:
                # if ldict[v] != "True":
                v1 = v
                if (v == "FALSE") or (v == "TRUE"):
                    pass
                else:
                    if dict1[v][0] != "True":
                        raise CompilerError("Semantic Error: Write before a variable is instantiated" + v)
            if type == "INT":
                textToWrite[subroutine].append("add $a0, %s,0\n"% reg)
                textToWrite[subroutine].append("li $v0, 1\nsyscall\n\n")
            elif type == "BOOL":
                textToWrite[subroutine].append("la $s0, False\nla $s1, True\nmovn $a0,$s1,%s\nmovz $a0,$s0,%s\nli $v0, 4\n"
                               "syscall\n"%(reg,reg))
            elif type == "STRING":
                try:
                    if ldict[v] != "True": ##unsure
                        raise CompilerError("Semantic Error: String mismatch")
                except:
                    pass
                for x in ineff:
                    textToWrite[subroutine].append(x)
                textToWrite[subroutine].append("la $a0, %s\nli $v0, 4\nsyscall\n\n"% varlist[0])

       # type, varlist, reg = EXPRESSION(child)
       # for v in varlist:
       #     if dict1[v][0] != "True":
       #        raise CompilerError("Semantic Error: Write before a variable is instantiated")
       # if type is "BOOL" or type is "INT":
       #     toWrite.append("add $a0, %s,0\n"% reg)
       #     toWrite.append("li $v0, 1\nsyscall\n\n")
       # elif type is "STRING":
       #     toWrite.append("la $a0, %s\nli $v0, 4\nsyscall\n\n"% varlist[0])


def otherReg(reg):
    if reg == "$t0":
        return ("$t1","$t2")
    if reg == "$t1":
        return ("$t0", "$t2")
    if reg == "$t2":
        return ("$t0", "$t1")

registers = {"$t0":False, "$t1":False, "$t2":False, "$t3":False, "$t4":False, "$t5":False, "$t6":False, "$t7":False, 
             "$t8":False, "$t9":False, "$s1":False, "$s2":False, "$s3":False, "$s4":False, "$s5":False, "$s6":False,
             "$s7":False}

def EXPRESSION(t, subroutine=".main"): #Gets tree with EXPRESSION as head
  #  #Temporary
  #  try:
  #      isstring = t.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].val
  #      if dict1[isstring][1] is "STRING":
  #         return ("STRING",[isstring])
  #  except:
  #     pass
    #Temporary
    try:
        isstring = t.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].val
        if dict1[isstring][1] == "STRING":
            return ("STRING",[isstring], "")
    except:
        pass
    varlist = []
    retType = "INT"
    type1 = ""
    type2 = ""
    reg1 = ""
    reg2 = ""
    opFlag = False

    for child in t.children:
        if child.label != "OR":
            if not opFlag:
                type1, varlist1, reg1 = TERM1(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = TERM1(child)
                varlist += varlist2
                if (type1 != "BOOL") | (type2 != "BOOL"):
                    raise CompilerError("Semantic Error: 'or' operand on non-bool")
                textToWrite[subroutine].append("or %s, %s, %s\n"%(reg1,reg1,reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False
        if child.label == "OR":
            retType = "BOOL"
            opFlag = True


    if reg2 != "":
        registers[reg2] = False
    if retType != "BOOL":
        retType = type1
    return (retType, varlist, reg1)

def TERM1(t, subroutine=".main"): #Gets tree with TERM1 as head
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label != "AND":
            if not opFlag:
                type1, varlist1, reg1 = FACT1(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = FACT1(child)
                varlist += varlist2
                if (type1 != "BOOL") | (type2 != "BOOL"):
                    raise CompilerError("Semantic Error: 'and' operand on non-bool")
                toWrite.append("and %s, %s, %s\n" % (reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False
        if child.label == "AND":
            retType = "BOOL"
            opFlag = True

    if reg2 != "":
        registers[reg2] = False
    if retType != "BOOL":
        retType = type1
    return (retType, varlist, reg1)

def FACT1(t, subroutine=".main"): #Gets tree with FACT1 as head
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    compareType = ""
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label == "EXP2":
            if not opFlag:
                type1, varlist1, reg1 = EXP2(child)
                varlist += varlist1

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
                type2, varlist2, reg2 = EXP2(child.children[1])
                varlist += varlist2
                if (type1 != "INT") | (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                textToWrite[subroutine].append("%s %s, %s, %s\n" % (compareType, reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False
            except CompilerError:
                raise CompilerError("Semantic Error in R")
            except: #No Comparison
                pass

    if reg2 != "":
        registers[reg2] = False
    if retType != "BOOL":
        retType = type1
    return (retType, varlist, reg1)

def EXP2(t, subroutine=".main"):
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label == "TERM2":
            if not opFlag:
                type1, varlist1, reg1 = TERM2(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = TERM2(child)
                varlist += varlist2
                if (type1 != "INT") or (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                textToWrite[subroutine].append("add %s, %s, %s\n" % (reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False

        if child.label == "PLUS":
            opFlag = True

    if reg2 != "":
        registers[reg2] = False
    retType = type1
    return (retType, varlist, reg1)

def TERM2(t, subroutine=".main"):
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label == "TERM3":
            if not opFlag:
                type1, varlist1, reg1 = TERM3(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = TERM3(child)
                varlist += varlist2
                if (type1 != "INT") or (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                textToWrite[subroutine].append("sub %s, %s, %s\n" % (reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False

        if child.label == "MINUS":
            opFlag = True

    if reg2 != "":
        registers[reg2] = False
    retType = type1
    return (retType, varlist, reg1)

def TERM3(t, subroutine=".main"):
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label == "FACT2":
            if not opFlag:
                type1, varlist1, reg1 = FACT2(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = FACT2(child)
                varlist += varlist2
                if (type1 != "INT") or (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                textToWrite[subroutine].append("mul %s, %s, %s\n" % (reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False

        if child.label == "MULTIPLICATION":
            opFlag = True

    if reg2 != "":
        registers[reg2] = False
    retType = type1
    return (retType, varlist, reg1)

def FACT2(t, subroutine=".main"):
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label == "FACT3":
            if not opFlag:
                type1, varlist1, reg1 = FACT3(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = FACT3(child)
                varlist += varlist2
                if (type1 != "INT") or (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                textToWrite[subroutine].append("div %s, %s, %s\n" % (reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False

        if child.label == "DIVISION":
            opFlag = True
    if reg2 != "":
        registers[reg2] = False
    retType = type1
    return (retType, varlist, reg1)

def FACT3(t, subroutine=".main"):
    opFlag = False
    type1 = ""
    type2 = ""
    varlist = []
    retType = "INT"
    reg1 = ""
    reg2 = ""

    for child in t.children:
        if child.label == "PRIMARY":
            if not opFlag:
                type1, varlist1, reg1 = PRIMARY(child)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = PRIMARY(child)
                varlist += varlist2
                if (type1 != "INT") or (type2 != "INT"):
                    raise CompilerError("Semantic Error: Compare operand on non-int")
                textToWrite[subroutine].append("rem %s, %s, %s\n" % (reg1, reg1, reg2))
                if reg2 != "":
                    registers[reg2] = False
                opFlag = False

        if child.label == "REMAINDER":
            opFlag = True
    if reg2 != "":
        registers[reg2] = False
    retType = type1
    return (retType, varlist, reg1)

def PRIMARY(t, subroutine=".main"):
    varlist = []
    retType = ""
    reg = ""

    for register in registers:
        if registers[register] == False:
            reg = register
            break
    registers[reg] = True

    child = t.children[0]
    if child.label == "EXPRESSION":
        registers[reg] = False
        retType, varlist1, reg1 = EXPRESSION(child)
        varlist += varlist1
        reg = reg1
        # textToWrite[subroutine].append("move %s, %s\n"%(reg,reg1))
        # registers[reg1] = False

    elif child.label == "INTLIT":
        retType = "INT"
        textToWrite[subroutine].append("li %s, %s\n"%(reg,child.val))
    elif child.label == "BOOLLIT":
        retType = "BOOL"
        if child.val == "True":
            textToWrite[subroutine].append("li %s, %s\n" % (reg, "1"))
        else:
            textToWrite[subroutine].append("li %s, %s\n" % (reg, "0"))
    elif child.label == "IDENT":
        var = child.children[0].val
        retType = dict1[var][1]
        varlist.append(var)
        textToWrite[subroutine].append("la $s0, %s\n"%var)
        textToWrite[subroutine].append("lw %s, ($s0)\n"%reg)
    return (retType,varlist, reg)


def DOINFIX(s, subroutine=".main"):
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
                textToWrite[subroutine].append("li $t1, %s\n" % a1)
            elif a1 == "$t0":
                d1 = "$t0"
            elif a1 == "$t3":
                d1 = "$t3"
            else:
                textToWrite[subroutine].append("la $s0, %s\nlw $t1, ($s0)\n" %a1)

            if re.match("\d",a2):
                textToWrite[subroutine].append("li $t2, %s\n" % a2)
            elif a2 == "$t0":
                d2 = "$t0"
            elif a2 == "$t3":
                d2 = "$t3"
            else:
                textToWrite[subroutine].append("la $s0, %s\nlw $t2, ($s0)\n" %a2)
            textToWrite[subroutine].append("sub %s,%s,%s\n"%(reg,d1,d2))
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
                textToWrite[subroutine].append("li $t1, %s\n" % a1)
            elif a1 == "$t0":
                d1 = "$t0"
            elif a1 == "$t3":
                d1 = "$t3"
            else:
                textToWrite[subroutine].append("la $s0, %s\nlw $t1, ($s0)\n" %a1)

            if re.match("\d",a2):
                textToWrite[subroutine].append("li $t2, %s\n" % a2)
            elif a2 == "$t0":
                d2 = "$t0"
            elif a2 == "$t3":
                d2 = "$t3"
            else:
                textToWrite[subroutine].append("la $s0, %s\nlw $t2, ($s0)\n" %a2)
            textToWrite[subroutine].append("add %s,%s,%s\n"%(reg,d1,d2))
            vs.append(reg)
            firstFlag = False
        else:
            vs.append(elem)

    if vs.__len__() == 1: #if no operations
        a = vs.pop()
        if re.match("\d",a):
            textToWrite[subroutine].append("li $t0, %s\n" % a)
        elif a == "$t0":
            return
        else:
            textToWrite[subroutine].append("la $s0, %s\nlw $t0, ($s0)\n" %a)



def ASSIGN(t, subroutine=".main"):

    #recieves a tree with root t being ASSIGNMENT
    var = t.children[0].children[0].val #variable being assigned
    vartype = dict1[var][1]
    # reset registers
    for register in registers:
        registers[register] = False
        #TEMPORARY
    # r = t.children[1].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
    # if r.label is "BOOLLIT":
    #     if vartype != "BOOL":
    #         raise CompilerError("Semanic Error: not a bool")
    #     if r.val == "True":
    #         textToWrite[subroutine].append("li $t0, 1\n")
    #     elif r.val == "False":
    #         textToWrite[subroutine].append("li $t0, 0\n")
    # elif r.label is "INTLIT":
    #     if vartype != "INT":
        #         raise CompilerError("Semanic Error: not an int")
    #     textToWrite[subroutine].append("li $t0, %s\n" % r.val)
        #Will need to add this back in
    # print(str(t.children[1]))
    # print(str(dict1))
    if t.children[1].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].label == "STRING":
        c =t.children[1].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0]
        find = var + ": .asciiz "
        replace = var + ": .asciiz " + c.val
        ind = datatoWrite.index(find)
        datatoWrite[ind] = replace
    else:
        type, varlist, reg = EXPRESSION(t.children[1])
        for v in varlist:
            # print(v)
            # print(str(dict1))
            if dict1[v][0] != "True":
                    raise CompilerError("Semantic Error: ASSIGN before a variable is instantiated")
        if vartype != type:
            # print(vartype + " " + type)
            raise CompilerError("Assignment types do not match")
        if vartype == "STRING": #Find var line in datatoWrite and make its initial value the dict2 value from varlist[0]
            find = var + ": .asciiz "
            replace = var + ": .asciiz " + dict2[varlist[0]]
            ind = datatoWrite.index(find)
            datatoWrite[ind] = replace
        else: #Integer/bool assign
            textToWrite[subroutine].append("la   $s0, %s\nsw %s, ($s0)\n\n" %(var,reg))  # store value from $t0 into var's address

    dict1[var] = ("True",dict1[var][1])

# Defines what #infix does
def INFIX(t, subroutine=".main"):
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

def IF(tree, subroutine=".main"):
    # for s in tree.children:
    #     print(" fi + " + s.label)
    doElse = False
    label1, label2 = getLabels()
    type, varlist, reg = EXPRESSION(tree.children[1])
    if type != "BOOL":
        raise CompilerError("Condition of If Statement is not a boolean: " + str(type))

    textToWrite[subroutine].append("blez %s, %s\n" % (reg, label1))  # if false jump past IF program (else)

    for child in tree.children[2].children[1].children: #IF program mips
        STATEMENT(child)

    try:
        if tree.children[3].label == "ELSE":
            doElse = True
    except IndexError:
        pass

    if doElse:
        textToWrite[subroutine].append("b %s\n" % label2)  # if we finish IF program then jump past ELSE program

    textToWrite[subroutine].append(label1 + ": nop\n") #label1 before else program

    if doElse:
        for child in tree.children[4].children[1].children:  # ELSE program mips
            STATEMENT(child)

        textToWrite[subroutine].append(label2 + ": nop\n") #place label to at the command following the else program
    
    # global nestedIfCounter #count nested ifs
    # conditionalTree = tree.children[1] #this holds the conditional of the if statement
    # statementListTree = tree.children[2].children[1] #this holds the actual statementList inside the if
    # #pass expressionTree to expression, format the if statement in MIPS using branches
    # boolResult = 0 #will eventually hold the result of the bool expression
    # hasElse = 0
    # try: # may or may not have a matching else
    #     elseTree = tree.children[3] # just 'else'
    #     elseBody = tree.children[4].children[1]
    #     textToWrite[subroutine].append("bne %s, $zero, ELSE%d\nCONSEQUENCE%d:\n" % (reg, nestedIfCounter, nestedIfCounter))
    #     for childX in statementListTree.children:
    #         STATEMENT(childX)
    #     textToWrite[subroutine].append("j ENDIF%d\n\nELSE%d:\n" % (nestedIfCounter, nestedIfCounter))
    #     for childY in elseBody.children:
    #         STATEMENT(childY)
    #     textToWrite[subroutine].append("j ENDIF%d\n\n" % nestedIfCounter)
    #     hasElse = 1
    # except:
    #     pass
    # if hasElse == 0:
    #     textToWrite[subroutine].append("bne %s, $zero, endif%d\nCONSEQUENCE%d:\n" % (reg, nestedIfCounter, nestedIfCounter)) #assuming the result of the boolResult is stored in $t0
    #     #pass programTree to Statement list
    #     for childX in statementListTree.children:
    #         STATEMENT(childX)
    #     textToWrite[subroutine].append("j ENDIF%d\n\n" % nestedIfCounter)
    # textToWrite[subroutine].append("ENDIF%d\n" % nestedIfCounter)
    # nestedIfCounter = nestedIfCounter + 1



labelNum = 1
def getLabels():
    global labelNum
    label1 = "L" + str(labelNum)
    labelNum += 1
    label2 = "L" + str(labelNum)
    labelNum += 1
    return (label1,label2)

def WHILE(tree, subroutine=".main"):
    label1, label2 = getLabels()
    textToWrite[subroutine].append(label1 + ": nop\n")
    type, varlist, reg = EXPRESSION(tree.children[1])
    if type != "BOOL":
        raise CompilerError("Condition of WHILE Statement is not a boolean: " + str(type))

    textToWrite[subroutine].append("blez %s, %s\n"% (reg, label2)) #if false jump past program

    for child in tree.children[2].children[1].children:
        STATEMENT(child)

    textToWrite[subroutine].append("b %s\n"% label1) #jump back to evaluate expression
    textToWrite[subroutine].append(label2 + ": nop\n") #Set jump past point to the instruction after the WHILE

    # for s in tree.children:
    #     print(" wh + " + s.label)



def STATEMENT(tree, subroutine=".main"): #Equivalent of STATEMENT

    if tree.isLeaf():
        pass
    if tree.label =="STATEMENT":
        # print(tree.children[0].label)
        if tree.children[0].label == "READ":
            arguments = []
            for child in tree.children[1].children:
                if child.children[0].label is "ID":
                    arguments.append(child.children[0].val)
            READ_IDS(arguments)
        elif tree.children[0].label == "WRITE":
            # arguments = []
            # for child in tree.children[1].children:
            #     if child.children[0].children[0].label is "INTLIT":
            #         arguments.append(child.children[0].children[0].val)
            #     elif child.children[0].children[0].children[0].label is "ID":
            #         arguments.append(child.children[0].children[0].children[0].val)
            WRITE_IDS(tree.children[1])
        elif tree.children[0].label == "ASSIGNMENT":
            ASSIGN(tree.children[0])
        elif tree.children[0].label == "BOOLTYPE":
            DEFTYPE(tree)
        elif tree.children[0].label == "STRINGTYPE":
            DEFTYPE(tree)
        elif tree.children[0].label == "INTTYPE":
            DEFTYPE(tree)
        elif tree.children[0].label == "IF":
            IF(tree)
        elif tree.children[0].label == "WHILE":
            WHILE(tree)
        try:
            if tree.children[2].label == "ASSIGNMENTSTR":
                ASSIGNSTR(tree)
        except:
            # print(sys.exc_info())
            pass
    # for child in tree.children:
    #     print("recurse " + child.label)
    #     STATEMENT(child)
    # try:
    #     STATEMENT(tree.children[0])

def ASSIGNSTR(tree, subroutine=".main"):
    global dict1
    setMe = tree.children[1].children[0].val

    if tree.children[2].children[0].children != []:
        to = tree.children[2].children[0].children[0].val
        if strdict[setMe][1] is not "STRING" or strdict[to][1] is not "STRING":
            raise CompilerError("Semantic Error: mismatched types")
        # dict1[to][0] = "True"
        # ldict[setMe] = "True"
        ldict[to] = "True"
        le = dict3[to]
        ineff.append("la $t0, %s\n" % to)
        ineff.append("la $t1, %s\n" % setMe)
        for x in range(0, le):
            ineff.append("lbu $t2, %d($t0)\n" % x)
            ineff.append("sb $t2, %d($t1)\n" % x)

    dict1[setMe] = ("True", dict1[setMe][1])
    ldict[setMe] = "True"


def DEFTYPE(tree, subroutine=".main"):
    pass
    # val = tree.children[1].children[0].val
    # a,b = dict1[val]
    # if a == "True":
    #     raise CompilerError("Semanic Error: Define type twice")
    # else:
    #     dict1[val] = ("True",b)

def findGenerateMIPSCode(t, dict): #, fname):

    # print(str(t))
    global datatoWrite
    global textToWrite
    global toWrite
    global dict1
    global dict2
    global dict3
    global strdict
    global ineff
    global ldict
    global stringnum
    
    datatoWrite = [] #data write section
    toWrite = [] # initialize what to write
    textToWrite = {".main":[]}
    dict1 = {} #main dict (Initiated, type)
    dict2 = {} #string dict
    dict3 = {}
    strdict = {}
    ineff = []
    ldict = {}
    stringnum = 0    
    strdict = dict
    datatoWrite.append(".data\n") #beginning of our MIP
    datatoWrite.append('False: .asciiz "False"\n')
    datatoWrite.append('True: .asciiz "True"\n')
    #Generate data section from dict
    for var in dict:
        # print(var)
        # print(dict[var])
        # if dict[var][0] == "" or dict[var][1] == "": #unsure
        #     raise CompilerError("Semantic error: Bad Dictionary")
        if dict[var][1] == 'STRING':
            datatoWrite.append("%s: .asciiz " % var)
            datatoWrite.append(dict[var][0])
            dict3[var] = len(dict[var][0]) - 2
            datatoWrite.append("\n")
        elif dict[var][1] == 'BOOL':
            # if 'True' in dict[var] or 'False' in dict[var]:
            datatoWrite.append("%s: .word 4\n" % var)
            # else:
            #     raise CompilerError("Semanic Error: Variable not declared correctly!")
        elif dict[var][1] == 'INT':
            datatoWrite.append("%s: .word 4\n" % var)
            # sync dictionaries
        if var != "":
            dict1[var] = ("False", dict[var][1])
        if dict[var][0] != "True" and dict[var][0] != "False" and var != "":
            dict2[var] = dict[var][0]


    # print(dict1)
    # print(dict2)
    # textToWrite[subroutine].append("\n.text\nmain:\n")
    #initiate the actual traversal
    #print(t.children[1].label)
    for childd in t.children[1].children:
        print(childd)
        STATEMENT(childd)
    #gracefully exit
    #textToWrite[subroutine].append("li   $v0, 10\nsyscall")
    #write the array to the file
    mainToWrite = textToWrite.pop(".main", None)
    for text in mainToWrite:
        toWrite.append(text)
    for s in textToWrite:
        for k in textToWrite[s]:
            toWrite.append(k)
    return datatoWrite + toWrite

class CompilerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
