#import MIPSinstruction
from tree import tree
import treetraverse

toWrite = [] # initialize what to write

# After the code generation has been done
# We will write everything inside 'toWrite' into
# output.asm file.

def PushCodes(InstToken):
    pass

# Generally does nothing, but we can make
# our own mean of function to do smth
def START():
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
def READ_IDS(args = []):
    """
    Here, we are receiving data so...
    (Maybe integer value?)
    Syscall integers:
    5 - read integer
    8 - read string
    At this point we are not likely to use 6, 7 which is
    read float and double respectively.

    Ex)
    li $v0, 5;
    syscall

    Loads whatsoever value you type to $vx register
    """
    for var in args:
        toWrite.append("la $a0, %s\n" % var)
        toWrite.append("li $v0, 8\nsyscall")

# Syscall the Print (Equivalent to Java's System.out.println())
def WRITE_IDS():
    """
    Here, we are printing data to the CMD

    Ex)
    li $v0, 1
    li $a0, 5
    syscall

    Prints 5
    """
    pass

# Defines what #assign does
def ASSIGN():
    pass

# Defines what #infix does
def INFIX():
    pass

# Defines what #process does
def PROCESS():
    pass

def postOrderDFS(tree):
    if tree.isLeaf():
        pass
    if tree.label is "STATEMENT":
        if tree.children[0].label is"READ":
            arguments = []
            print(tree.children[1].children[0].children[0].val)
            for child in tree.children[1].children[0].children:
                if child.label is "ID":
                    arguments.append(child.val)
            print(arguments)
            READ_IDS(arguments)
    for child in tree.children:
        postOrderDFS(child)

def findGenerateMIPSCode(t, dict, fname):
    outFile = open(fname, "w")
    toWrite.append(".data\n") #beginning of our MIPS
        
    #Generate data section from dict
    for var in dict:
        toWrite.append("%s: .word 4\n" % var)
        
    toWrite.append(".text\n")
    #initiate the actual traversal
    postOrderDFS(t)

    #write the array to the file
    for line in toWrite:
        outFile.write(line)
    # After traversing the nodes, we invoke certain functions
    pass
