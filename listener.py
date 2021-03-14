# Generated from Grammar.g4 by ANTLR 4.9.1
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import sys
sys.tracebacklimit = 0



from GrammarListener import *

class Listener(GrammarListener):
    def __init__(self):
        self.queue = []
    # Enter a parse tree produced by GrammarParser#startRule.
    def enterStartRule(self, ctx):
        self.queue.append(("PROG", ctx))

    # Exit a parse tree produced by GrammarParser#startRule.
    def exitStartRule(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#signed_int.
    def enterSigned_int(self, ctx):
        self.queue.append(("INT", ctx))
        

    # Exit a parse tree produced by GrammarParser#signed_int.
    def exitSigned_int(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#float_number.
    def enterFloat_number(self, ctx):
        self.queue.append(("FLOAT", ctx))
        

    # Exit a parse tree produced by GrammarParser#float_number.
    def exitFloat_number(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx):
        self.queue.append(("STATEMENT", ctx))
        

    # Exit a parse tree produced by GrammarParser#statement.
    def exitStatement(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#declaration.
    def enterDeclaration(self, ctx):
        self.queue.append(("DEC", ctx))

    # Exit a parse tree produced by GrammarParser#declaration.
    def exitDeclaration(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#definition.
    def enterDefinition(self, ctx):
        self.queue.append(("DEF", ctx))

    # Exit a parse tree produced by GrammarParser#definition.
    def exitDefinition(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#assignment.
    def enterAssignment(self, ctx):
        self.queue.append(("ASSIGN", ctx))
        pass

    # Exit a parse tree produced by GrammarParser#assignment.
    def exitAssignment(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx):
        self.queue.append(("EXP", ctx))
        

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx):
        self.queue.append(("A_EXP", ctx))


    # Exit a parse tree produced by GrammarParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx):
        pass
    
    # Enter a parse tree produced by GrammarParser#types.
    def enterTypes(self, ctx):
        self.queue.append(("TYPE", ctx))


    # Exit a parse tree produced by GrammarParser#types.
    def exitTypes(self, ctx):
        pass

    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx):
        self.queue.append(("VAR", ctx))

    # Exit a parse tree produced by GrammarParser#variable.
    def exitVariable(self, ctx):
        pass
    
    # Enter a parse tree produced by GrammarParser#character.
    def enterCharacter(self, ctx):
        self.queue.append(("CHAR", ctx))

    # Exit a parse tree produced by GrammarParser#character.
    def exitCharacter(self, ctx):
        pass


class CErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, err, e):
        raise Exception("[Syntax Error] Line {} Position {}: {}".format(line, column, err))