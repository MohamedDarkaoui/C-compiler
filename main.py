import sys
from antlr4 import *
from mathematicalGrammarLexer import mathematicalGrammarLexer
from mathematicalGrammarParser import mathematicalGrammarParser
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = mathematicalGrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = mathematicalGrammarParser(stream)
    tree = parser.startRule()
 
if __name__ == '__main__':
    main(sys.argv)
