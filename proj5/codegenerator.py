#import MIPSinstruction
from tree import tree
import treetraverse

toWrite = [] # initialize what to write
dict = {None:None}

# After the code generation has been done
# We will write everything inside 'toWrite' into
# output.asm file.

def PushCodes(InstToken):
    pass

#Write beginning of MIPS
def START():
    global dict
    toWrite.append(".data\n")

    # Generate data section from dict
    for var in dict:
        pass
    pass

# If reaching this function,
# We have to invoke the code generation.
def FINISH():
    """
    Exit syscall is 10

    Ex)
    li $??, 10
    syscall
    """
    pass

# Syscall the KeyboardInput (Equivalent to Java's Scanner.next())
def READ_IDS(t):

    #for each IDENT in ID_LIST
    for i in t.children[1].children:
        pass

    # """
    # Here, we are receiving data so...
    # (Maybe integer value?)
    # Syscall integers:
    # 5 - read integer
    # 8 - read string
    # At this point we are not likely to use 6, 7 which is
    # read float and double respectively.
    #
    # Ex)
    # li $v0, 5;
    # syscall
    #
    # Loads whatsoever value you type to $vx register
    # """
    pass

# Syscall the Print (Equivalent to Java's System.out.println())
def WRITE_IDS(t):
    global dict

    #for each expression in expression_list
    for i in t.children[1].children:
        varList = INFIX(i)
        for v in varList:
            if dict[v] != True:
                raise CompilerError("Syntax Error: cannot write unnassigned variable")
        pass
    # """
    # Here, we are printing data to the CMD
    #
    # Ex)
    # li $v0, 1
    # li $a0, 5
    # syscall
    #
    # Prints 5
    # """
    pass

# Defines what #assign does
def ASSIGN(t):
    global dict
    #recieves a tree with root t being ASSIGNMENT
    var = t.children[0].children[0].val #variable being assigned

    varList = INFIX(t.children[1]) #Infix on expression

    #output.append() #build output

    dict[var] = True #we have assigned the variable
    pass

# Defines what #infix does
def INFIX(t):
    varList = []

    return varList
    pass

# Defines what #process does
def PROCESS(t):
    pass

def findGenerateMIPSCode(t, dictionary):
    global dict
    dict = dictionary
    START()

    toWrite.append(".main\n") #beginning of .main in MIPS

    #for each statement in statement list
    for i in t.children[1].children:
        if i.children[0].label == "ASSIGNMENT":
            ASSIGN(i.children[0])
        elif i.children[0].label == "WRITE":
            WRITE_IDS(i)
        elif i.children[0].label == "READ":
            READ_IDS(i)

        FINISH()

    # if t.label != "PROGRAM":
    #     raise CompilerError("bad tree, no program");
    # if t.children[0].label != "BEGIN":
    #     raise CompilerError("bad tree, no begin");
    # if t.children[1].label == "STATEMENT_LIST":
    #
    # else:
    #     raise CompilerError("bad tree, no statement list");
    # if t.isLeaf():
    #     return None # Stop iteration, return to the parent node
    # for i in t.children:
    #     pass
    #     # After traversing the nodes, we invoke certain functions

    PushCodes(None)

    pass

class CompilerError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg
