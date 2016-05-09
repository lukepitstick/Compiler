"""
Compiler Design Group 7
Kwangju Kim
Julius Ware
Chris Dieter
Luke Pitstick
"""

import sys
import argparse
import tree
import lexer_sol
import MLparser
import codegenerator2
import traceback

def compiler(source, tokens, output):
    mlp = MLparser.parser(source, tokens)

    if output == 'TEST':
        print(mlp)
        return True

    MIPScodes = []
    try:
        MIPScodes = codegenerator2.findGenerateMIPSCode(mlp[0], mlp[1], mlp[2])
    except MLparser.ParserError:
        traceback.print_exc()
        return False
    except codegenerator.CompilerError:
        traceback.print_exc()
        return False

    try:
        outFile = open(output, 'w')
        for line in MIPScodes:
            outFile.write(line)
    except Exception:
        traceback.print_exc()
        return False
    return True

 
if __name__ == "__main__":  # Only true if program invoked from the command line

    # Use the argparse library to parse the commandline arguments
    parser = argparse.ArgumentParser(description = "Group7 micro-language compiler")
    parser.add_argument('-t', type = str, dest = 'token_file',
                       help = "Token file", default = 'tokens.txt')
    parser.add_argument('source_file', type = str,
                        help = "Source-code file")
    parser.add_argument('output_file', type = str, 
                        help = 'output file name')
    
    args = parser.parse_args()

    # Call the compiler function

    compiler(args.source_file, args.token_file, args.output_file)
