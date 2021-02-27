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
        buf.write("W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\3\2\3\2\3\2\3\2\3\2")
        buf.write("\3\2\3\2\3\2\3\2\5\2\24\n\2\3\3\3\3\3\3\3\3\3\3\3\3\5")
        buf.write("\3\34\n\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\7\3\'\n")
        buf.write("\3\f\3\16\3*\13\3\3\4\3\4\3\4\3\4\3\4\3\4\5\4\62\n\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4=\n\4\f\4\16\4@")
        buf.write("\13\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5\5J\n\5\3\5\3\5")
        buf.write("\3\5\3\5\3\5\3\5\7\5R\n\5\f\5\16\5U\13\5\3\5\2\5\4\6\b")
        buf.write("\6\2\4\6\b\2\7\3\2\3\4\3\2\5\6\3\2\b\t\3\2\n\13\3\2\f")
        buf.write("\r\2`\2\23\3\2\2\2\4\33\3\2\2\2\6\61\3\2\2\2\bI\3\2\2")
        buf.write("\2\n\13\5\4\3\2\13\f\7\23\2\2\f\24\3\2\2\2\r\16\5\6\4")
        buf.write("\2\16\17\7\23\2\2\17\24\3\2\2\2\20\21\5\b\5\2\21\22\7")
        buf.write("\23\2\2\22\24\3\2\2\2\23\n\3\2\2\2\23\r\3\2\2\2\23\20")
        buf.write("\3\2\2\2\24\3\3\2\2\2\25\26\b\3\1\2\26\34\7\24\2\2\27")
        buf.write("\30\7\21\2\2\30\31\5\4\3\2\31\32\7\22\2\2\32\34\3\2\2")
        buf.write("\2\33\25\3\2\2\2\33\27\3\2\2\2\34(\3\2\2\2\35\36\f\6\2")
        buf.write("\2\36\37\t\2\2\2\37\'\5\4\3\7 !\f\5\2\2!\"\t\3\2\2\"\'")
        buf.write("\5\4\3\6#$\f\4\2\2$%\7\7\2\2%\'\5\4\3\5&\35\3\2\2\2& ")
        buf.write("\3\2\2\2&#\3\2\2\2\'*\3\2\2\2(&\3\2\2\2()\3\2\2\2)\5\3")
        buf.write("\2\2\2*(\3\2\2\2+,\b\4\1\2,\62\5\4\3\2-.\7\21\2\2./\5")
        buf.write("\6\4\2/\60\7\22\2\2\60\62\3\2\2\2\61+\3\2\2\2\61-\3\2")
        buf.write("\2\2\62>\3\2\2\2\63\64\f\6\2\2\64\65\t\4\2\2\65=\5\6\4")
        buf.write("\7\66\67\f\5\2\2\678\t\5\2\28=\5\6\4\69:\f\4\2\2:;\t\6")
        buf.write("\2\2;=\5\6\4\5<\63\3\2\2\2<\66\3\2\2\2<9\3\2\2\2=@\3\2")
        buf.write("\2\2><\3\2\2\2>?\3\2\2\2?\7\3\2\2\2@>\3\2\2\2AB\b\5\1")
        buf.write("\2BJ\5\6\4\2CD\7\20\2\2DJ\5\b\5\4EF\7\21\2\2FG\5\b\5\2")
        buf.write("GH\7\22\2\2HJ\3\2\2\2IA\3\2\2\2IC\3\2\2\2IE\3\2\2\2JS")
        buf.write("\3\2\2\2KL\f\6\2\2LM\7\16\2\2MR\5\b\5\7NO\f\5\2\2OP\7")
        buf.write("\17\2\2PR\5\b\5\6QK\3\2\2\2QN\3\2\2\2RU\3\2\2\2SQ\3\2")
        buf.write("\2\2ST\3\2\2\2T\t\3\2\2\2US\3\2\2\2\f\23\33&(\61<>IQS")
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
    RULE_arithmetic_expression = 1
    RULE_conditional_expression = 2
    RULE_logical_expression = 3

    ruleNames =  [ "startRule", "arithmetic_expression", "conditional_expression", 
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

        def arithmetic_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Arithmetic_expressionContext,0)


        def SEMICOLON(self):
            return self.getToken(mathematicalGrammarParser.SEMICOLON, 0)

        def conditional_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Conditional_expressionContext,0)


        def logical_expression(self):
            return self.getTypedRuleContext(mathematicalGrammarParser.Logical_expressionContext,0)


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
        try:
            self.state = 17
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 8
                self.arithmetic_expression(0)
                self.state = 9
                self.match(mathematicalGrammarParser.SEMICOLON)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 11
                self.conditional_expression(0)
                self.state = 12
                self.match(mathematicalGrammarParser.SEMICOLON)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 14
                self.logical_expression(0)
                self.state = 15
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
        _startState = 2
        self.enterRecursionRule(localctx, 2, self.RULE_arithmetic_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mathematicalGrammarParser.INT]:
                self.state = 20
                self.match(mathematicalGrammarParser.INT)
                pass
            elif token in [mathematicalGrammarParser.LP]:
                self.state = 21
                self.match(mathematicalGrammarParser.LP)
                self.state = 22
                self.arithmetic_expression(0)
                self.state = 23
                self.match(mathematicalGrammarParser.RP)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 36
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 27
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 28
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.PLUS or _la==mathematicalGrammarParser.MINUS):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 29
                        self.arithmetic_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 30
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 31
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.TIMES or _la==mathematicalGrammarParser.DIV):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 32
                        self.arithmetic_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = mathematicalGrammarParser.Arithmetic_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_arithmetic_expression)
                        self.state = 33
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 34
                        self.match(mathematicalGrammarParser.MODULO)
                        self.state = 35
                        self.arithmetic_expression(3)
                        pass

             
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_conditional_expression, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 42
                self.arithmetic_expression(0)
                pass

            elif la_ == 2:
                self.state = 43
                self.match(mathematicalGrammarParser.LP)
                self.state = 44
                self.conditional_expression(0)
                self.state = 45
                self.match(mathematicalGrammarParser.RP)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 60
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 58
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
                    if la_ == 1:
                        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional_expression)
                        self.state = 49
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 50
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.GT or _la==mathematicalGrammarParser.ST):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 51
                        self.conditional_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional_expression)
                        self.state = 52
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 53
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.GET or _la==mathematicalGrammarParser.SET):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 54
                        self.conditional_expression(4)
                        pass

                    elif la_ == 3:
                        localctx = mathematicalGrammarParser.Conditional_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_conditional_expression)
                        self.state = 55
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 56
                        _la = self._input.LA(1)
                        if not(_la==mathematicalGrammarParser.EQ or _la==mathematicalGrammarParser.NEQ):
                            self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 57
                        self.conditional_expression(3)
                        pass

             
                self.state = 62
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_logical_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 64
                self.conditional_expression(0)
                pass

            elif la_ == 2:
                self.state = 65
                self.match(mathematicalGrammarParser.NOT)
                self.state = 66
                self.logical_expression(2)
                pass

            elif la_ == 3:
                self.state = 67
                self.match(mathematicalGrammarParser.LP)
                self.state = 68
                self.logical_expression(0)
                self.state = 69
                self.match(mathematicalGrammarParser.RP)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,9,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 79
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,8,self._ctx)
                    if la_ == 1:
                        localctx = mathematicalGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 73
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 74
                        self.match(mathematicalGrammarParser.OR)
                        self.state = 75
                        self.logical_expression(5)
                        pass

                    elif la_ == 2:
                        localctx = mathematicalGrammarParser.Logical_expressionContext(self, _parentctx, _parentState)
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_logical_expression)
                        self.state = 76
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 77
                        self.match(mathematicalGrammarParser.AND)
                        self.state = 78
                        self.logical_expression(4)
                        pass

             
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,9,self._ctx)

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
        self._predicates[1] = self.arithmetic_expression_sempred
        self._predicates[2] = self.conditional_expression_sempred
        self._predicates[3] = self.logical_expression_sempred
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
         




