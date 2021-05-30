import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from src.listener import Listener, CErrorListener
from src.AST.ASTCreator import ASTCreator
from src.llvm import LLVM
from src.mips import MIPS

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
    ast.dot("treeGraph")

    if argv[1] in ['llvm', 'LLVM']:
        llvmgenerator = LLVM(ast)
        llvmgenerator.toLLVM(argv[3])

    elif argv[1] in ['mips', 'MIPS']:
        mipsgenerator = MIPS(ast)
        mipsgenerator.toMIPS(argv[3])

if __name__ == '__main__':
    main(sys.argv)
