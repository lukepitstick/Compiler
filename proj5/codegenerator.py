#import MIPSinstruction
from tree import tree
import treetraverse
import re

toWrite = [] # initialize what to write
dict1 = {}
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
	for var in args:
		dict1[var] = "true"
		toWrite.append("li $v0, 5\nsyscall\n")
		toWrite.append("la $t0, %s\n" % var)
		toWrite.append("sw $v0, 0($t0)\n\n")

# Syscall the Print (Equivalent to Java's System.out.println())
def WRITE_IDS(args = []):
	for var in args:
		if re.match("\d", var):
			toWrite.append("li $a0, %s\n" % var)
			toWrite.append("li $v0, 1\nsyscall\n\n")
		elif dict1[var] is "true":
			toWrite.append("lw $a0, %s\n" % var)
			toWrite.append("li $v0, 1\nsyscall\n\n")
		else:
			raise Exception("Variable not yet initialized!")
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
		if tree.children[0].label is "READ":
			arguments = []
			for child in tree.children[1].children:
				if child.children[0].label is "ID":
					arguments.append(child.children[0].val)
			READ_IDS(arguments)
		if tree.children[0].label is "WRITE":
			arguments = []
			for child in tree.children[1].children:
				if child.children[0].children[0].label is "INTLIT":
					arguments.append(child.children[0].children[0].val)
				elif child.children[0].children[0].children[0].label is "ID":
					arguments.append(child.children[0].children[0].children[0].val)
			WRITE_IDS(arguments)
	for child in tree.children:
		postOrderDFS(child)

def findGenerateMIPSCode(t, dict, fname):
	outFile = open(fname, "w")
	toWrite.append(".data\n") #beginning of our MIPS
	#Generate data section from dict
	for var in dict:
		dict1[var] = ""
		toWrite.append("%s: .word 4\n" % var) 
	toWrite.append(".text\nmain:\n")
	#initiate the actual traversal
	postOrderDFS(t)
	#write the array to the file
	for line in toWrite:
		outFile.write(line)
	# After traversing the nodes, we invoke certain functions
	pass
