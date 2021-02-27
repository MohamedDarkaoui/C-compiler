# Generated from mathematicalGrammar.g4 by ANTLR 4.9.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\25")
        buf.write("]\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7")
        buf.write("\3\7\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\r\3\r\3\r\3\16\3\16\3\16\3\17\3\17\3\20\3")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\6\23S\n\23\r\23\16\23T\3")
        buf.write("\24\6\24X\n\24\r\24\16\24Y\3\24\3\24\2\2\25\3\3\5\4\7")
        buf.write("\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33\17")
        buf.write("\35\20\37\21!\22#\23%\24\'\25\3\2\4\3\2\62;\5\2\13\f\17")
        buf.write("\17\"\"\2^\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2")
        buf.write("\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2")
        buf.write("\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write("\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#")
        buf.write("\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\3)\3\2\2\2\5+\3\2\2\2")
        buf.write("\7-\3\2\2\2\t/\3\2\2\2\13\61\3\2\2\2\r\63\3\2\2\2\17\65")
        buf.write("\3\2\2\2\21\67\3\2\2\2\23:\3\2\2\2\25=\3\2\2\2\27@\3\2")
        buf.write("\2\2\31C\3\2\2\2\33F\3\2\2\2\35I\3\2\2\2\37K\3\2\2\2!")
        buf.write("M\3\2\2\2#O\3\2\2\2%R\3\2\2\2\'W\3\2\2\2)*\7-\2\2*\4\3")
        buf.write("\2\2\2+,\7/\2\2,\6\3\2\2\2-.\7,\2\2.\b\3\2\2\2/\60\7\61")
        buf.write("\2\2\60\n\3\2\2\2\61\62\7\'\2\2\62\f\3\2\2\2\63\64\7@")
        buf.write("\2\2\64\16\3\2\2\2\65\66\7>\2\2\66\20\3\2\2\2\678\7@\2")
        buf.write("\289\7?\2\29\22\3\2\2\2:;\7>\2\2;<\7?\2\2<\24\3\2\2\2")
        buf.write("=>\7?\2\2>?\7?\2\2?\26\3\2\2\2@A\7#\2\2AB\7?\2\2B\30\3")
        buf.write("\2\2\2CD\7~\2\2DE\7~\2\2E\32\3\2\2\2FG\7(\2\2GH\7(\2\2")
        buf.write("H\34\3\2\2\2IJ\7#\2\2J\36\3\2\2\2KL\7*\2\2L \3\2\2\2M")
        buf.write("N\7+\2\2N\"\3\2\2\2OP\7=\2\2P$\3\2\2\2QS\t\2\2\2RQ\3\2")
        buf.write("\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U&\3\2\2\2VX\t\3\2\2")
        buf.write("WV\3\2\2\2XY\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z[\3\2\2\2[\\")
        buf.write("\b\24\2\2\\(\3\2\2\2\5\2TY\3\b\2\2")
        return buf.getvalue()


class mathematicalGrammarLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    PLUS = 1
    MINUS = 2
    TIMES = 3
    DIV = 4
    MODULO = 5
    GT = 6
    ST = 7
    GET = 8
    SET = 9
    EQ = 10
    NEQ = 11
    OR = 12
    AND = 13
    NOT = 14
    LP = 15
    RP = 16
    SEMICOLON = 17
    INT = 18
    WS = 19

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'%'", "'>'", "'<'", "'>='", "'<='", 
            "'=='", "'!='", "'||'", "'&&'", "'!'", "'('", "')'", "';'" ]

    symbolicNames = [ "<INVALID>",
            "PLUS", "MINUS", "TIMES", "DIV", "MODULO", "GT", "ST", "GET", 
            "SET", "EQ", "NEQ", "OR", "AND", "NOT", "LP", "RP", "SEMICOLON", 
            "INT", "WS" ]

    ruleNames = [ "PLUS", "MINUS", "TIMES", "DIV", "MODULO", "GT", "ST", 
                  "GET", "SET", "EQ", "NEQ", "OR", "AND", "NOT", "LP", "RP", 
                  "SEMICOLON", "INT", "WS" ]

    grammarFileName = "mathematicalGrammar.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


