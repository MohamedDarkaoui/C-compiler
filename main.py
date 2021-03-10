import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from listener import Listener
from cst import cst
 
def main(argv):
    input_stream = FileStream(argv[1])
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    tree = parser.startRule()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    #c = cst(tree)
    #print(c.dot())


if __name__ == '__main__':
    main(sys.argv)
