import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from listener import Listener, CErrorListener
from ast import *
from llvm import LLVMGenerator
import filecmp

def main(argv):
    input_stream = FileStream(argv[2]) 
    lexer = GrammarLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = GrammarParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CErrorListener())
    tree = parser.startRule()
    listener = Listener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)  
    astcreator = ASTCreator(tree, listener.queue)
    ast = astcreator.generateTree()
    llvmgenerator = LLVMGenerator(ast)
    llvmgenerator.toLLVM(argv[3])
    result = filecmp.cmp(argv[3], argv[4], shallow = False)

    if result:
        print("Test " + argv[1] + " passed.")
    else:
        print("Test " + argv[1] + " failed.")

if __name__ == '__main__':
    main(sys.argv)