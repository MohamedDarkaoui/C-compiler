# Generated from mathematicalGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mathematicalGrammarParser import mathematicalGrammarParser
else:
    from mathematicalGrammarParser import mathematicalGrammarParser

# This class defines a complete listener for a parse tree produced by mathematicalGrammarParser.
class mathematicalGrammarListener(ParseTreeListener):

    # Enter a parse tree produced by mathematicalGrammarParser#startRule.
    def enterStartRule(self, ctx:mathematicalGrammarParser.StartRuleContext):
        pass

    # Exit a parse tree produced by mathematicalGrammarParser#startRule.
    def exitStartRule(self, ctx:mathematicalGrammarParser.StartRuleContext):
        pass


    # Enter a parse tree produced by mathematicalGrammarParser#expression.
    def enterExpression(self, ctx:mathematicalGrammarParser.ExpressionContext):
        pass

    # Exit a parse tree produced by mathematicalGrammarParser#expression.
    def exitExpression(self, ctx:mathematicalGrammarParser.ExpressionContext):
        pass


    # Enter a parse tree produced by mathematicalGrammarParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx:mathematicalGrammarParser.Arithmetic_expressionContext):
        pass

    # Exit a parse tree produced by mathematicalGrammarParser#arithmetic_expression.
    def exitArithmetic_expression(self, ctx:mathematicalGrammarParser.Arithmetic_expressionContext):
        pass


    # Enter a parse tree produced by mathematicalGrammarParser#conditional_expression.
    def enterConditional_expression(self, ctx:mathematicalGrammarParser.Conditional_expressionContext):
        pass

    # Exit a parse tree produced by mathematicalGrammarParser#conditional_expression.
    def exitConditional_expression(self, ctx:mathematicalGrammarParser.Conditional_expressionContext):
        pass


    # Enter a parse tree produced by mathematicalGrammarParser#logical_expression.
    def enterLogical_expression(self, ctx:mathematicalGrammarParser.Logical_expressionContext):
        pass

    # Exit a parse tree produced by mathematicalGrammarParser#logical_expression.
    def exitLogical_expression(self, ctx:mathematicalGrammarParser.Logical_expressionContext):
        pass



del mathematicalGrammarParser