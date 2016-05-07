import re
class tree:
    #Luke Pitstick
    #Sean Scheetz
    #Christopher Dieter
    """
    Tree class, where a tree is a label
    with zero or more trees as children
    """

    def __init__(self, label, val = None, children = None):
        """
        Tree constructor
        """
        self.val = val
        self.label = label
        self.children = children if children != None else []

    def __str__(self):
        """
        Translate to newick string
        """
        if self is None:
            return None

        ret = ""

        ret += self.label;
        if self.isLeaf():
            return ret + ";"

        ret = ")" + ret;

        tmp = ""
        for c in self.children:
            tmp += c.strHelper() + ","
        g = len(tmp)
        tmp = tmp[0:g-1]
        ret = tmp + ret
        ret = "(" + ret + ";"
        ret = re.sub(" ", "", ret)
        return ret

    def strHelper(self):
        ret = ""

        ret += self.label;
        if self.isLeaf():
            return ret

        ret = ")" + ret;

        tmp = ""
        for c in self.children:
            tmp += c.strHelper() + ","
        g = len(tmp)
        tmp = tmp[0:g-1]
        ret = tmp + ret
        ret = "(" + ret
        return ret

    def getChildLabel(self):
        for i in self.children:
            print(i.label)

    def __repr__(self):
        return "Tree: " + str(self)

    def __len__(self):
        """
        Return number of nodes in teee
        """
        count = 0

        if self is None:
            return count

        count += 1

        for c in self.children:
            count += c.__len__()

        return count

    def isLeaf(self):
        """
        Return true/false indicating whether
        the tree is a leaf
        """
        return len(self.children) == 0

    def append(self, t):
        self.children.append(t)



class ParserException(Exception):
    """
    Exception class for parse_newick
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg

debug = False
recursion_level = 0

def add_debug(fn):
    def debugged_fn(current, G):
        global recursion_level
        print(" "*recursion_level + "Entering: %s (%s)" % (fn.__name__, current))
        recursion_level += 3
        R = fn(current, G)
        recursion_level -= 3
        print(" "*recursion_level + "Leaving: %s" % (fn.__name__))
        return R

    return debugged_fn if debug else fn

# Parse_newick Should raise the following ParserException errors when appropriate:
# * Terminating semi-colon missing.
# * Expected label missing.
# * Missing command or ) where expected.
# (You may add others as you see fit.)
#
# Spacing should not matter: "(a,b)c;", and " ( a  ,  b ) c; " should result in idential
# trees.
def parse_newick(s):
    """
    Take a newick string and return the corresponding tree object.
    """
    t = tree("")
    t = parser(s)
    return t

def lexer(s):
    for c in re.sub("\s+", "", s):
        yield c
    yield '$'

#returns a tree object
def parser(s):
    r = s.replace(" ", "")
    G = lexer(r)
    current, t = T(next(G), G)
    if not current == ";":
        raise ParserException("Line must end with semi-colon, current: " + current)
    c = next(G)
    if c != '$':
        raise ParserException("Semi-colon in middle of line")
    return t

#starting production
@add_debug
def T(current, G):
    t = tree("")
    if re.match("\w", current):
        labelStr = current
        current = next(G)
        while re.match("\w", current):
            labelStr += current
            current = next(G)
        t.label = labelStr
        current, child = S(current, G)
        if not child.label == "":
            t.children.append(child)
        return current, t
    if current == "(":
        current, t = TPrime(next(G), G)
        return current, t
    else:
        raise ParserException("Illegal start character")

#secondary production
@add_debug
def TPrime(current, G):
    t = tree("temp")
    #take the first token from after the "(" and send it to processing
    if not re.match("[\w(]", current):
        raise ParserException("Invalid Interior")
    symbol, child = S(current, G)

    if not child.label == "":
        t.children.append(child)
    #if returned token is a comma, then there are more children nodes.
    #process them until a ")" is found.
    while symbol == ",":
        c = next(G)
        if not re.match('[\w(]', c):
            raise ParserException("Comma with no subsequent label")
        symbol, child1 = S(c, G)
        if not child1.label == "":
            t.children.append(child1)
    if not symbol == ")":
        raise ParserException("Mismatched parens!")
    temp = t
    c = next(G);
    if re.match('[,)]', c):
        symbol = c
        t.label = ' '
    elif re.match('\(', c):
        raise ParserException("Invalid parent")
    elif re.match(';', c):
        raise ParserException("semicolon after paren")
    else:
        symbol, temp = S(c, G)
        t.label = temp.label

    return symbol, t

#Tertiary production
@add_debug
def S(current, G):
    t = tree("")
    #end of the line, only comes here for single nodes
    if current == ";":
        return current, t
    #we've found a leaf node, return it as a child
    if re.match("\w", current):
        labelStr = current
        current = next(G)
        while re.match("\w", current):
            labelStr += current
            current = next(G)
        t.label = labelStr
    #we've found a nested tree, let's recurse!
    if current == "(":
        current, t = TPrime(next(G), G)
        return current, t
    return current, t

# Here for testing/debugging purposes
if __name__ == "__main__":
    print("Testing trees:")
    print(parse_newick("label1;").__repr__())
    # print(parse_newick("(a)b;").__repr__())
    # print(parse_newick("(a,c,d,e)b;").__repr__())
    # print(parse_newick("(a,(b)c,(q)h)f;").__repr__())

