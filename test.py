import sys
from antlr4 import *
from GrammarLexer import GrammarLexer
from GrammarParser import GrammarParser
from src.listener import Listener, CErrorListener
from src.AST.ASTCreator import ASTCreator
from src.llvm import LLVM
from src.mips import MIPS
import filecmp

def main(argv):
    input_stream = FileStream(argv[3]) 
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

    if argv[1] in ['llvm', 'LLVM']:
        llvmgenerator = LLVM(ast)
        llvmgenerator.toLLVM(argv[4])
        result = filecmp.cmp(argv[4], argv[5], shallow = False)

        if result:
            print("LLVM Test " + argv[2] + " passed.")
        else:
            print("LLVM Test " + argv[2] + " failed.")
            
    elif argv[1] in ['mips', 'MIPS']:
        mipsgenerator = MIPS(ast)
        mipsgenerator.toMIPS(argv[4])
        result = filecmp.cmp(argv[4], argv[5], shallow = False)

        if result:
            print("MIPS Test " + argv[2] + " passed.")
        else:
            print("MIPS Test " + argv[2] + " failed.")

if __name__ == '__main__':
    main(sys.argv)