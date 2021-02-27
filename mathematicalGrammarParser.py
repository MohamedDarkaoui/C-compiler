# Generated from mathematicalGrammar.g4 by ANTLR 4.9.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\25")
        buf.write("_\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\3\2\7\2\16\n")
        buf.write("\2\f\2\16\2\21\13\2\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\5\3\34\n\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4$\n\4\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4/\n\4\f\4\16\4\62\13\4")
        buf.write("\3\5\3\5\3\5\3\5\3\5\3\5\5\5:\n\5\3\5\3\5\3\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5E\n\5\f\5\16\5H\13\5\3\6\3\6\3\6\3")
        buf.write("\6\3\6\3\6\3\6\3\6\5\6R\n\6\3\6\3\6\3\6\3\6\3\6\3\6\7")
        buf.write("\6Z\n\6\f\6\16\6]\13\6\3\6\2\5\6\b\n\7\2\4\6\b\n\2\7\3")
        buf.write("\2\3\4\3\2\5\6\3\2\b\t\3\2\n\13\3\2\f\r\2h\2\17\3\2\2")
        buf.write("\2\4\33\3\2\2\2\6#\3\2\2\2\b9\3\2\2\2\nQ\3\2\2\2\f\16")
        buf.write("\5\4\3\2\r\f\3\2\2\2\16\21\3\2\2\2\17\r\3\2\2\2\17\20")
        buf.write("\3\2\2\2\20\3\3\2\2\2\21\17\3\2\2\2\22\23\5\6\4\2\23\24")
        buf.write("\7\23\2\2\24\34\3\2\2\2\25\26\5\b\5\2\26\27\7\23\2\2\27")
        buf.write("\34\3\2\2\2\30\31\5\n\6\2\31\32\7\23\2\2\32\34\3\2\2\2")
        buf.write("\33\22\3\2\2\2\33\25\3\2\2\2\33\30\3\2\2\2\34\5\3\2\2")
        buf.write("\2\35\36\b\4\1\2\36$\7\24\2\2\37 \7\21\2\2 !\5\6\4\2!")
        buf.write("\"\7\22\2\2\"$\3\2\2\2#\35\3\2\2\2#\37\3\2\2\2$\60\3\2")
        buf.write("\2\2%&\f\6\2\2&\'\t\2\2\2\'/\5\6\4\7()\f\5\2\2)*\t\3\2")
        buf.write("\2*/\5\6\4\6+,\f\4\2\2,-\7\7\2\2-/\5\6\4\5.%\3\2\2\2.")
        buf.write("(\3\2\2\2.+\3\2\2\2/\62\3\2\2\2\60.\3\2\2\2\60\61\3\2")
        buf.write("\2\2\61\7\3\2\2\2\62\60\3\2\2\2\63\64\b\5\1\2\64:\5\6")
        buf.write("\4\2\65\66\7\21\2\2\66\67\5\b\5\2\678\7\22\2\28:\3\2\2")
        buf.write("\29\63\3\2\2\29\65\3\2\2\2:F\3\2\2\2;<\f\6\2\2<=\t\4\2")
        buf.write("\2=E\5\b\5\7>?\f\5\2\2?@\t\5\2\2@E\5\b\5\6AB\f\4\2\2B")
        buf.write("C\t\6\2\2CE\5\b\5\5D;\3\2\2\2D>\3\2\2\2DA\3\2\2\2EH\3")
        buf.write("\2\2\2FD\3\2\2\2FG\3\2\2\2G\t\3\2\2\2HF\3\2\2\2IJ\b\6")
        buf.write("\1\2JR\5\b\5\2KL\7\20\2\2LR\5\n\6\4MN\7\21\2\2NO\5\n\6")
        buf.write("\2OP\7\22\2\2PR\3\2\2\2QI\3\2\2\2QK\3\2\2\2QM\3\2\2\2")
        buf.write("R[\3\2\2\2ST\f\6\2\2TU\7\16\2\2UZ\5\n\6\7VW\f\5\2\2WX")
        buf.write("\7\17\2\2XZ\5\n\6\6YS\3\2\2\2YV\3\2\2\2Z]\3\2\2\2[Y\3")
        buf.write("\2\2\2[\\\3\2\2\2\\\13\3\2\2\2][\3\2\2\2\r\17\33#.\60")
        buf.write("9DFQY[")
        return buf.getvalue()


class mathematicalGrammarParser ( Parser ):

    grammarFileName = "mathematicalGrammar.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", 
                     "'<'", "'>='", "'<='", "'=='", "'!='", "'||'", "'&&'", 
                     "'!'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>", "PLUS", "MINUS", "TIMES", "DIV", "MODULO", 
                      "GT", "ST", "GET", "SET", "EQ", "NEQ", "OR", "AND", 
                      "NOT", "LP", "RP", "SEMICOLON", "INT", "WS" ]

    RULE_startRule = 0
    RULE_expression = 1
    RULE_arithmetic_expression = 2
    RULE_conditional_expression = 3
    RULE_logical_expression = 4

    ruleNames =  [ "startRule", "expression", "arithmetic_expression", "conditional_expression", 
                   "logical_expression" ]

    EOF = Token.EOF
    PLUS=1
    MINUS=2
    TIMES=3
    DIV=4
    MODULO=5
    GT=6
    ST=7
    GET=8
    SET=9
    EQ=10
    NEQ=11
    OR=12
    AND=13
    NOT=14
    LP=15
    RP=16
    SEMICOLON=17
    INT=18
    WS=19

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartRuleContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematicalGrammarParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(mathematicalGrammarParser.ExpressionContext,i)


        def getRuleIndex(self):
            return mathematicalGrammarParser.RULE_startRule

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStartRule" ):
                listener.enterStartRule(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStartRule" ):
                listener.exitStartRule(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStartRule" ):
                return visitor.visitStartRule(self)
            else:
                return visitor.visitChildren(self)




    def startRule(self):

        localctx = mathematicalGrammarParser.StartRuleContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_startRule)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mathematicalGrammarParser.NOT) | (1 << mathematicalGrammarParser.LP) | (1 << mathematicalGrammarParser.INT))) != 0):
                self.state = 10
                self.expression()
                self.state = 15
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Arithmetic_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(mathematicalGrammarParser.SEMICOLON, 0)

        def conditional_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Conditional_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Logical_expressionContext,0)


        def getRuleIndex(self):
            return mathematicalGrammarParser.RULE_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpression" ):
                listener.enterExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpression" ):
                listener.exitExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpression" ):
                return visitor.visitExpression(self)
            else:
                return visitor.visitChildren(self)




    def expression(self):

        localctx = mathematicalGrammarParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expression)
        try:
            self.state = 25
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 16
                self.arithmetic_expression(0)
                self.state = 17
                self.match(mathematicalGrammarParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 19
                self.conditional_expression(0)
                self.state = 20
                self.match(mathematicalGrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 22
                self.logical_expression(0)
                self.state = 23
                self.match(mathematicalGrammarParser.SEMICOLON)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Arithmetic_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(mathematicalGrammarParser.INT, 0)

        def LP(self):
            return self.getToken(mathematicalGrammarParser.LP, 0)

        def arithmetic_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematicalGrammarParser.Arithmetic_expressionContext)
            else:
                return self.getTypedRuleContext(mathematicalGrammarParser.Arithmetic_expressionContext,i)


        def RP(self):
            return self.getToken(mathematicalGrammarParser.RP, 0)

        def PLUS(self):
            return self.getToken(mathematicalGrammarParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(mathematicalGrammarParser.MINUS, 0)

        def TIMES(self):
            return self.getToken(mathematicalGrammarParser.TIMES, 0)

        def DIV(self):
            return self.getToken(mathematicalGrammarParser.DIV, 0)

        def MODULO(self):
            return self.getToken(mathematicalGrammarParser.MODULO, 0)

        def getRuleIndex(self):
            return mathematicalGrammarParser.RULE_arithmetic_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArithmetic_expression" ):
                listener.enterArithmetic_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArithmetic_expression" ):
                listener.exitArithmetic_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArithmetic_expression" ):
                return visitor.visitArithmetic_expression(self)
            else:
                return visitor.visitChildren(self)



    def arithmetic_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_arithmetic_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathematicalGrammarParser.INT]:
                self.state = 28
                self.match(mathematicalGrammarParser.INT)
                pass
            elif token in [mathematicalGrammarParser.LP]:
                self.state = 29
                self.match(mathematicalGrammarParser.LP)
                self.state = 30
                self.arithmetic_expression(0)
                self.state = 31
                self.match(mathematicalGrammarParser.RP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 46
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 44
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 35
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 36
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.PLUS or _la==mathematicalGrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 37
                        self.arithmetic_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 38
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 39
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.TIMES or _la==mathematicalGrammarParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 40
                        self.arithmetic_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 41
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 42
                        self.match(mathematicalGrammarParser.MODULO)
                        self.state = 43
                        self.arithmetic_expression(3)
                        pass

             
                self.state = 48
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Conditional_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def arithmetic_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Arithmetic_expressionContext,0)


        def LP(self):
            return self.getToken(mathematicalGrammarParser.LP, 0)

        def conditional_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematicalGrammarParser.Conditional_expressionContext)
            else:
                return self.getTypedRuleContext(mathematicalGrammarParser.Conditional_expressionContext,i)


        def RP(self):
            return self.getToken(mathematicalGrammarParser.RP, 0)

        def GT(self):
            return self.getToken(mathematicalGrammarParser.GT, 0)

        def ST(self):
            return self.getToken(mathematicalGrammarParser.ST, 0)

        def GET(self):
            return self.getToken(mathematicalGrammarParser.GET, 0)

        def SET(self):
            return self.getToken(mathematicalGrammarParser.SET, 0)

        def EQ(self):
            return self.getToken(mathematicalGrammarParser.EQ, 0)

        def NEQ(self):
            return self.getToken(mathematicalGrammarParser.NEQ, 0)

        def getRuleIndex(self):
            return mathematicalGrammarParser.RULE_conditional_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConditional_expression" ):
                listener.enterConditional_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConditional_expression" ):
                listener.exitConditional_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConditional_expression" ):
                return visitor.visitConditional_expression(self)
            else:
                return visitor.visitChildren(self)



    def conditional_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_conditional_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 55
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 50
                self.arithmetic_expression(0)
                pass

            elif la_ == 2:
                self.state = 51
                self.match(mathematicalGrammarParser.LP)
                self.state = 52
                self.conditional_expression(0)
                self.state = 53
                self.match(mathematicalGrammarParser.RP)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional_expression)
                        self.state = 57
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 58
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.GT or _la==mathematicalGrammarParser.ST):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 59
                        self.conditional_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional_expression)
                        self.state = 60
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 61
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.GET or _la==mathematicalGrammarParser.SET):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        self.conditional_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional_expression)
                        self.state = 63
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 64
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.EQ or _la==mathematicalGrammarParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        self.conditional_expression(3)
                        pass

             
                self.state = 70
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class Logical_expressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def conditional_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Conditional_expressionContext,0)


        def NOT(self):
            return self.getToken(mathematicalGrammarParser.NOT, 0)

        def logical_expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mathematicalGrammarParser.Logical_expressionContext)
            else:
                return self.getTypedRuleContext(mathematicalGrammarParser.Logical_expressionContext,i)


        def LP(self):
            return self.getToken(mathematicalGrammarParser.LP, 0)

        def RP(self):
            return self.getToken(mathematicalGrammarParser.RP, 0)

        def OR(self):
            return self.getToken(mathematicalGrammarParser.OR, 0)

        def AND(self):
            return self.getToken(mathematicalGrammarParser.AND, 0)

        def getRuleIndex(self):
            return mathematicalGrammarParser.RULE_logical_expression

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogical_expression" ):
                listener.enterLogical_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogical_expression" ):
                listener.exitLogical_expression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogical_expression" ):
                return visitor.visitLogical_expression(self)
            else:
                return visitor.visitChildren(self)



    def logical_expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mathematicalGrammarParser.Logical_expressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 8
        self.enterRecursionRule(localctx, 8, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
            if la_ == 1:
                self.state = 72
                self.conditional_expression(0)
                pass

            elif la_ == 2:
                self.state = 73
                self.match(mathematicalGrammarParser.NOT)
                self.state = 74
                self.logical_expression(2)
                pass

            elif la_ == 3:
                self.state = 75
                self.match(mathematicalGrammarParser.LP)
                self.state = 76
                self.logical_expression(0)
                self.state = 77
                self.match(mathematicalGrammarParser.RP)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 89
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,10,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 87
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
                    if la_ == 1:
                        localctx = mathematicalGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 81
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 82
                        self.match(mathematicalGrammarParser.OR)
                        self.state = 83
                        self.logical_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = mathematicalGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 84
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 85
                        self.match(mathematicalGrammarParser.AND)
                        self.state = 86
                        self.logical_expression(4)
                        pass

             
                self.state = 91
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,10,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.arithmetic_expression_sempred
        self._predicates[3] = self.conditional_expression_sempred
        self._predicates[4] = self.logical_expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def arithmetic_expression_sempred(self, localctx:Arithmetic_expressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 2)
         

    def conditional_expression_sempred(self, localctx:Conditional_expressionContext, predIndex:int):
            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         

    def logical_expression_sempred(self, localctx:Logical_expressionContext, predIndex:int):
            if predIndex == 6:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 7:
                return self.precpred(self._ctx, 3)
         




