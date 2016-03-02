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

    if current != '$':
        raise ParserError("File did not end after 'end'")
    print('\n')
    print(repr(t))
    print('\n')
    # print(dict)
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
        else:
            raise ParserError("no semicolon at line: " + current.line)
    return t, current

@add_debug
def STATEMENT(current, G):
    t = tree("STATEMENT")
    if current.name == "READ":
        t.append(tree("READ"))
        t1, current = READ(next(G), G)
        t.append(t1)
    elif current.name == "WRITE":
        t.append(tree("WRITE"))
        t2, current = WRITE(next(G), G)
        t.append(t2)
    else:
        t3, current = ASSIGNMENT(current, G)
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
    current = EXPRESSION(next(G), G)
    return current

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
        t.append(tree('INTLIT'))
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
    t.append(tree('ID'))
    dict[current.pattern] = -1; #add symbol to symbol table, will use different values later.
    return t, next(G)

# @add_debug
# def ARITHOP(current, G):
#     pass

if __name__ == "__main__":
    print(parser('sample1.txt', 'tokens.txt'))
