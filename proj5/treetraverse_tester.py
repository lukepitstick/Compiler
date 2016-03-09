import tree
from lexer_sol import Token
import MLparser

samp = ['begin', 'read(x, y, z);', 'end']
f = open('traverse.txt', 'w')
for s in samp:
    f.write(s)
    f.write('\n')
f.close()
tr, dc = MLparser.parser('traverse.txt', 'tokens.txt')
travrecur(tr)
