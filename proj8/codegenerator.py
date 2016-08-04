import tree #from tree?
import re
import sys
datatoWrite = [] #data write section
textToWrite = {"close":["\nclose:\nli $v0, 10\nsyscall\n"], "main":[".text\nmain:\n"]} # initialize main section what to write, will also add subroutines
toWrite = [] # initialize what to write (remained for compatibility)
dict1 = {} #main dict (Initiated, type)
dict2 = {} #string dict
dict3 = {}
strdict = {}
ineff = []
ldict = {}
notGlobal = {}
stringnum = 0
nestedIfCounter = 0

# ========== DEBUG PART ================== #

debug = False
recursion_level = 0

def add_debug(fn):
    def debugged_fn(tree, subroutine="main"):
        global recursion_level
        print(" "*recursion_level + "Entering: %s (%s)" % (fn.__name__, subroutine))
        recursion_level += 3
        R = fn(tree, subroutine)
        recursion_level -= 3
        print(" "*recursion_level + "Leaving: %s" % (fn.__name__))
        return R
    
    return debugged_fn if debug else fn

# ========== DEBUG PART ENDS ============= #

@add_debug
def READ_IDS(args, subroutine="main"): #was args = []
    global textToWrite
    global dict1
    
    for var in args:
        if dict1[var][1] == "INT":
            textToWrite[subroutine].append("li $v0, 5\n")
            textToWrite[subroutine].append("syscall\n")
            textToWrite[subroutine].append("la $t0, %s\n" % var)
            textToWrite[subroutine].append("sw $v0, 0($t0)\n\n")
            dict1[var] = ("True","INT")
        else:
            raise CompilerError("Semantic Error: Read on invalid type: " + var)


@add_debug
def WRITE_IDS(t, subroutine="main"): #receives tree with head as expr_list
    global stringnum
    global registers
    
    # reset registers
    for register in registers:
        registers[register] = False
    for child in t.children:
        # child.children[0].children[0].children[0].children[0].children[0].children[0].children[0].getChildLabel()
        if \
        child.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].label \
        == "STRING":
            val = child.children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].children[0].val
            stringid = "stringtmptmp" + str(stringnum)
            stringnum += 1
            datatoWrite.append("%s: .asciiz %s\n" %(stringid, val))
            textToWrite[subroutine].append("la $a0, %s\nli $v0, 4\nsyscall\n\n" % stringid)
        else:
            # reset registers
            for register in registers:
                registers[register] = False
            type, varlist, reg = EXPRESSION(child, subroutine)
            v1 = ""
            for v in varlist:
                # if ldict[v] != "True":
                v1 = v
                globalv = "global" + v[len(v)-1:len(v)]
                # print("V: " + globalv)
                if (v == "FALSE") or (v == "TRUE"):
                    pass
                else:
                    if dict1[v][0] != "True":
                        if dict1[globalv][0] != "True":
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


registers = {"$t0":False, "$t1":False, "$t2":False, "$t3":False, "$t4":False, "$t5":False, "$t6":False, "$t7":False, 
             "$t8":False, "$t9":False, "$s1":False, "$s2":False, "$s3":False, "$s4":False, "$s5":False, "$s6":False,
             "$s7":False}

@add_debug
def EXPRESSION(t, subroutine="main"): #Gets tree with EXPRESSION as head

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
                type1, varlist1, reg1 = TERM1(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = TERM1(child, subroutine)
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

@add_debug
def TERM1(t, subroutine="main"): #Gets tree with TERM1 as head
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
                type1, varlist1, reg1 = FACT1(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = FACT1(child, subroutine)
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

@add_debug
def FACT1(t, subroutine="main"): #Gets tree with FACT1 as head
    # print("sub: " + subroutine)
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
                type1, varlist1, reg1 = EXP2(child, subroutine)
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
                type2, varlist2, reg2 = EXP2(child.children[1], subroutine)
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

@add_debug
def EXP2(t, subroutine="main"):
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
                type1, varlist1, reg1 = TERM2(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = TERM2(child, subroutine)
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


@add_debug
def TERM2(t, subroutine="main"):
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
                type1, varlist1, reg1 = TERM3(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = TERM3(child, subroutine)
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


@add_debug
def TERM3(t, subroutine="main"):
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
                type1, varlist1, reg1 = FACT2(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = FACT2(child, subroutine)
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


@add_debug
def FACT2(t, subroutine="main"):
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
                type1, varlist1, reg1 = FACT3(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = FACT3(child, subroutine)
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


@add_debug
def FACT3(t, subroutine="main"):
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
                type1, varlist1, reg1 = PRIMARY(child, subroutine)
                varlist += varlist1
            if opFlag:
                type2, varlist2, reg2 = PRIMARY(child, subroutine)
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


@add_debug
def PRIMARY(t, subroutine="main"):
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
        retType, varlist1, reg1 = EXPRESSION(child, subroutine)
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
        if retType == "INT":
            globalvar = 'global' + var
            # print(str(dict1))
            if subroutine in notGlobal:
                if var in notGlobal[subroutine]:
                    var = subroutine + var
                elif globalvar in dict1:
                    var = globalvar
                else:#ahahahaha
                    var = subroutine + var
            elif globalvar in dict1:
                var = globalvar
            else:
                var = subroutine + var
        varlist.append(var)
        textToWrite[subroutine].append("la $s0, %s\n"%var)
        textToWrite[subroutine].append("lw %s, ($s0)\n"%reg)
    return (retType,varlist, reg)


@add_debug
def ASSIGN(t, subroutine="main"):

    #recieves a tree with root t being ASSIGNMENT
    var = t.children[0].children[0].val #variable being assigned
    vartype = dict1[var][1]
    if vartype == "INT":
        skip = False
        vtmp = var
        var = subroutine + var

        if subroutine in notGlobal:
            if vtmp in notGlobal[subroutine]:
                var = subroutine + vtmp
                skip = True


        if (dict1[var][0] == 'False') & (not skip):
            # print(subroutine + str(notGlobal))
            var = 'global' + vtmp
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
        type, varlist, reg = EXPRESSION(t.children[1], subroutine)
        for v in varlist:
            globalv = "global" + v[len(v) - 1:len(v)]
            # print(v)
            # print(str(dict1))
            # if vartype == 'INT':
            #     if dict1[subroutine + v][0] != "True":
            #         raise CompilerError("Semantic Error: ASSIGN before a variable is instantiated: %s" % t.children[1])
            # else:
            if dict1[v][0] != "True":
                if dict1[globalv][0] != "True":
                        raise CompilerError("Semantic Error: ASSIGN before a variable is instantiated: %s" % t.children[1])
        if vartype != type:
            # print(vartype + " " + type)
            raise CompilerError("Assignment types do not match: %s" % t.children[1])
        if vartype == "STRING": #Find var line in datatoWrite and make its initial value the dict2 value from varlist[0]
            find = var + ": .asciiz "
            replace = var + ": .asciiz " + dict2[varlist[0]]
            ind = datatoWrite.index(find)
            datatoWrite[ind] = replace
        else: #Integer/bool assign
            textToWrite[subroutine].append("la   $s0, %s\nsw %s, ($s0)\n\n" %(var,reg))  # store value from $t0 into var's address

    # if vartype == 'INT':
    #     dict1[subroutine + var] = ("True", dict1[subroutine + var][1])
    # else:
        dict1[var] = ("True",dict1[var][1])


@add_debug
def IF(tree, subroutine="main"):
    # for s in tree.children:
    #     print(" fi + " + s.label)
    doElse = False
    label1, label2 = getLabels()
    type, varlist, reg = EXPRESSION(tree.children[1], subroutine)
    if type != "BOOL":
        raise CompilerError("Condition of If Statement is not a boolean: " + str(type))

    textToWrite[subroutine].append("blez %s, %s\n" % (reg, label1))  # if false jump past IF program (else)

    for child in tree.children[2].children[1].children: #IF program mips
        STATEMENT(child, subroutine)

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
            STATEMENT(child, subroutine)

        textToWrite[subroutine].append(label2 + ": nop\n") #place label to at the command following the else program



labelNum = 1

def getLabels():
    global labelNum
    label1 = "L" + str(labelNum)
    labelNum += 1
    label2 = "L" + str(labelNum)
    labelNum += 1
    return (label1,label2)


@add_debug
def WHILE(tree, subroutine="main"):
    label1, label2 = getLabels()
    textToWrite[subroutine].append(label1 + ": nop\n")
    type, varlist, reg = EXPRESSION(tree.children[1],subroutine)
    if type != "BOOL":
        raise CompilerError("Condition of WHILE Statement is not a boolean: " + str(type))

    textToWrite[subroutine].append("blez %s, %s\n"% (reg, label2)) #if false jump past program

    for child in tree.children[2].children[1].children:
        STATEMENT(child, subroutine)

    textToWrite[subroutine].append("b %s\n"% label1) #jump back to evaluate expression
    textToWrite[subroutine].append(label2 + ": nop\n") #Set jump past point to the instruction after the WHILE


@add_debug
def STATEMENT(tree, subroutine="main"): #Equivalent of STATEMENT
    if tree.isLeaf():
        pass
    if tree.label =="STATEMENT":
        # print(tree.children[0].label)
        if tree.children[0].label == "READ":
            arguments = []
            for child in tree.children[1].children:
                if child.children[0].label is "ID":
                    arguments.append(child.children[0].val)
            READ_IDS(arguments, subroutine)
        elif tree.children[0].label == "WRITE":
            WRITE_IDS(tree.children[1], subroutine)
        elif tree.children[0].label == "ASSIGNMENT":
            ASSIGN(tree.children[0], subroutine)
        elif tree.children[0].label == "BOOLTYPE":
            DEFTYPE(tree, subroutine)
        elif tree.children[0].label == "STRINGTYPE":
            DEFTYPE(tree, subroutine)
        elif tree.children[0].label == "INTTYPE":
            global notGlobal
            notGlobal[subroutine] = {tree.children[1].children[0].val:  "True"}
            # print(str(tree.children[0]
            DEFTYPE(tree, subroutine)
        elif tree.children[0].label == "IF":
            IF(tree, subroutine)
        elif tree.children[0].label == "WHILE":
            WHILE(tree, subroutine)
        elif tree.children[0].label == "FUNCCALL":
            FUNCCALL(tree,subroutine)
        try:
            if tree.children[2].label == "ASSIGNMENTSTR":
                ASSIGNSTR(tree, subroutine)
        except:
            # print(sys.exc_info())
            pass


@add_debug
def ASSIGNSTR(tree, subroutine="main"):
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


@add_debug
def DEFTYPE(tree, subroutine="main"):
    pass
    # val = tree.children[1].children[0].val
    # a,b = dict1[val]
    # if a == "True":
    #     raise CompilerError("Semanic Error: Define type twice")
    # else:
    #     dict1[val] = ("True",b)


@add_debug
def FUNCTION(tr,mainIdx, subroutine=None):
    global textToWrite
    # print(tr.label)
    setFuncReturn = True
    funcReturn = ""
    funcidtag = ""
    if tr.label == "GLOBAL":
        # print("todo")
        pass
    else:
        for childFuncs in tr.children:  # gets the functions
            for childd in childFuncs.children:
                # print(childd.label)
                if childd.label == "ID":
                    if setFuncReturn:
                        funcReturn = childd.val
                        setFuncReturn = False
                    else:
                        funcidtag = childd.val
                        # print(funcidtag)
                        setFuncReturn = True
                elif childd.label == "PROGRAM":
                    textToWrite[funcidtag] = [("\n\n%s:\n" % funcidtag)]
                    for child2 in childd.children[1].children:
                        STATEMENT(child2, subroutine=funcidtag)
                    textToWrite[funcidtag].append("\njr $ra\n")
                else:
                    raise CompilerError("Inappropriate token detected: %s" % childd.label)
    #print(">>> SUBROUTINE FOR FUNCTION CALL SHOULD BE IMPLEMENTED. <<<")

@add_debug
def FUNCCALL(t,subroutine = "main"):
    textToWrite[subroutine].append("jal %s\n"%t.children[0].val)
    # print(str(t))
    # print(str(t.children[0].val))


def findGenerateMIPSCode(t, dict_, dict2_): #, fname):
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
    global scopedict
    
    datatoWrite = [] #data write section
    toWrite = [] # initialize what to write
    textToWrite = {"close":["\nclose:\nli $v0, 10\nsyscall\n"], "main":[".text\nmain:\n"]}
    dict1 = {} #main dict (Initiated, type)
    dict2 = {} #string dict
    dict3 = {}
    scopedict = {}
    strdict = {}
    ineff = []
    ldict = {}
    stringnum = 0    
    strdict = dict1
    datatoWrite.append(".data\n") #beginning of our MIP
    datatoWrite.append('False: .asciiz "False"\n')
    datatoWrite.append('True: .asciiz "True"\n')
    #Generate data section from dict
    # print(str(dict2_["varScopeDict"]))
    for fun in dict2_["varScopeDict"]:
        for funvar in dict2_["varScopeDict"][fun]:
            newname = fun + funvar
            if(fun == "global"):
                scopedict[newname] = ('True', dict2_["varScopeDict"][fun][funvar][1])
            else:
                scopedict[newname] = ('False',dict2_["varScopeDict"][fun][funvar][1])
        # print(funname)
    # print(str(scopedict));
    for newvar in scopedict:
        datatoWrite.append("%s: .word 4\n" % newvar)

    for var in dict_:
        if dict_[var][1] == 'STRING':
            datatoWrite.append("%s: .asciiz " % var)
            datatoWrite.append(dict_[var][0])
            dict3[var] = len(dict_[var][0]) - 2
            datatoWrite.append("\n")
        elif dict_[var][1] == 'BOOL':
            # if 'True' in dict[var] or 'False' in dict[var]:
            datatoWrite.append("%s: .word 4\n" % var)
            # else:
            #     raise CompilerError("Semanic Error: Variable not declared correctly!")
        elif dict_[var][1] == 'INT':
            pass
            # datatoWrite.append("%s: .word 4\n" % var)
            # sync dictionaries
        if var != "":
            # if dict_[var][1] != 'INT':
                dict1[var] = ("False", dict_[var][1])
        if dict_[var][0] != "True" and dict_[var][0] != "False" and var != "":
            dict2[var] = dict1[var][0]

    for scope in scopedict:
        dict1[scope] = scopedict[scope]
    # print(dict1)
    # print(dict2)
    # textToWrite[subroutine].append("\n.text\nmain:\n")
    #initiate the actual traversal
    #print(t.children[1].label)
    # t.getChildLabel()
    mainIdx = 0
    while t.children[mainIdx].label != 'PROGRAM':
        FUNCTION(t.children[mainIdx],mainIdx)
        mainIdx += 1
    assert(t.children[mainIdx].label == 'PROGRAM')
    for childd in t.children[mainIdx].children[1].children:
        STATEMENT(childd)
    #gracefully exit
    #textToWrite[subroutine].append("li   $v0, 10\nsyscall")
    #write the array to the file
    #print(textToWrite)
    mainToWrite = textToWrite.pop("main", None)
    toWrite.append("\n\n")
    for text in mainToWrite:
        toWrite.append(text)
    toWrite.append("\nj close\n")
    for s in textToWrite:
        #print(s)
        if (len(textToWrite[s]) > 1):
            for k in textToWrite[s]:
                toWrite.append(k)
    closeToWrite = textToWrite.pop("close", None)
    # if errorOccurred():
    #     toWrite.append("\n\nclose:\nli $v0, 11\nsyscall")
    for text in closeToWrite:
        toWrite.append(text)
    # print(toWrite)
    return datatoWrite + toWrite


class CompilerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
