import re
import sys

class LexerError(Exception):
    """
    Exception to be thrown when the lexer encounters a bad token.
    """
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return str(self.msg)

class Token:
    """
    A class for storing token information.
    The variable instances for a token object are:
    * t_class: The token class.
    * name: The name of the token.
    * pattern: The specific pattern of the token
    * line: The line containing the token
    * line_num: The line number (numbered from 1)
    * col: The column number (numbered from 0)
    """

    def __init__(self, t_class, name, pattern, line, line_num, col):
        """
        Constructor
        """
        self.t_class = t_class
        self.name = name
        self.pattern = pattern
        self.line = line
        self.line_num = int(line_num)
        self.col = int(col)

    def __str__(self):
        """
        Defines behavior of the str function on the Token class.
        Prints as a tupple all information except self.line.
        """
        return str((self.t_class, self.name, self.pattern, self.line_num, self.col))

    def __repr__(self):
        """
        Defines the behaviour of the repr() function
        on the Token class.
        """
        return "Token: " + str(self)

    def __eq__(self, other):
        """
        Defines behaviour of the == operator on the Token class
        """
        return self.t_class == other.t_class and self.name == other.name and \
               self.pattern == other.pattern and self.line == other.line and \
               self.line_num == other.line_num and self.col == other.col
               

def lexer(source_file, token_file):
                   
    token_hash = {}
    re_list = []

    fp = open(token_file)
    for line in open(token_file):
        A = re.split("\s+", line.rstrip())
        re_list.append(A[2])
        token_hash[A[2]] = (A[0], A[1])
    fp.close()


    def search_list():
        for key in re_list:
            r = re.match(key, line[col:])
            if r:
                return key, r
        return None, None
        
    with open(source_file) as fp:
        line = fp.readline()
        line_num = 1

        while line:
            col = 0;
            line = line.rstrip()
            while line[col:].rstrip():
                r = re.match("\s+", line[col:])
                if r:
                    col += len(r.group(0))

                if line[col] == '#':
                    break
                    
                key, r = search_list()
                if key:
                    yield Token(token_hash[key][0], token_hash[key][1], r.group(1), line, line_num, col)
                    col += len(r.group(1))
                else:
                    msg = "Bad token (line %d, column %d): %s" % (line_num, col, line[col:])
                    raise LexerError(msg)

            line = fp.readline()
            line_num += 1;

    

