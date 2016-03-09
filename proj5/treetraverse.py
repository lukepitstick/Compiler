import tree
from lexer_sol import Token
import MLparser

def traverse(tr):
    print("Tree struct: " + repr(tr))
    print("Current node: " + str(tr.label))
    if tr.isLeaf():
      pass
    for child in tr.children:
      travrecur(child)

# We use that traverse function
# We will notice when the traverse function hits the certain node 
# we look up the token, its pattern, etc. and if necessary
# call the function.