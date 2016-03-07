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

def compiler(source, tokens, output):
    mlp = MLparser.parser(source, tokens)
    outf = open(output, 'w')
    outf.write(repr(mlp[0]))
    outf.write('\n')
    outf.write(repr(mlp[1]))
    outf.close()

 
if __name__ == "__main__":  # Only true if program invoked from the command line

    # Use the argparse library to parse the commandline arguments
    parser = argparse.ArgumentParser(description = "Group7 micro-language compiler")
    parser.add_argument('-t', type = str, dest = 'token_file',
                       help = "Token file", default = 'tokens.txt')
    parser.add_argument('source_file', type = str,
                        help = "Source-code file", default = 'tokens.txt')
    parser.add_argument('output_file', type = str, 
                        help = 'output file name')
    
    args = parser.parse_args()

    # Call the compiler function
    compiler(args.source_file, args.token_file, args.output_file)
