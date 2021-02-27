# Generated from mathematicalGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mathematicalGrammarParser import mathematicalGrammarParser
else:
    from mathematicalGrammarParser import mathematicalGrammarParser

# This class defines a complete generic visitor for a parse tree produced by mathematicalGrammarParser.

class mathematicalGrammarVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mathematicalGrammarParser#startRule.
    def visitStartRule(self, ctx:mathematicalGrammarParser.StartRuleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematicalGrammarParser#expression.
    def visitExpression(self, ctx:mathematicalGrammarParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematicalGrammarParser#arithmetic_expression.
    def visitArithmetic_expression(self, ctx:mathematicalGrammarParser.Arithmetic_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematicalGrammarParser#conditional_expression.
    def visitConditional_expression(self, ctx:mathematicalGrammarParser.Conditional_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mathematicalGrammarParser#logical_expression.
    def visitLogical_expression(self, ctx:mathematicalGrammarParser.Logical_expressionContext):
        return self.visitChildren(ctx)



del mathematicalGrammarParser