import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from src.listener import Listener, CErrorListener
from src.AST.ASTCreator import ASTCreator
from src.llvm import LLVM

def main(argv):
    input_stream = FileStream(argv[1])
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
    ast.dot("treeGraph")

    llvmgenerator = LLVM(ast)
    llvmgenerator.toLLVM('llvm.ll')

if __name__ == '__main__':
    main(sys.argv)
