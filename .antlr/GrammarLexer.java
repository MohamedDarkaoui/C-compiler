// Generated from /home/mohamed/CLionProjects/C-compiler/Grammar.g4 by ANTLR 4.8
import org.antlr.v4.runtime.Lexer;
import org.antlr.v4.runtime.CharStream;
import org.antlr.v4.runtime.Token;
import org.antlr.v4.runtime.TokenStream;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.misc.*;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GrammarLexer extends Lexer {
	static { RuntimeMetaData.checkVersion("4.8", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		IF=1, ELSE=2, WHILE=3, EQ=4, NEQ=5, GT=6, ST=7, GET=8, SET=9, LB=10, RB=11, 
		PLUS=12, MINUS=13, TIMES=14, DIV=15, MODULO=16, BC=17, EC=18, LP=19, RP=20, 
		COMMENT1=21, COMMENT2=22, ASSIGN=23, SEMICOLON=24, POINT=25, AMPERSAND=26, 
		UNSIGNED_INT=27, DIGIT=28, WS=29, CONST=30, UNDERSCORE=31, INT=32, CHAR=33, 
		FLOAT=34, VOID=35, RETURN=36, ID=37, CHARACTER=38, COMMA=39;
	public static String[] channelNames = {
		"DEFAULT_TOKEN_CHANNEL", "HIDDEN"
	};

	public static String[] modeNames = {
		"DEFAULT_MODE"
	};

	private static String[] makeRuleNames() {
		return new String[] {
			"IF", "ELSE", "WHILE", "EQ", "NEQ", "GT", "ST", "GET", "SET", "LB", "RB", 
			"PLUS", "MINUS", "TIMES", "DIV", "MODULO", "BC", "EC", "LP", "RP", "COMMENT1", 
			"COMMENT2", "ASSIGN", "SEMICOLON", "POINT", "AMPERSAND", "UNSIGNED_INT", 
			"DIGIT", "WS", "CONST", "UNDERSCORE", "INT", "CHAR", "FLOAT", "VOID", 
			"RETURN", "ID", "CHARACTER", "COMMA"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'if'", "'else'", "'while'", "'=='", "'!='", "'>'", "'<'", "'>='", 
			"'<='", "'{'", "'}'", "'+'", "'-'", "'*'", "'/'", "'%'", "'/*'", "'*/'", 
			"'('", "')'", null, null, "'='", "';'", "'.'", "'&'", null, null, null, 
			"'const'", "'_'", "'int'", "'char'", "'float'", "'void'", "'return'", 
			null, null, "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "IF", "ELSE", "WHILE", "EQ", "NEQ", "GT", "ST", "GET", "SET", "LB", 
			"RB", "PLUS", "MINUS", "TIMES", "DIV", "MODULO", "BC", "EC", "LP", "RP", 
			"COMMENT1", "COMMENT2", "ASSIGN", "SEMICOLON", "POINT", "AMPERSAND", 
			"UNSIGNED_INT", "DIGIT", "WS", "CONST", "UNDERSCORE", "INT", "CHAR", 
			"FLOAT", "VOID", "RETURN", "ID", "CHARACTER", "COMMA"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}


	public GrammarLexer(CharStream input) {
		super(input);
		_interp = new LexerATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public String[] getChannelNames() { return channelNames; }

	@Override
	public String[] getModeNames() { return modeNames; }

	@Override
	public ATN getATN() { return _ATN; }

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2)\u00e8\b\1\4\2\t"+
		"\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13"+
		"\t\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36\t\36\4\37\t\37\4 \t \4!"+
		"\t!\4\"\t\"\4#\t#\4$\t$\4%\t%\4&\t&\4\'\t\'\4(\t(\3\2\3\2\3\2\3\3\3\3"+
		"\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3"+
		"\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\17"+
		"\3\17\3\20\3\20\3\21\3\21\3\22\3\22\3\22\3\23\3\23\3\23\3\24\3\24\3\25"+
		"\3\25\3\26\3\26\3\26\3\26\7\26\u008c\n\26\f\26\16\26\u008f\13\26\3\26"+
		"\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\7\27\u009a\n\27\f\27\16\27\u009d"+
		"\13\27\3\27\3\27\3\27\3\27\3\30\3\30\3\31\3\31\3\32\3\32\3\33\3\33\3\34"+
		"\6\34\u00ac\n\34\r\34\16\34\u00ad\3\35\3\35\3\36\6\36\u00b3\n\36\r\36"+
		"\16\36\u00b4\3\36\3\36\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3!\3!\3!\3"+
		"!\3\"\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3#\3$\3$\3$\3$\3$\3%\3%\3%\3%\3%"+
		"\3%\3%\3&\3&\7&\u00de\n&\f&\16&\u00e1\13&\3\'\3\'\3\'\3\'\3(\3(\4\u008d"+
		"\u009b\2)\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33"+
		"\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32\63\33\65\34\67"+
		"\359\36;\37= ?!A\"C#E$G%I&K\'M(O)\3\2\6\3\2\62;\5\2\13\f\17\17\"\"\5\2"+
		"C\\aac|\6\2\62;C\\aac|\2\u00ec\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t"+
		"\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2"+
		"\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2"+
		"\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2"+
		"+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2"+
		"\2\67\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2"+
		"C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2\2\2\2O\3"+
		"\2\2\2\3Q\3\2\2\2\5T\3\2\2\2\7Y\3\2\2\2\t_\3\2\2\2\13b\3\2\2\2\re\3\2"+
		"\2\2\17g\3\2\2\2\21i\3\2\2\2\23l\3\2\2\2\25o\3\2\2\2\27q\3\2\2\2\31s\3"+
		"\2\2\2\33u\3\2\2\2\35w\3\2\2\2\37y\3\2\2\2!{\3\2\2\2#}\3\2\2\2%\u0080"+
		"\3\2\2\2\'\u0083\3\2\2\2)\u0085\3\2\2\2+\u0087\3\2\2\2-\u0095\3\2\2\2"+
		"/\u00a2\3\2\2\2\61\u00a4\3\2\2\2\63\u00a6\3\2\2\2\65\u00a8\3\2\2\2\67"+
		"\u00ab\3\2\2\29\u00af\3\2\2\2;\u00b2\3\2\2\2=\u00b8\3\2\2\2?\u00be\3\2"+
		"\2\2A\u00c0\3\2\2\2C\u00c4\3\2\2\2E\u00c9\3\2\2\2G\u00cf\3\2\2\2I\u00d4"+
		"\3\2\2\2K\u00db\3\2\2\2M\u00e2\3\2\2\2O\u00e6\3\2\2\2QR\7k\2\2RS\7h\2"+
		"\2S\4\3\2\2\2TU\7g\2\2UV\7n\2\2VW\7u\2\2WX\7g\2\2X\6\3\2\2\2YZ\7y\2\2"+
		"Z[\7j\2\2[\\\7k\2\2\\]\7n\2\2]^\7g\2\2^\b\3\2\2\2_`\7?\2\2`a\7?\2\2a\n"+
		"\3\2\2\2bc\7#\2\2cd\7?\2\2d\f\3\2\2\2ef\7@\2\2f\16\3\2\2\2gh\7>\2\2h\20"+
		"\3\2\2\2ij\7@\2\2jk\7?\2\2k\22\3\2\2\2lm\7>\2\2mn\7?\2\2n\24\3\2\2\2o"+
		"p\7}\2\2p\26\3\2\2\2qr\7\177\2\2r\30\3\2\2\2st\7-\2\2t\32\3\2\2\2uv\7"+
		"/\2\2v\34\3\2\2\2wx\7,\2\2x\36\3\2\2\2yz\7\61\2\2z \3\2\2\2{|\7\'\2\2"+
		"|\"\3\2\2\2}~\7\61\2\2~\177\7,\2\2\177$\3\2\2\2\u0080\u0081\7,\2\2\u0081"+
		"\u0082\7\61\2\2\u0082&\3\2\2\2\u0083\u0084\7*\2\2\u0084(\3\2\2\2\u0085"+
		"\u0086\7+\2\2\u0086*\3\2\2\2\u0087\u0088\7\61\2\2\u0088\u0089\7,\2\2\u0089"+
		"\u008d\3\2\2\2\u008a\u008c\13\2\2\2\u008b\u008a\3\2\2\2\u008c\u008f\3"+
		"\2\2\2\u008d\u008e\3\2\2\2\u008d\u008b\3\2\2\2\u008e\u0090\3\2\2\2\u008f"+
		"\u008d\3\2\2\2\u0090\u0091\7,\2\2\u0091\u0092\7\61\2\2\u0092\u0093\3\2"+
		"\2\2\u0093\u0094\b\26\2\2\u0094,\3\2\2\2\u0095\u0096\7\61\2\2\u0096\u0097"+
		"\7\61\2\2\u0097\u009b\3\2\2\2\u0098\u009a\13\2\2\2\u0099\u0098\3\2\2\2"+
		"\u009a\u009d\3\2\2\2\u009b\u009c\3\2\2\2\u009b\u0099\3\2\2\2\u009c\u009e"+
		"\3\2\2\2\u009d\u009b\3\2\2\2\u009e\u009f\7\f\2\2\u009f\u00a0\3\2\2\2\u00a0"+
		"\u00a1\b\27\2\2\u00a1.\3\2\2\2\u00a2\u00a3\7?\2\2\u00a3\60\3\2\2\2\u00a4"+
		"\u00a5\7=\2\2\u00a5\62\3\2\2\2\u00a6\u00a7\7\60\2\2\u00a7\64\3\2\2\2\u00a8"+
		"\u00a9\7(\2\2\u00a9\66\3\2\2\2\u00aa\u00ac\t\2\2\2\u00ab\u00aa\3\2\2\2"+
		"\u00ac\u00ad\3\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae8\3"+
		"\2\2\2\u00af\u00b0\t\2\2\2\u00b0:\3\2\2\2\u00b1\u00b3\t\3\2\2\u00b2\u00b1"+
		"\3\2\2\2\u00b3\u00b4\3\2\2\2\u00b4\u00b2\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5"+
		"\u00b6\3\2\2\2\u00b6\u00b7\b\36\2\2\u00b7<\3\2\2\2\u00b8\u00b9\7e\2\2"+
		"\u00b9\u00ba\7q\2\2\u00ba\u00bb\7p\2\2\u00bb\u00bc\7u\2\2\u00bc\u00bd"+
		"\7v\2\2\u00bd>\3\2\2\2\u00be\u00bf\7a\2\2\u00bf@\3\2\2\2\u00c0\u00c1\7"+
		"k\2\2\u00c1\u00c2\7p\2\2\u00c2\u00c3\7v\2\2\u00c3B\3\2\2\2\u00c4\u00c5"+
		"\7e\2\2\u00c5\u00c6\7j\2\2\u00c6\u00c7\7c\2\2\u00c7\u00c8\7t\2\2\u00c8"+
		"D\3\2\2\2\u00c9\u00ca\7h\2\2\u00ca\u00cb\7n\2\2\u00cb\u00cc\7q\2\2\u00cc"+
		"\u00cd\7c\2\2\u00cd\u00ce\7v\2\2\u00ceF\3\2\2\2\u00cf\u00d0\7x\2\2\u00d0"+
		"\u00d1\7q\2\2\u00d1\u00d2\7k\2\2\u00d2\u00d3\7f\2\2\u00d3H\3\2\2\2\u00d4"+
		"\u00d5\7t\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7v\2\2\u00d7\u00d8\7w\2\2"+
		"\u00d8\u00d9\7t\2\2\u00d9\u00da\7p\2\2\u00daJ\3\2\2\2\u00db\u00df\t\4"+
		"\2\2\u00dc\u00de\t\5\2\2\u00dd\u00dc\3\2\2\2\u00de\u00e1\3\2\2\2\u00df"+
		"\u00dd\3\2\2\2\u00df\u00e0\3\2\2\2\u00e0L\3\2\2\2\u00e1\u00df\3\2\2\2"+
		"\u00e2\u00e3\7)\2\2\u00e3\u00e4\13\2\2\2\u00e4\u00e5\7)\2\2\u00e5N\3\2"+
		"\2\2\u00e6\u00e7\7.\2\2\u00e7P\3\2\2\2\b\2\u008d\u009b\u00ad\u00b4\u00df"+
		"\3\b\2\2";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}