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
	print("hey")
	"""
	source_file: A program written in the ML langauge.
	returns True if the code is syntactically correct.
	Throws a ParserError otherwise.
	"""
	G = lexer(source_file, token_file)
	current = PROGRAM(next(G), G)
	if current.name is '$':
		return True
	else:
		return False
	
@add_debug	
def PROGRAM(current, G):
	print(current.pattern)
	if current.name == "BEGIN":
		current = STATEMENT_LIST(next(G), G)
		if current.name == "END":
			return '$'
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
	
if __name__ == "__main__":
    print(parser('test.txt', 'tokens.txt'))
	

