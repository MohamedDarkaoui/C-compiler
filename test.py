import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from src.listener import Listener, CErrorListener
from src.AST.ASTCreator import ASTCreator
from src.llvm import LLVM
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
    ast = astcreator.generateAST()
    llvmgenerator = LLVM(ast)
    llvmgenerator.toLLVM(argv[3])
    result = filecmp.cmp(argv[3], argv[4], shallow = False)

    if result:
        print("Test " + argv[1] + " passed.")
    else:
        print("Test " + argv[1] + " failed.")

if __name__ == '__main__':
    main(sys.argv)