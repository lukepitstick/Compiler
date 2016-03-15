"""
Parser for the Micro-language.
Grammar:
   <program> -> begin <statement_list> end
   <statement_list> -> <statement>; { <statement; }
   <statement> -> <assign> | read( <id_list> ) | write( <expr_list> )
   <assign> -> <ident> := <expression>
   <id_list> -> <ident> {, <ident>}
   <expr_list> -> <expression> {, <expression>}
   <expression> -> <primary> {<arith_op> <primary>}
   <primary> -> (<expression>) | <ident> | INTLITERAL
   <ident> -> ID
   <arith_op> -> + | -
"""
# Compiler Design Group 7
# Luke Pitstick
# Christopher Dieter
# Kwangju Kim
# Julius Ware

from lexer_sol import lexer
from tree import tree
from traceback import print_exc

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

class ParserError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return self.msg


#######################################
# Parsing code
dict = {None:None}; #instantiate symbol table
del dict[None]
def parser(source_file, token_file):	
    """
    source_file: A program written in the ML langauge.
    returns True if the code is syntactically correct.
    Throws a ParserError otherwise.
    """
    dict.clear() #clear dict
    G = lexer(source_file, token_file)

    t = None; # this should be changed to the tree

    try:
        t, current = PROGRAM(next(G), G)
    except StopIteration:
        raise ParserError("File finished before end")

    if current.name != '$':
        raise ParserError("File did not end after 'end'")
    return t, dict #return tree and symbol table

@add_debug	
def PROGRAM(current, G):
    t = tree("PROGRAM")
    if current.name == "BEGIN":
        t1 = tree("BEGIN")
        t.append(t1)
        t2, current = STATEMENT_LIST(next(G), G)
        t.append(t2)
        if current.name == "END":
            t.append(tree("END"))
            return t, next(G)
        raise ParserError("No 'end' at line: " + current.line)
    raise ParserError("No 'begin' at line: " + current.line)

@add_debug
def STATEMENT_LIST(current, G):
    t = tree("STATEMENT_LIST")
    t1, current = STATEMENT(current, G)
    t.append(t1)
    while True:
        if current.name == 'SEMICOLON':
            # t.append(tree('SEMICOLON'))
            current = next(G)
            if current.name == "END":
                #t.append(tree('END'))
                return t, current
            t2, current = STATEMENT(current, G)
            t.append(t2)
        else:
            raise ParserError("no semicolon at line: " + current.line)
    return t, current

@add_debug
def STATEMENT(current, G):
    t = tree("STATEMENT")
    if current.name == "READ":
        t.append(tree("READ"))
        t1, current = READ(next(G), G)
        # print("READ" + str(type(current)))
        t.append(t1)
    elif current.name == "WRITE":
        t.append(tree("WRITE"))
        t2, current = WRITE(next(G), G)
        # print("WRITE" + str(type(current)))
        t.append(t2)
    else:
        t3, current = ASSIGNMENT(current, G)
        # print("ASSIGNMENT" + str(type(current)))
        t.append(t3)
    return t, current

@add_debug
def READ(current, G):
    if current.name != "LPAREN":
        raise ParserError("Expected lparen is missing: " + current.line)
    # t.append(tree("LPAREN"))
    t, current = ID_LIST(next(G), G)
    if current.name != "RPAREN":
        raise ParserError("Expected rparen is missing: " + current.line)
    # t.append(tree("RPAREN"))
    return t, next(G)

@add_debug
def WRITE(current, G):
    if current.name != "LPAREN":
        raise ParserError("Expected lparen is missing: " + current.line)
    # t.append(tree("LPAREN"))
    t, current = EXPR_LIST(next(G), G)
    if current.name != "RPAREN":
        raise ParserError("Expected rparen is missing: " + str(current.line_num) + current.pattern)
    # t.append(tree("RPAREN"))
    return t, next(G)

@add_debug
def ASSIGNMENT(current, G):
    t = tree("ASSIGNMENT")
    tident, current = IDENT(current, G)
    t.append(tident)
    if current.name != "ASSIGNOP":
        raise ParserError("Expected assignop is missing: " + current.line)
    # t.append(tree("ASSIGNOP"))
    texpr, current = EXPRESSION(next(G), G)
    t.append(texpr)
    return t, current

"""
Maybe we can also try this way...

@add_debug
def ID_EXPR_LIST(current, G, Fn): # Fn can be either IDENT or EXPRESSION
    if Fn != IDENT or Fn != EXPRESSION:
        raise P
    current = Fn(current, G)
    while True:
        if current.name == 'COMMA':
            current = next(G)
        current = Fn(current, G)
        if current.name != 'COMMA':
            break;
    return current

"""

@add_debug
def ID_LIST(current, G):
    t = tree("ID_LIST")
    t1, current = IDENT(current, G)
    t.append(t1)
    while True:
        if current.name == 'COMMA':
            # t.append(tree('COMMA'))
            current = next(G)
            t2, current = IDENT(current, G)
            t.append(t2)
        if current.name != 'COMMA':
            break
    return t, current

@add_debug
def EXPR_LIST(current, G):
    t = tree("EXPR_LIST")
    t1, current = EXPRESSION(current, G)
    t.append(t1)
    while True:
        if current.name == 'COMMA':
            # t.append(tree('COMMA'))
            current = next(G)
            t2, current = EXPRESSION(current, G)
            t.append(t2)
        if current.name != 'COMMA':
            break;
    return t, current

@add_debug
def EXPRESSION(current, G):
    t = tree("EXPRESSION")
    t1, current = PRIMARY(current, G)
    t.append(t1)

    while True:
        if (current.name == 'PLUS') | (current.name == 'MINUS'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = PRIMARY(current, G)
            t.append(t2)
        if (current.name != 'PLUS') & (current.name != 'MINUS'):
            return t, current
    # while True:
    #     if ARITHOP(current, G).name != 'PLUS' or 'MINUS': # ????
    #         break
    #     current = PRIMARY(next(G), G)
    # return current

@add_debug
def PRIMARY(current, G):
    t = tree('PRIMARY')
    if current.name == 'INTLIT':
        tmp = tree('INTLIT')
        tmp.val = current.pattern
        t.append(tmp)
        return t, next(G)
    if current.name == 'LPAREN':
        # t.append(tree('LPAREN'))
        t1, current = EXPRESSION(next(G), G)
        if current.name != 'RPAREN':
            raise ParserError("Expected rparen is missing: " + current.line)
        t.append(t1)
        return t, next(G)
    t2, current = IDENT(current, G)
    t.append(t2)
    return t, current

@add_debug
def IDENT(current, G):
    t = tree('IDENT')
    if current.name != 'ID':
        raise ParserError("Error when parsing IDENT: " + current.line)
    tmp = tree('ID')
    tmp.val = current.pattern
    t.append(tmp)
    dict[current.pattern] = current.line; #add symbol to symbol table, will use different values later.
    return t, next(G)

# @add_debug
# def ARITHOP(current, G):
#     pass

if __name__ == "__main__":
    try:
        test_case = ['begin', 'read(x);', 'end']
        with open("own_test.txt", "w") as fp:
            fp.write("\n".join(test_case) + "\n")
        try:
            print('Test case: ' + str(test_case))
            sampt, tokk = parser('own_test.txt', 'tokens.txt')
            newk = '(BEGIN,((READ,((ID)IDENT)ID_LIST)STATEMENT)STATEMENT_LIST,END)PROGRAM;'
            if str(sampt) != newk:
                raise Exception('An internal error occured. Recheck the source code.')
            print('Test case successful: \n' + str(sampt) + '\nIS\n' + newk)
        except ParserError:
            print_exc()
            print('Test case failed.')
        finally:
            print('=========================================================================')
        for i in range(1, 7):
            fname = 'sample' + str(i) + '.txt'
            print("Parsing " + fname)
            try:
                parser(fname, 'tokens.txt')
                print('The source file is following a valid syntax.')
            except ParserError:
                print_exc()
                print('The source file is not following a valid syntax.')
            finally:
                 print('=========================================================================')
    except ImportError:
        print('The sample file does not exist.')
    finally:
        print('Personal tester is over.')
