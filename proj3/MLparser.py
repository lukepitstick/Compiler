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
#Luke Pitstick
#Christopher Dieter
#Kwangju Kang
#Julius Ware

from lexer_sol import lexer

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
def parser(source_file, token_file):	
    # print("hey")
    """
    source_file: A program written in the ML langauge.
    returns True if the code is syntactically correct.
    Throws a ParserError otherwise.
    """
    G = lexer(source_file, token_file)
    try:
        current = PROGRAM(next(G), G)
    except StopIteration:
        raise ParserError("File finished before end")

    try:
        next(G)
    except StopIteration:
        return True
    raise ParserError("File did not end after 'end'")

@add_debug	
def PROGRAM(current, G):
    # print(current.pattern)
    if current.name == "BEGIN":
        current = STATEMENT_LIST(next(G), G)
        if current.name == "END":
            return
        raise ParserError("No 'end' at line: " + current.line)
    raise ParserError("No 'begin' at line: " + current.line)

@add_debug
def STATEMENT_LIST(current, G):
    current = STATEMENT(current, G)
    while True:
        if current.name == 'SEMICOLON':
            current = next(G)
            if current.name == "END":
                return current
            current = STATEMENT(current, G)
        if current.name != 'SEMICOLON':
            raise ParserError("no semicolon at line: " + current.line)
    return current

@add_debug
def STATEMENT(current, G):
    if current.name == "READ":
        current = READ(next(G), G)
    elif current.name == "WRITE":
        current = WRITE(next(G), G)
    else:
        current = ASSIGNMENT(current, G)
    return current

@add_debug
def READ(current, G):
    if current.name != "LPAREN":
        raise ParserError("Expected lparen is missing: " + current.line)
    current = ID_LIST(next(G), G)
    if current.name != "RPAREN":
        raise ParserError("Expected rparen is missing: " + current.line)
    return next(G)

@add_debug
def WRITE(current, G):
    if current.name != "LPAREN":
        raise ParserError("Expected lparen is missing: " + current.line)
    current = EXPR_LIST(next(G), G)
    if current.name != "RPAREN":
        raise ParserError("Expected rparen is missing: " + str(current.line_num) + current.pattern)
    return next(G)

@add_debug
def ASSIGNMENT(current, G):
    current = IDENT(current, G)
    if current.name != "ASSIGNOP":
        raise ParserError("Expected assignop is missing: " + current.line)
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
    current = IDENT(current, G)
    while True:
        if current.name == 'COMMA':
            current = next(G)
            current = IDENT(current, G)
        if current.name != 'COMMA':
            break
    return current

@add_debug
def EXPR_LIST(current, G):
    current = EXPRESSION(current, G)
    while True:
        if current.name == 'COMMA':
            current = next(G)
            current = EXPRESSION(current, G)
        if current.name != 'COMMA':
            break;
    return current

@add_debug
def EXPRESSION(current, G):
    current = PRIMARY(current, G)

    while True:
        if (current.name == 'PLUS') | (current.name == 'MINUS'): #May have to add ARITHOP in future
            current = next(G)
            current = PRIMARY(current, G)
        if (current.name != 'PLUS') & (current.name != 'MINUS'):
            return current
    # while True:
    #     if ARITHOP(current, G).name != 'PLUS' or 'MINUS': # ????
    #         break
    #     current = PRIMARY(next(G), G)
    # return current

@add_debug
def PRIMARY(current, G):
    if current.name == 'INTLIT':
        return next(G)
    if current.name == 'LPAREN':
        current = EXPRESSION(next(G), G)
        if current.name != 'RPAREN':
            raise ParserError("Expected rparen is missing: " + current.line)
        return next(G)
    current = IDENT(current, G)
    return current

@add_debug
def IDENT(current, G):
    if current.name != 'ID':
        raise ParserError("Error when parsing IDENT: " + current.line)
    return next(G)

# @add_debug
# def ARITHOP(current, G):
#     pass

if __name__ == "__main__":
    print(parser('sample1.txt', 'tokens.txt'))
