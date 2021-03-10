# Generated from Grammar.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .GrammarParser import GrammarParser
else:
    from GrammarParser import GrammarParser


from GrammarListener import *

class Listener(GrammarListener):
 
    # Enter a parse tree produced by GrammarParser#startRule.
    def enterStartRule(self, ctx:GrammarParser.StartRuleContext):
        print(ctx.getText())
        print("startrule")

    # Exit a parse tree produced by GrammarParser#startRule.
    def exitStartRule(self, ctx:GrammarParser.StartRuleContext):
        pass


    # Enter a parse tree produced by GrammarParser#signed_int.
    def enterSigned_int(self, ctx:GrammarParser.Signed_intContext):
        print(ctx.getText())
        print("signed int")

    # Exit a parse tree produced by GrammarParser#signed_int.
    def exitSigned_int(self, ctx:GrammarParser.Signed_intContext):
        pass


    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx:GrammarParser.ExpressionContext):
        print(ctx.getText())
        print("expression")

    # Exit a parse tree produced by GrammarParser#expression.
    def exitExpression(self, ctx:GrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:GrammarParser.Arithmetic_expressionContext):
        print(ctx.getText())
        print("arithmetic")

    # Exit a parse tree produced by GrammarParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:GrammarParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#conditional_expression.
    def enterConditional_expression(self, ctx:GrammarParser.Conditional_expressionContext):
        print(ctx.getText())

    # Exit a parse tree produced by GrammarParser#conditional_expression.
    def exitConditional_expression(self, ctx:GrammarParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by GrammarParser#logical_expression.
    def enterLogical_expression(self, ctx:GrammarParser.Logical_expressionContext):
        print(ctx.getText())

    # Exit a parse tree produced by GrammarParser#logical_expression.
    def exitLogical_expression(self, ctx:GrammarParser.Logical_expressionContext):
        pass

