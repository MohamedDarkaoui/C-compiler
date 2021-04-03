# Generated from Grammar.g4 by ANTLR 4.9.1
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener
import sys
#sys.tracebacklimit = 0



from GrammarListener import *

class Listener(GrammarListener):
    def __init__(self):
        self.queue = []
    # Enter a parse tree produced by GrammarParser#startRule.
    def enterStartRule(self, ctx):
        self.queue.append("PROG")

    # Enter a parse tree produced by GrammarParser#signed_int.
    def enterSigned_int(self, ctx):
        self.queue.append("INT")

    # Enter a parse tree produced by GrammarParser#float_number.
    def enterFloat_number(self, ctx):
        self.queue.append("FLOAT")
        

    # Enter a parse tree produced by GrammarParser#statement.
    def enterStatement(self, ctx):
        self.queue.append("STATEMENT")
        

    # Enter a parse tree produced by GrammarParser#declaration.
    def enterDeclaration(self, ctx):
        self.queue.append("DEC")

    # Enter a parse tree produced by GrammarParser#definition.
    def enterDefinition(self, ctx):
        self.queue.append("DEF")

    # Enter a parse tree produced by GrammarParser#assignment.
    def enterAssignment(self, ctx):
        self.queue.append("ASSIGN")

    # Enter a parse tree produced by GrammarParser#expression.
    def enterExpression(self, ctx):
        self.queue.append("EXP")

    # Enter a parse tree produced by GrammarParser#arithmetic_expression.
    def enterArithmetic_expression(self, ctx):
        self.queue.append("A_EXP")
    
    # Enter a parse tree produced by GrammarParser#types.
    def enterTypes(self, ctx):
        self.queue.append("TYPE")

    # Enter a parse tree produced by GrammarParser#variable.
    def enterVariable(self, ctx):
        self.queue.append("VAR")
    
    # Enter a parse tree produced by GrammarParser#character.
    def enterCharacter(self, ctx):
        self.queue.append("CHAR")

    #------- 03/04/2021
    # Enter a parse tree produced by GrammarParser#condition.
    def enterCondition(self, ctx):
        self.queue.append("CONDITION")

    # Enter a parse tree produced by GrammarParser#comparison_expression.
    def enterComparison_expression(self, ctx):
        self.queue.append("COMPARISON")
    
    # Enter a parse tree produced by GrammarParser#block.
    def enterBlock(self, ctx):
        self.queue.append("BLOCK")

    # Enter a parse tree produced by GrammarParser#selection_sequence.
    def enterSelection_sequence(self, ctx):
        self.queue.append("SELECT")

    # Enter a parse tree produced by GrammarParser#else_statement.
    def enterElse_statement(self, ctx):
        self.queue.append("ELSE")
        
    # Enter a parse tree produced by GrammarParser#else_if_statement.
    def enterElse_if_statement(self, ctx):
        self.queue.append("ELSE IF")
    
        # Enter a parse tree produced by GrammarParser#if_statement.
    def enterIf_statement(self, ctx):
        self.queue.append("IF")
    
    # Enter a parse tree produced by GrammarParser#while_statement.
    def enterWhile_statement(self, ctx):
        self.queue.append("WHILE")

        

class CErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, err, e):
        raise Exception("[Syntax Error] Line {} Position {}: {}".format(line, column, err))