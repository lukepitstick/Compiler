#import MIPSinstruction
from tree import tree
# import treetraverse
import re

toWrite = [] # initialize what to write
dict1 = {}


def READ_IDS(args): #was args = []
    for var in args:
        dict1[var] = "true"
        toWrite.append("li $v0, 5\nsyscall\n")
        toWrite.append("la $t0, %s\n" % var)
        toWrite.append("sw $v0, 0($t0)\n\n")


def WRITE_IDS(t):
    for child in t.children:
        s,varList = INFIX(child)
        for v in varList:
            if dict1[v] != "true":
                raise CompilerError("Semantic Error: Write before a variable is instantiated")
        DOINFIX(s)
        #print syscall
        toWrite.append("add $a0, $t0,0\n")
        toWrite.append("li $v0, 1\nsyscall\n\n")

    # for var in args:
    #     pass
    #     # if re.match("\d", var):
    #     #     toWrite.append("li $a0, %s\n" % var)
    #     #     toWrite.append("li $v0, 1\nsyscall\n\n")
    #     # elif dict1[var] is "true":
    #     #     toWrite.append("lw $a0, %s\n" % var)
    #     #     toWrite.append("li $v0, 1\nsyscall\n\n")
    #     # else:
    #     #     raise Exception("Variable not yet initialized!")


def DOINFIX(s):
    vs = []
    # print(str(s))
    firstFlag = True;
    while s.__len__() != 0:
        elem = s.pop(0)
        if elem is "-":
            reg = "$t0"
            a2 = vs.pop()
            a1 = vs.pop()
            if not firstFlag:
                if (a1 != "$t0") & (a2 != "$t0"):
                    reg = "$t3"

            # print("plus a2: " +  a2 + "a1: " + a1)
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
            # print("plus a2: " +  a2 + "a1: " + a1)
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
            firstFlag = False;
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

    s, varList = INFIX(t.children[1]) #Infix on expression
    for v in varList:
        if dict1[v] != "true":
                raise CompilerError("Semantic Error: ASSIGN before a variable is instantiated")

    DOINFIX(s)

    toWrite.append("la   $s0, %s\nsw   $t0, ($s0)\n\n" % var) #store value from $t0 into var's address
    dict1[var] = "true" #we have assigned the variable


# Defines what #infix does
def INFIX(t):
    #receives tree t with head as expression
    stack = []
    varList = []
    # print(t)
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
            # print("recurse")
            s,VV = INFIX(child.children[0])
            # print("stack: " + str(s))
            # print(str(VV))
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
    # print("varlist: " + str(varList))
    return stack, varList

    # for child in t.children:
    #         if child.children[0].label == "EXPRESSION":
    #             s,VV = INFIX(child.children[0])
    #             varList.append(VV)
    #             stack.append(s)
    #         elif child.children[0].label == "INTLIT":
    #             stack.append(child.children[0].val)
    #         elif child.children[0].label == "IDENT":
    #             stack.append(child.children[0].children[0].val)
    #             varList.append(child.children[0].children[0].val)
    #         elif child.children[0].label == "PLUS":
    #             stack.append("-")
    #         elif child.children[0].label == "MINUS":
    #             stack.append("+")
    #     return stack, varList


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
    for child in tree.children:
        postOrderDFS(child)


def findGenerateMIPSCode(t, dict): #, fname):
    # outFile = open(fname, "w")
    toWrite.append(".data\n") #beginning of our MIPS
    #Generate data section from dict
    for var in dict:
        dict1[var] = ""
        toWrite.append("%s: .word 4\n" % var)

    toWrite.append(".text\nmain:\n")

    #initiate the actual traversal
    postOrderDFS(t)

    #gracefully exit
    toWrite.append("li   $v0, 10\nsyscall")

    #write the array to the file
    return toWrite

class CompilerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
