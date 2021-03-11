# Generated from Grammar.g4 by ANTLR 4.9.1
from antlr4 import *



if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser


from GrammarListener import *

class Listener(GrammarListener):
    def __init__(self):
        self.queue = []
    # Enter a parse tree produced by GrammarParser#startRule.
    def enterStartRule(self, ctx):
        self.queue.append(("startRule", ctx))

    # Exit a parse tree produced by GrammarParser#startRule.
    def exitStartRule(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#signed_int.
    def enterSigned_int(self, ctx):
        self.queue.append(("signed_int", ctx))

    # Exit a parse tree produced by GrammarParser#signed_int.
    def exitSigned_int(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx):
        self.queue.append(("expression", ctx))



    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx):
        self.queue.append(("arithmetic_expression", ctx))

    # Exit a parse tree produced by GrammarParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#conditional_expression.
    def enterConditional_expression(self, ctx):
        self.queue.append(("conditional_expression", ctx))


    # Exit a parse tree produced by GrammarParser#conditional_expression.
    def exitConditional_expression(self, ctx):
        pass


    # Enter a parse tree produced by GrammarParser#logical_expression.
    def enterLogical_expression(self, ctx):
        self.queue.append(("logical_expression", ctx))

    # Exit a parse tree produced by GrammarParser#logical_expression.
    def exitLogical_expression(self, ctx):
        pass


