# Compiler Design Group 7
# Luke Pitstick
# Christopher Dieter
# Kwangju Kim
# Julius Ware

import sys
import argparse
from lexer_sol import lexer
from tree import tree
from traceback import print_exc
from codegenerator import CompilerError

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
dict_ = {} #instantiate symbol table
strDict = {}
funcDict = {}
# the new dictionary of dictionaries for scope. The key is the scope_variate, 
# the value is a another dictionary containing variable name as key and tuple 
# as value
varScopeDict = {}
counter = 0
typeOfVar = ""
valOfVar = ""
varName1 = ""
# keeps track of the scope
scope_variate = None

def parser(source_file, token_file):	
    """
    source_file: A program written in the ML langauge.
    returns True if the code is syntactically correct.
    Throws a ParserError otherwise.
    """
    global typeOfVar
    global valOfVar
    global varName1
    global strDict
    global funcDict
    global varScopeDict
    global counter
    global dict_
    global scope_variate
    
    typeOfVar = ""
    valOfVar = ""
    varName1 = ""    
    
    dict_.clear() #clear dict
    strDict.clear()
    funcDict.clear()
    varScopeDict.clear()
    count = 0
    scope_variate = None
    
    G = lexer(source_file, token_file)

    t = None # this should be changed to the tree

    try:
        t, current = CLASS(next(G), G)
    except StopIteration:
        raise ParserError("Syntax Error: File finished before end")

    if current.name != '$':
        raise ParserError("Syntax Error: File did not end after 'end'")

    retdict = dict_
    retdict2 = {}
    retdict2["dict"] = dict_
    retdict2["strDict"] = strDict
    retdict2["funcDict"] = funcDict
    retdict2["varScopeDict"] = varScopeDict
    #print(retdict)
    return t, retdict, retdict2 #return tree and symbol table

@add_debug
def CLASS(current, G):
    global scope_variate
    t = tree("CLASS")
    if current.name == "GLOBAL":
        t1, current = GLOBAL(current, G)
        t.append(t1)
    if current.name == "FUNCTION":
        t2, current = FUNCTIONLST(current, G)
        t.append(t2)
    if current.name == "BEGIN":
        scope_variate = "MAIN"
        t3, current = PROGRAM(current, G)
        t.append(t3)
    """
    for x in varScopeDict:
        print(x)
        print(varScopeDict[x])
    """
    return t, current

@add_debug
def GLOBAL(current, G):
    global scope_variate
    scope_variate = "GLOBAL"
    while(True):
        t = tree("GLOBAL")
        holder = False
        t1, current, holder = STATEMENT(next(G), G)
        t.append(t1)
        if current.name != "SEMICOLON":
            raise ParserError("must end with semi-colon")
        current = next(G)
        if current.name != "GLOBAL":
            return t, current
    return t, current

@add_debug
def FUNCTIONLST(current, G):
    global scope_variate
    t = tree("FUNCTION")
    while(True):
        if current.name != "FUNCTION":
            break
        type = next(G)
        t.append(tree(type.name))
        name = next(G)
        t.append(tree(name.name))
        funcDict[name.pattern] = type.name
        scope_variate = name.pattern
        current = next(G)
        if current.name == "LPAREN":
            holder = False
            current = next(G)
            while(True):
                if current.name == "RPAREN":
                    break
                if current.name == "COMMA":
                    current = next(G)
                t1, current, holder = STATEMENT(current, G)
                t.append(t1)
        current = next(G)
        tt, current = PROGRAM(current, G)
        t.append(tt)
    return t, current

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
        raise ParserError("Syntax Error: No 'end' at line: " + current.line)
    raise ParserError("Syntax Error: No 'begin' at line: " + current.line)

@add_debug
def STATEMENT_LIST(current, G):
    t = tree("STATEMENT_LIST")
    skipSemi2 = False
    t1, current, skipSemi2 = STATEMENT(current, G)
    t.append(t1)
    while True:
        if (current.name == 'SEMICOLON') | skipSemi2:
            # t.append(tree('SEMICOLON'))
            if (current.name == 'SEMICOLON'):
                SEMICOLON(current, G)
                current = next(G)
            if current.name == "END":
                return t, current
            skipSemi2 = False
            t2, current, skipSemi2 = STATEMENT(current, G)
            # print(str(t2))
            # print(current.name + " " + str(skipSemi2))
            if current.name == "END":
                t.append(t2)
                return t, current
            t.append(t2)
        else:
            raise ParserError("Syntax Error: no semicolon at line: " + current.line + " at " + str(current.line_num))
    return t, current

@add_debug
def SEMICOLON(current, G):
    pass

@add_debug
def STATEMENT(current, G):
    skipSemi = False
    t = tree("STATEMENT")
    global typeOfVar
    global varName1
    if current.name == "IF":
        t.append(tree("IF"))
        var1 = next(G)
        # ty = str(dict_[var1.pattern][1])
        # print(var1.pattern) #can be an expression, check for bool in compiler
        # if var1.name != "ID":
        #     raise SyntaxError("must be an ID")
        # if ty != "BOOL":
        #     raise SyntaxError("must be a bool")
        t0, current = EXPRESSION(var1, G)
        t.append(t0)
        thn = current
        if thn.name != "THEN":
            raise ParserError("must be followed by then")
        current = next(G)
        t1, current = PROGRAM(current, G)
        t.append(t1)
        if current.name == "ELSE":
            t.append(tree("ELSE"))
            current = next(G)
            t2, current = PROGRAM(current, G)
            t.append(t2)
            if current.name == "END": #else begin {code} end end ... handles if two ends follow each other
                return t, current, skipSemi
        # print("lalal" + current.name)
        # print(str(t))
        skipSemi = True
    elif current.pattern in funcDict.keys():
        tmp = tree("FUNCCALL")
        paren = next(G)
        current = next(G)
        if current.name == "RPAREN":
            pass
        else:
            while (True):

                if current.name == "RPAREN":
                    break
                if current.name == "COMMA":
                    current = next(G)
                t1, current = EXPRESSION(current, G)
                t.append(t1)
        current = next(G)
        t.append(tmp)
    elif current.name == "WHILE":
        t.append(tree("WHILE"))
        current = next(G)
        t1, current = EXPRESSION(current, G)
        t.append(t1)
        t2, current = PROGRAM(current, G)
        # print(t2.label)
        t.append(t2)
        skipSemi = True
    elif current.name == "RETURN":
        t.append(tree("RETURN"))
        current = next(G)
        if current.name == "REFERENCE":
            current = next(G)
            current.pattern = "ref-" + current.pattern
        if current.name == "INTLIT":
            t1, current = PRIMARY(current, G)
            t.append(t1)
        elif current.name == "STRING":
            t1, current = PRIMARY(current, G)
            t.append(t1)
        elif current.name == "BOOLLIT":
            t1, current = PRIMARY(current, G)
            t.append(t1)
        else:
            t1, current = EXPRESSION(current, G)
            print(current)
            t.append(t1)
    elif current.name == "INTTYPE":
        typeOfVar = "INT"
        t.append(tree("INTTYPE"))
        current = next(G)
        varName1 = current.pattern
        try:
            isthereatype = str(dict_[current.pattern][1])
            #checks to see if there is the current variable has already been declared in the current scope!
            hmm = str(varScopeDict[scope_variate][current.pattern][1])
            varInScope = str(varScopeDict[scope_variate])
            raise ParserError("Semantic error: type declared twice on a variable. "\
                              + current.line)
        except KeyError:
            pass
        t1, current = IDENT(current, G)
        t.append(t1)
    elif current.name == "BOOLTYPE":
        typeOfVar = "BOOL"
        t.append(tree("BOOLTYPE"))
        current = next(G)
        varName1 = current.pattern
        try:
            isthereatype = str(dict_[current.pattern][1])
            hmm = str(varScopeDict[scope_variate][current.pattern][1])
            varInScope = str(varScopeDict[scope_variate])
            raise CompilerError("Semantic error: type declared twice on a variable. "\
                              + current.line)
        except KeyError:
            pass
        t1, current = IDENT(current, G)
        t.append(t1)
    elif current.name == "STRINGTYPE":
        typeOfVar = "STRING"
        t.append(tree("STRINGTYPE"))
        current = next(G)
        varName1 = current.pattern
        try:
            isthereatype = str(dict_[current.pattern][1])
            hmm = str(varScopeDict[scope_variate][current.pattern][1])
            varInScope = str(varScopeDict[scope_variate])
            raise CompilerError("Semantic error: type declared twice on a variable. "\
                              + current.line)
        except KeyError:
            pass
        t1, current = IDENT(current, G)
        t.append(t1)
        t2, current = ASSIGNMENTSTR(current, G)
        t.append(t2)
    elif current.name == "READ":
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
    return t, current, skipSemi

@add_debug
def ASSIGNMENTSTR(current, G):
    t = tree("ASSIGNMENTSTR")
    if current.name != "ASSIGNOP":
        return t, current
    current = next(G)
    if current.name == "STRING":
        tstrlit = tree("STRING")
        tstrlit.val = current.pattern
        valOfVar = current.pattern
        tuple1 = (valOfVar, typeOfVar)
        dict_[varName1] = tuple1
        t.append(tstrlit)
        return t, next(G)

    tident2, current = IDENT(current, G)
    t.append(tident2)
    return t, current
    

@add_debug
def READ(current, G):
    if current.name != "LPAREN":
        raise ParserError("Syntax Error: Expected lparen is missing: " +\
                          current.line)
    # t.append(tree("LPAREN"))
    t, current = ID_LIST(next(G), G)
    if current.name != "RPAREN":
        raise ParserError("Syntax Error: Expected rparen is missing: " +\
                          current.line)
    # t.append(tree("RPAREN"))
    return t, next(G)

@add_debug
def WRITE(current, G):
    if current.name != "LPAREN":
        raise ParserError("Syntax Error: Expected lparen is missing: " +\
                          current.line)
    # t.append(tree("LPAREN"))
    current = next(G)
    t, current = EXPR_LIST(current, G)
    if current.name != "RPAREN":
        raise ParserError("Syntax Error: Expected rparen is missing: " + \
                          str(current.line_num) + current.pattern)
    # t.append(tree("RPAREN"))
    return t, next(G)

@add_debug
def ASSIGNMENT(current, G):
    t = tree("ASSIGNMENT")
    tident, current = IDENT(current, G)
    t.append(tident)
    if current.name != "ASSIGNOP":
        raise ParserError("Syntax Error: Expected assignop is missing: " + current.line)
    # t.append(tree("ASSIGNOP"))
    texpr, current = EXPRESSION(next(G), G)
    t.append(texpr)
    return t, current

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
            break
    return t, current

@add_debug
def EXPRESSION(current, G):
    t = tree("EXPRESSION")
    t1, current = TERM1(current, G)
    t.append(t1)

    while True:
        if (current.name == 'OR'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = TERM1(current, G)
            t.append(t2)
        if (current.name != 'OR'):
            return t, current

def TERM1(current, G):
    t = tree("TERM1")
    t1, current = FACT1(current, G)
    t.append(t1)

    while True:
        if (current.name == 'AND'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = FACT1(current, G)
            t.append(t2)
        if (current.name != 'AND'):
            return t, current

def FACT1(current, G):
    t = tree("FACT1")
    t1, current = EXP2(current, G)
    t.append(t1)
    t2, current = R(current, G)
    t.append(t2)
    return t, current

@add_debug
def R(current, G):
    t = tree("R")
    if(current.name == 'GREATEREQUAL') | (current.name == 'LESSEQUAL') |\
      (current.name == 'EQUAL') | (current.name == 'LESSTHAN') | \
      (current.name == 'GREATERTHAN') | (current.name == 'NOTEQUAL'):
        t.append(tree(current.name))
        current = next(G)
        t2, current = EXP2(current, G)
        t.append(t2)
        return t, current
    else:
        return t, current

@add_debug
def EXP2(current, G):
    t = tree("EXP2")
    t1, current = TERM2(current, G)
    t.append(t1)

    while True:
        if (current.name == 'PLUS'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = TERM2(current, G)
            t.append(t2)
        if (current.name != 'PLUS'):
            return t, current

@add_debug
def TERM2(current, G):
    t = tree("TERM2")
    t1, current = TERM3(current, G)
    t.append(t1)

    while True:
        if (current.name == 'MINUS'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = TERM3(current, G)
            t.append(t2)
        if (current.name != 'MINUS'):
            return t, current

@add_debug
def TERM3(current, G):
    t = tree("TERM3")
    t1, current = FACT2(current, G)
    t.append(t1)

    while True:
        if (current.name == 'MULTIPLICATION'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = FACT2(current, G)
            t.append(t2)
        if (current.name != 'MULTIPLICATION'):
            return t, current

@add_debug
def FACT2(current, G):
    t = tree("FACT2")
    t1, current = FACT3(current, G)
    t.append(t1)

    while True:
        if (current.name == 'DIVISION'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = FACT3(current, G)
            t.append(t2)
        if (current.name != 'DIVISION'):
            return t, current

@add_debug
def FACT3(current, G):
    t = tree("FACT3")
    t1, current = PRIMARY(current, G)
    t.append(t1)

    while True:
        if (current.name == 'REMAINDER'): #May have to add ARITHOP in future
            t.append(tree(current.name))
            current = next(G)
            t2, current = PRIMARY(current, G)
            t.append(t2)
        if (current.name != 'REMAINDER'):
            return t, current

@add_debug
def PRIMARY(current, G):
    global counter
    t = tree('PRIMARY')
    if current.pattern in funcDict.keys():
        tmp = tree("FUNCCALL")
        paren = next(G)
        current = next(G)
        if current.name == "RPAREN":
            pass
        else:
            t1, current = ID_LIST(current, G)
            if current.name != "RPAREN":
                raise ParserError("not matching parens")
            tmp.append(t1)
            t.append(tmp)
        return t, next(G)
    if current.name == 'INTLIT':
        tmp = tree('INTLIT')
        tmp.val = current.pattern
        tuple1 = ("False", typeOfVar)
        dict_[varName1] = tuple1 #do we need this?
        t.append(tmp)
        return t, next(G)
    if current.name == 'BOOLLIT':
        tmp = tree('BOOLLIT')
        tmp.val = current.pattern
        tuple1 = ("False", typeOfVar)
        dict_[varName1] = tuple1 #do we need this?
        t.append(tmp)
        return t, next(G)
    if current.name == 'LPAREN':
        t1, current = EXPRESSION(next(G), G)
        if current.name != 'RPAREN':
            raise ParserError("Syntax Error: Expected rparen is missing: " \
                              + current.line)
        t.append(t1)
        return t, next(G)
    if current.name == "STRING": #unsure
        tstrlit = tree("STRING")
        tstrlit.val = current.pattern
        t.append(tstrlit)
        # valOfVar = current.pattern
        tuple1 = (current.pattern, "STRING")
        tname = "lit%i" % counter
        strDict[tname] = tuple1
        counter = counter + 1
        ct = next(G)
        return t, ct
    t2, current = IDENT(current, G)
    t.append(t2)
    return t, current

@add_debug
def IDENT(current, G,):
    global varName1
    t = tree('IDENT')
    if current.name == "REFERENCE":
        current = next(G)
        current.pattern = "ref-" + current.pattern
    if current.name != 'ID':
        raise ParserError("Syntax Error: Error when parsing IDENT: " \
                          + current.line)
    tmp = tree('ID')
    tmp.val = current.pattern
    t.append(tmp)
    g = ""
    try:
        g = dict_[current.pattern][0]
    except:
        pass
    gt = typeOfVar
    try:
        gt = dict_[current.pattern][1]
    except:
        pass
    dict_[current.pattern] = (g, gt) #add symbol to symbol table, will use different values later.
    varScopeDict[scope_variate] = {current.pattern:(g, gt)}
    return t, next(G)

if __name__ == "__main__":
    global dict_
    global strDict
    global funcDict
    global varScopeDict
    
    for i in range(1,9):
        try:
            fname = 'mltestcodes/test%d.ml' % i
            print("Parsing " + fname)
            try:
                sampt, tokk, tokk2 = parser(fname, 'tokens.txt')
                print('The source file is following a valid syntax.')
                print("\n" + repr(sampt))
                print('=======================================================')
                assert(tokk2["dict"] == dict_)
                print("\nSymbol Table:\n" + str(tokk2["dict"]))
                assert(tokk2["strDict"] == strDict)
                print("\nString Table:\n" + str(strDict))
                assert(tokk2["funcDict"] == funcDict)
                print("\nFunction Table:\n" + str(funcDict))
                assert(tokk2["varScopeDict"] == varScopeDict)
                print("\nVariable Scope Table:\n" + str(varScopeDict))
                print('=======================================================')
                print("\nThe list of child:")
                sampt.getChildLabel()
            except ParserError:
                print_exc()
                print('The source file is not following a valid syntax.')
        except ImportError:
            print('The sample file does not exist.')
        finally:
            print('======================================================')
            end = input('Press <ENTER> to continue... (or QUIT to exit)')
            if end == 'QUIT':
                break
    print('Personal tester is over.')
