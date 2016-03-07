import tree
from lexer_sol import Token
import MLparser

def traverse(tr):
    pass

def travrecur(tr):
    print("Tree struct: " + repr(tr))
    print("Current node: " + str(tr.label))
    if tr.isLeaf():
      pass
    for child in tr.children:
      travrecur(child)

samp = ['begin', 'read(x, y, z);', 'end']
f = open('traverse.txt', 'w')
for s in samp:
    f.write(s)
    f.write('\n')
f.close()
tr, dc = MLparser.parser('traverse.txt', 'tokens.txt')
travrecur(tr)
