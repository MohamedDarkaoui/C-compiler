// Generated from /home/mohamed/CLionProjects/C-compiler/Grammar.g4 by ANTLR 4.8
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class GrammarParser extends Parser {
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
	public static final int
		RULE_startRule = 0, RULE_signed_int = 1, RULE_float_number = 2, RULE_types = 3, 
		RULE_function_types = 4, RULE_variable = 5, RULE_character = 6, RULE_arg = 7, 
		RULE_arguments = 8, RULE_statement = 9, RULE_declaration = 10, RULE_definition = 11, 
		RULE_assignment = 12, RULE_if_statement = 13, RULE_else_if_statement = 14, 
		RULE_else_statement = 15, RULE_selection_sequence = 16, RULE_while_statement = 17, 
		RULE_function_declaration = 18, RULE_function_definition = 19, RULE_function = 20, 
		RULE_block = 21, RULE_expression = 22, RULE_arithmetic_expression = 23, 
		RULE_comparison_expression = 24, RULE_condition = 25;
	private static String[] makeRuleNames() {
		return new String[] {
			"startRule", "signed_int", "float_number", "types", "function_types", 
			"variable", "character", "arg", "arguments", "statement", "declaration", 
			"definition", "assignment", "if_statement", "else_if_statement", "else_statement", 
			"selection_sequence", "while_statement", "function_declaration", "function_definition", 
			"function", "block", "expression", "arithmetic_expression", "comparison_expression", 
			"condition"
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

	@Override
	public String getGrammarFileName() { return "Grammar.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public GrammarParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartRuleContext extends ParserRuleContext {
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode EOF() { return getToken(GrammarParser.EOF, 0); }
		public StartRuleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_startRule; }
	}

	public final StartRuleContext startRule() throws RecognitionException {
		StartRuleContext _localctx = new StartRuleContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_startRule);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(52);
			block();
			setState(53);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Signed_intContext extends ParserRuleContext {
		public TerminalNode UNSIGNED_INT() { return getToken(GrammarParser.UNSIGNED_INT, 0); }
		public TerminalNode PLUS() { return getToken(GrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GrammarParser.MINUS, 0); }
		public Signed_intContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_signed_int; }
	}

	public final Signed_intContext signed_int() throws RecognitionException {
		Signed_intContext _localctx = new Signed_intContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_signed_int);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(58);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
				{
				setState(55);
				match(PLUS);
				}
				break;
			case MINUS:
				{
				setState(56);
				match(MINUS);
				}
				break;
			case UNSIGNED_INT:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(60);
			match(UNSIGNED_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Float_numberContext extends ParserRuleContext {
		public List<TerminalNode> UNSIGNED_INT() { return getTokens(GrammarParser.UNSIGNED_INT); }
		public TerminalNode UNSIGNED_INT(int i) {
			return getToken(GrammarParser.UNSIGNED_INT, i);
		}
		public TerminalNode POINT() { return getToken(GrammarParser.POINT, 0); }
		public TerminalNode PLUS() { return getToken(GrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GrammarParser.MINUS, 0); }
		public Float_numberContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_float_number; }
	}

	public final Float_numberContext float_number() throws RecognitionException {
		Float_numberContext _localctx = new Float_numberContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_float_number);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(65);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
				{
				setState(62);
				match(PLUS);
				}
				break;
			case MINUS:
				{
				setState(63);
				match(MINUS);
				}
				break;
			case UNSIGNED_INT:
				{
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			setState(67);
			match(UNSIGNED_INT);
			setState(68);
			match(POINT);
			setState(69);
			match(UNSIGNED_INT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class TypesContext extends ParserRuleContext {
		public TerminalNode INT() { return getToken(GrammarParser.INT, 0); }
		public TerminalNode CHAR() { return getToken(GrammarParser.CHAR, 0); }
		public TerminalNode FLOAT() { return getToken(GrammarParser.FLOAT, 0); }
		public TypesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_types; }
	}

	public final TypesContext types() throws RecognitionException {
		TypesContext _localctx = new TypesContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_types);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			_la = _input.LA(1);
			if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << CHAR) | (1L << FLOAT))) != 0)) ) {
			_errHandler.recoverInline(this);
			}
			else {
				if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
				_errHandler.reportMatch(this);
				consume();
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_typesContext extends ParserRuleContext {
		public TypesContext types() {
			return getRuleContext(TypesContext.class,0);
		}
		public TerminalNode VOID() { return getToken(GrammarParser.VOID, 0); }
		public Function_typesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_types; }
	}

	public final Function_typesContext function_types() throws RecognitionException {
		Function_typesContext _localctx = new Function_typesContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_function_types);
		try {
			setState(75);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case INT:
			case CHAR:
			case FLOAT:
				enterOuterAlt(_localctx, 1);
				{
				setState(73);
				types();
				}
				break;
			case VOID:
				enterOuterAlt(_localctx, 2);
				{
				setState(74);
				match(VOID);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class VariableContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(GrammarParser.ID, 0); }
		public VariableContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_variable; }
	}

	public final VariableContext variable() throws RecognitionException {
		VariableContext _localctx = new VariableContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_variable);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(77);
			match(ID);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CharacterContext extends ParserRuleContext {
		public TerminalNode CHARACTER() { return getToken(GrammarParser.CHARACTER, 0); }
		public CharacterContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_character; }
	}

	public final CharacterContext character() throws RecognitionException {
		CharacterContext _localctx = new CharacterContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_character);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(79);
			match(CHARACTER);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgContext extends ParserRuleContext {
		public TypesContext types() {
			return getRuleContext(TypesContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public ArgContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arg; }
	}

	public final ArgContext arg() throws RecognitionException {
		ArgContext _localctx = new ArgContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_arg);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(81);
			types();
			setState(82);
			variable();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ArgumentsContext extends ParserRuleContext {
		public List<ArgContext> arg() {
			return getRuleContexts(ArgContext.class);
		}
		public ArgContext arg(int i) {
			return getRuleContext(ArgContext.class,i);
		}
		public List<TerminalNode> COMMA() { return getTokens(GrammarParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(GrammarParser.COMMA, i);
		}
		public ArgumentsContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arguments; }
	}

	public final ArgumentsContext arguments() throws RecognitionException {
		ArgumentsContext _localctx = new ArgumentsContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_arguments);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(92);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << INT) | (1L << CHAR) | (1L << FLOAT))) != 0)) {
				{
				{
				setState(84);
				arg();
				}
				setState(89);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==COMMA) {
					{
					{
					setState(85);
					match(COMMA);
					setState(86);
					arg();
					}
					}
					setState(91);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class StatementContext extends ParserRuleContext {
		public DefinitionContext definition() {
			return getRuleContext(DefinitionContext.class,0);
		}
		public DeclarationContext declaration() {
			return getRuleContext(DeclarationContext.class,0);
		}
		public AssignmentContext assignment() {
			return getRuleContext(AssignmentContext.class,0);
		}
		public Selection_sequenceContext selection_sequence() {
			return getRuleContext(Selection_sequenceContext.class,0);
		}
		public While_statementContext while_statement() {
			return getRuleContext(While_statementContext.class,0);
		}
		public FunctionContext function() {
			return getRuleContext(FunctionContext.class,0);
		}
		public StatementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_statement; }
	}

	public final StatementContext statement() throws RecognitionException {
		StatementContext _localctx = new StatementContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_statement);
		try {
			setState(100);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,5,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(94);
				definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(95);
				declaration();
				}
				break;
			case 3:
				enterOuterAlt(_localctx, 3);
				{
				setState(96);
				assignment();
				}
				break;
			case 4:
				enterOuterAlt(_localctx, 4);
				{
				setState(97);
				selection_sequence();
				}
				break;
			case 5:
				enterOuterAlt(_localctx, 5);
				{
				setState(98);
				while_statement();
				}
				break;
			case 6:
				enterOuterAlt(_localctx, 6);
				{
				setState(99);
				function();
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public TypesContext types() {
			return getRuleContext(TypesContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(GrammarParser.SEMICOLON, 0); }
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(102);
			types();
			setState(103);
			variable();
			setState(104);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DefinitionContext extends ParserRuleContext {
		public TypesContext types() {
			return getRuleContext(TypesContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(GrammarParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(GrammarParser.SEMICOLON, 0); }
		public TerminalNode CONST() { return getToken(GrammarParser.CONST, 0); }
		public DefinitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_definition; }
	}

	public final DefinitionContext definition() throws RecognitionException {
		DefinitionContext _localctx = new DefinitionContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_definition);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(107);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==CONST) {
				{
				setState(106);
				match(CONST);
				}
			}

			setState(109);
			types();
			setState(110);
			variable();
			setState(111);
			match(ASSIGN);
			setState(112);
			expression();
			setState(113);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class AssignmentContext extends ParserRuleContext {
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode ASSIGN() { return getToken(GrammarParser.ASSIGN, 0); }
		public ExpressionContext expression() {
			return getRuleContext(ExpressionContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(GrammarParser.SEMICOLON, 0); }
		public AssignmentContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_assignment; }
	}

	public final AssignmentContext assignment() throws RecognitionException {
		AssignmentContext _localctx = new AssignmentContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_assignment);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(115);
			variable();
			setState(116);
			match(ASSIGN);
			setState(117);
			expression();
			setState(118);
			match(SEMICOLON);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class If_statementContext extends ParserRuleContext {
		public TerminalNode IF() { return getToken(GrammarParser.IF, 0); }
		public TerminalNode LP() { return getToken(GrammarParser.LP, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RP() { return getToken(GrammarParser.RP, 0); }
		public TerminalNode LB() { return getToken(GrammarParser.LB, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RB() { return getToken(GrammarParser.RB, 0); }
		public If_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_if_statement; }
	}

	public final If_statementContext if_statement() throws RecognitionException {
		If_statementContext _localctx = new If_statementContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(120);
			match(IF);
			setState(121);
			match(LP);
			setState(122);
			condition();
			setState(123);
			match(RP);
			setState(124);
			match(LB);
			setState(125);
			block();
			setState(126);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_if_statementContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(GrammarParser.ELSE, 0); }
		public TerminalNode IF() { return getToken(GrammarParser.IF, 0); }
		public TerminalNode LP() { return getToken(GrammarParser.LP, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RP() { return getToken(GrammarParser.RP, 0); }
		public TerminalNode LB() { return getToken(GrammarParser.LB, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RB() { return getToken(GrammarParser.RB, 0); }
		public Else_if_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_if_statement; }
	}

	public final Else_if_statementContext else_if_statement() throws RecognitionException {
		Else_if_statementContext _localctx = new Else_if_statementContext(_ctx, getState());
		enterRule(_localctx, 28, RULE_else_if_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(128);
			match(ELSE);
			setState(129);
			match(IF);
			setState(130);
			match(LP);
			setState(131);
			condition();
			setState(132);
			match(RP);
			setState(133);
			match(LB);
			setState(134);
			block();
			setState(135);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Else_statementContext extends ParserRuleContext {
		public TerminalNode ELSE() { return getToken(GrammarParser.ELSE, 0); }
		public TerminalNode LB() { return getToken(GrammarParser.LB, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RB() { return getToken(GrammarParser.RB, 0); }
		public Else_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_else_statement; }
	}

	public final Else_statementContext else_statement() throws RecognitionException {
		Else_statementContext _localctx = new Else_statementContext(_ctx, getState());
		enterRule(_localctx, 30, RULE_else_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(137);
			match(ELSE);
			setState(138);
			match(LB);
			setState(139);
			block();
			setState(140);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Selection_sequenceContext extends ParserRuleContext {
		public If_statementContext if_statement() {
			return getRuleContext(If_statementContext.class,0);
		}
		public List<Else_if_statementContext> else_if_statement() {
			return getRuleContexts(Else_if_statementContext.class);
		}
		public Else_if_statementContext else_if_statement(int i) {
			return getRuleContext(Else_if_statementContext.class,i);
		}
		public Else_statementContext else_statement() {
			return getRuleContext(Else_statementContext.class,0);
		}
		public Selection_sequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_selection_sequence; }
	}

	public final Selection_sequenceContext selection_sequence() throws RecognitionException {
		Selection_sequenceContext _localctx = new Selection_sequenceContext(_ctx, getState());
		enterRule(_localctx, 32, RULE_selection_sequence);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(142);
			if_statement();
			setState(146);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(143);
					else_if_statement();
					}
					} 
				}
				setState(148);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,7,_ctx);
			}
			setState(150);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ELSE) {
				{
				setState(149);
				else_statement();
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class While_statementContext extends ParserRuleContext {
		public TerminalNode WHILE() { return getToken(GrammarParser.WHILE, 0); }
		public TerminalNode LP() { return getToken(GrammarParser.LP, 0); }
		public ConditionContext condition() {
			return getRuleContext(ConditionContext.class,0);
		}
		public TerminalNode RP() { return getToken(GrammarParser.RP, 0); }
		public TerminalNode LB() { return getToken(GrammarParser.LB, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RB() { return getToken(GrammarParser.RB, 0); }
		public While_statementContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_while_statement; }
	}

	public final While_statementContext while_statement() throws RecognitionException {
		While_statementContext _localctx = new While_statementContext(_ctx, getState());
		enterRule(_localctx, 34, RULE_while_statement);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(152);
			match(WHILE);
			setState(153);
			match(LP);
			setState(154);
			condition();
			setState(155);
			match(RP);
			setState(156);
			match(LB);
			setState(157);
			block();
			setState(158);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_declarationContext extends ParserRuleContext {
		public Function_typesContext function_types() {
			return getRuleContext(Function_typesContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public TerminalNode LP() { return getToken(GrammarParser.LP, 0); }
		public ArgumentsContext arguments() {
			return getRuleContext(ArgumentsContext.class,0);
		}
		public TerminalNode RP() { return getToken(GrammarParser.RP, 0); }
		public Function_declarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_declaration; }
	}

	public final Function_declarationContext function_declaration() throws RecognitionException {
		Function_declarationContext _localctx = new Function_declarationContext(_ctx, getState());
		enterRule(_localctx, 36, RULE_function_declaration);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(160);
			function_types();
			setState(161);
			variable();
			setState(162);
			match(LP);
			setState(163);
			arguments();
			setState(164);
			match(RP);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Function_definitionContext extends ParserRuleContext {
		public Function_declarationContext function_declaration() {
			return getRuleContext(Function_declarationContext.class,0);
		}
		public TerminalNode LB() { return getToken(GrammarParser.LB, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public TerminalNode RB() { return getToken(GrammarParser.RB, 0); }
		public Function_definitionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function_definition; }
	}

	public final Function_definitionContext function_definition() throws RecognitionException {
		Function_definitionContext _localctx = new Function_definitionContext(_ctx, getState());
		enterRule(_localctx, 38, RULE_function_definition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(166);
			function_declaration();
			setState(167);
			match(LB);
			setState(168);
			block();
			setState(169);
			match(RB);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FunctionContext extends ParserRuleContext {
		public Function_definitionContext function_definition() {
			return getRuleContext(Function_definitionContext.class,0);
		}
		public Function_declarationContext function_declaration() {
			return getRuleContext(Function_declarationContext.class,0);
		}
		public TerminalNode SEMICOLON() { return getToken(GrammarParser.SEMICOLON, 0); }
		public FunctionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_function; }
	}

	public final FunctionContext function() throws RecognitionException {
		FunctionContext _localctx = new FunctionContext(_ctx, getState());
		enterRule(_localctx, 40, RULE_function);
		try {
			setState(175);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,9,_ctx) ) {
			case 1:
				enterOuterAlt(_localctx, 1);
				{
				setState(171);
				function_definition();
				}
				break;
			case 2:
				enterOuterAlt(_localctx, 2);
				{
				setState(172);
				function_declaration();
				setState(173);
				match(SEMICOLON);
				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public List<StatementContext> statement() {
			return getRuleContexts(StatementContext.class);
		}
		public StatementContext statement(int i) {
			return getRuleContext(StatementContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 42, RULE_block);
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(180);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			while ( _alt!=1 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1+1 ) {
					{
					{
					setState(177);
					statement();
					}
					} 
				}
				setState(182);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,10,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public Arithmetic_expressionContext arithmetic_expression() {
			return getRuleContext(Arithmetic_expressionContext.class,0);
		}
		public CharacterContext character() {
			return getRuleContext(CharacterContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 44, RULE_expression);
		try {
			setState(185);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case PLUS:
			case MINUS:
			case LP:
			case UNSIGNED_INT:
			case ID:
				enterOuterAlt(_localctx, 1);
				{
				setState(183);
				arithmetic_expression(0);
				}
				break;
			case CHARACTER:
				enterOuterAlt(_localctx, 2);
				{
				setState(184);
				character();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Arithmetic_expressionContext extends ParserRuleContext {
		public Signed_intContext signed_int() {
			return getRuleContext(Signed_intContext.class,0);
		}
		public VariableContext variable() {
			return getRuleContext(VariableContext.class,0);
		}
		public Float_numberContext float_number() {
			return getRuleContext(Float_numberContext.class,0);
		}
		public TerminalNode LP() { return getToken(GrammarParser.LP, 0); }
		public List<Arithmetic_expressionContext> arithmetic_expression() {
			return getRuleContexts(Arithmetic_expressionContext.class);
		}
		public Arithmetic_expressionContext arithmetic_expression(int i) {
			return getRuleContext(Arithmetic_expressionContext.class,i);
		}
		public TerminalNode RP() { return getToken(GrammarParser.RP, 0); }
		public TerminalNode TIMES() { return getToken(GrammarParser.TIMES, 0); }
		public TerminalNode DIV() { return getToken(GrammarParser.DIV, 0); }
		public TerminalNode PLUS() { return getToken(GrammarParser.PLUS, 0); }
		public TerminalNode MINUS() { return getToken(GrammarParser.MINUS, 0); }
		public TerminalNode MODULO() { return getToken(GrammarParser.MODULO, 0); }
		public Arithmetic_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_arithmetic_expression; }
	}

	public final Arithmetic_expressionContext arithmetic_expression() throws RecognitionException {
		return arithmetic_expression(0);
	}

	private Arithmetic_expressionContext arithmetic_expression(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		Arithmetic_expressionContext _localctx = new Arithmetic_expressionContext(_ctx, _parentState);
		Arithmetic_expressionContext _prevctx = _localctx;
		int _startState = 46;
		enterRecursionRule(_localctx, 46, RULE_arithmetic_expression, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(195);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,12,_ctx) ) {
			case 1:
				{
				setState(188);
				signed_int();
				}
				break;
			case 2:
				{
				setState(189);
				variable();
				}
				break;
			case 3:
				{
				setState(190);
				float_number();
				}
				break;
			case 4:
				{
				setState(191);
				match(LP);
				setState(192);
				arithmetic_expression(0);
				setState(193);
				match(RP);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(208);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(206);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
					case 1:
						{
						_localctx = new Arithmetic_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic_expression);
						setState(197);
						if (!(precpred(_ctx, 3))) throw new FailedPredicateException(this, "precpred(_ctx, 3)");
						setState(198);
						_la = _input.LA(1);
						if ( !(_la==TIMES || _la==DIV) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(199);
						arithmetic_expression(4);
						}
						break;
					case 2:
						{
						_localctx = new Arithmetic_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic_expression);
						setState(200);
						if (!(precpred(_ctx, 2))) throw new FailedPredicateException(this, "precpred(_ctx, 2)");
						setState(201);
						_la = _input.LA(1);
						if ( !(_la==PLUS || _la==MINUS) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(202);
						arithmetic_expression(3);
						}
						break;
					case 3:
						{
						_localctx = new Arithmetic_expressionContext(_parentctx, _parentState);
						pushNewRecursionContext(_localctx, _startState, RULE_arithmetic_expression);
						setState(203);
						if (!(precpred(_ctx, 1))) throw new FailedPredicateException(this, "precpred(_ctx, 1)");
						setState(204);
						match(MODULO);
						setState(205);
						arithmetic_expression(2);
						}
						break;
					}
					} 
				}
				setState(210);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,14,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public static class Comparison_expressionContext extends ParserRuleContext {
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public TerminalNode EQ() { return getToken(GrammarParser.EQ, 0); }
		public TerminalNode NEQ() { return getToken(GrammarParser.NEQ, 0); }
		public TerminalNode GT() { return getToken(GrammarParser.GT, 0); }
		public TerminalNode ST() { return getToken(GrammarParser.ST, 0); }
		public TerminalNode GET() { return getToken(GrammarParser.GET, 0); }
		public TerminalNode SET() { return getToken(GrammarParser.SET, 0); }
		public Comparison_expressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_comparison_expression; }
	}

	public final Comparison_expressionContext comparison_expression() throws RecognitionException {
		Comparison_expressionContext _localctx = new Comparison_expressionContext(_ctx, getState());
		enterRule(_localctx, 48, RULE_comparison_expression);
		int _la;
		try {
			setState(216);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case RP:
				enterOuterAlt(_localctx, 1);
				{
				}
				break;
			case PLUS:
			case MINUS:
			case LP:
			case UNSIGNED_INT:
			case ID:
			case CHARACTER:
				enterOuterAlt(_localctx, 2);
				{
				setState(212);
				expression();
				setState(213);
				_la = _input.LA(1);
				if ( !((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << EQ) | (1L << NEQ) | (1L << GT) | (1L << ST) | (1L << GET) | (1L << SET))) != 0)) ) {
				_errHandler.recoverInline(this);
				}
				else {
					if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
					_errHandler.reportMatch(this);
					consume();
				}
				setState(214);
				expression();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ConditionContext extends ParserRuleContext {
		public Comparison_expressionContext comparison_expression() {
			return getRuleContext(Comparison_expressionContext.class,0);
		}
		public ConditionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_condition; }
	}

	public final ConditionContext condition() throws RecognitionException {
		ConditionContext _localctx = new ConditionContext(_ctx, getState());
		enterRule(_localctx, 50, RULE_condition);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(218);
			comparison_expression();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 23:
			return arithmetic_expression_sempred((Arithmetic_expressionContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean arithmetic_expression_sempred(Arithmetic_expressionContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 3);
		case 1:
			return precpred(_ctx, 2);
		case 2:
			return precpred(_ctx, 1);
		}
		return true;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3)\u00df\4\2\t\2\4"+
		"\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t"+
		"\13\4\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22"+
		"\4\23\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31\t\31"+
		"\4\32\t\32\4\33\t\33\3\2\3\2\3\2\3\3\3\3\3\3\5\3=\n\3\3\3\3\3\3\4\3\4"+
		"\3\4\5\4D\n\4\3\4\3\4\3\4\3\4\3\5\3\5\3\6\3\6\5\6N\n\6\3\7\3\7\3\b\3\b"+
		"\3\t\3\t\3\t\3\n\3\n\3\n\7\nZ\n\n\f\n\16\n]\13\n\5\n_\n\n\3\13\3\13\3"+
		"\13\3\13\3\13\3\13\5\13g\n\13\3\f\3\f\3\f\3\f\3\r\5\rn\n\r\3\r\3\r\3\r"+
		"\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\17\3"+
		"\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21\3"+
		"\21\3\21\3\22\3\22\7\22\u0093\n\22\f\22\16\22\u0096\13\22\3\22\5\22\u0099"+
		"\n\22\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24\3\24\3\24\3\24"+
		"\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\5\26\u00b2\n\26\3\27"+
		"\7\27\u00b5\n\27\f\27\16\27\u00b8\13\27\3\30\3\30\5\30\u00bc\n\30\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00c6\n\31\3\31\3\31\3\31\3\31"+
		"\3\31\3\31\3\31\3\31\3\31\7\31\u00d1\n\31\f\31\16\31\u00d4\13\31\3\32"+
		"\3\32\3\32\3\32\3\32\5\32\u00db\n\32\3\33\3\33\3\33\4\u0094\u00b6\3\60"+
		"\34\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$&(*,.\60\62\64\2\6\3\2\""+
		"$\3\2\20\21\3\2\16\17\3\2\6\13\2\u00dd\2\66\3\2\2\2\4<\3\2\2\2\6C\3\2"+
		"\2\2\bI\3\2\2\2\nM\3\2\2\2\fO\3\2\2\2\16Q\3\2\2\2\20S\3\2\2\2\22^\3\2"+
		"\2\2\24f\3\2\2\2\26h\3\2\2\2\30m\3\2\2\2\32u\3\2\2\2\34z\3\2\2\2\36\u0082"+
		"\3\2\2\2 \u008b\3\2\2\2\"\u0090\3\2\2\2$\u009a\3\2\2\2&\u00a2\3\2\2\2"+
		"(\u00a8\3\2\2\2*\u00b1\3\2\2\2,\u00b6\3\2\2\2.\u00bb\3\2\2\2\60\u00c5"+
		"\3\2\2\2\62\u00da\3\2\2\2\64\u00dc\3\2\2\2\66\67\5,\27\2\678\7\2\2\38"+
		"\3\3\2\2\29=\7\16\2\2:=\7\17\2\2;=\3\2\2\2<9\3\2\2\2<:\3\2\2\2<;\3\2\2"+
		"\2=>\3\2\2\2>?\7\35\2\2?\5\3\2\2\2@D\7\16\2\2AD\7\17\2\2BD\3\2\2\2C@\3"+
		"\2\2\2CA\3\2\2\2CB\3\2\2\2DE\3\2\2\2EF\7\35\2\2FG\7\33\2\2GH\7\35\2\2"+
		"H\7\3\2\2\2IJ\t\2\2\2J\t\3\2\2\2KN\5\b\5\2LN\7%\2\2MK\3\2\2\2ML\3\2\2"+
		"\2N\13\3\2\2\2OP\7\'\2\2P\r\3\2\2\2QR\7(\2\2R\17\3\2\2\2ST\5\b\5\2TU\5"+
		"\f\7\2U\21\3\2\2\2V[\5\20\t\2WX\7)\2\2XZ\5\20\t\2YW\3\2\2\2Z]\3\2\2\2"+
		"[Y\3\2\2\2[\\\3\2\2\2\\_\3\2\2\2][\3\2\2\2^V\3\2\2\2^_\3\2\2\2_\23\3\2"+
		"\2\2`g\5\30\r\2ag\5\26\f\2bg\5\32\16\2cg\5\"\22\2dg\5$\23\2eg\5*\26\2"+
		"f`\3\2\2\2fa\3\2\2\2fb\3\2\2\2fc\3\2\2\2fd\3\2\2\2fe\3\2\2\2g\25\3\2\2"+
		"\2hi\5\b\5\2ij\5\f\7\2jk\7\32\2\2k\27\3\2\2\2ln\7 \2\2ml\3\2\2\2mn\3\2"+
		"\2\2no\3\2\2\2op\5\b\5\2pq\5\f\7\2qr\7\31\2\2rs\5.\30\2st\7\32\2\2t\31"+
		"\3\2\2\2uv\5\f\7\2vw\7\31\2\2wx\5.\30\2xy\7\32\2\2y\33\3\2\2\2z{\7\3\2"+
		"\2{|\7\25\2\2|}\5\64\33\2}~\7\26\2\2~\177\7\f\2\2\177\u0080\5,\27\2\u0080"+
		"\u0081\7\r\2\2\u0081\35\3\2\2\2\u0082\u0083\7\4\2\2\u0083\u0084\7\3\2"+
		"\2\u0084\u0085\7\25\2\2\u0085\u0086\5\64\33\2\u0086\u0087\7\26\2\2\u0087"+
		"\u0088\7\f\2\2\u0088\u0089\5,\27\2\u0089\u008a\7\r\2\2\u008a\37\3\2\2"+
		"\2\u008b\u008c\7\4\2\2\u008c\u008d\7\f\2\2\u008d\u008e\5,\27\2\u008e\u008f"+
		"\7\r\2\2\u008f!\3\2\2\2\u0090\u0094\5\34\17\2\u0091\u0093\5\36\20\2\u0092"+
		"\u0091\3\2\2\2\u0093\u0096\3\2\2\2\u0094\u0095\3\2\2\2\u0094\u0092\3\2"+
		"\2\2\u0095\u0098\3\2\2\2\u0096\u0094\3\2\2\2\u0097\u0099\5 \21\2\u0098"+
		"\u0097\3\2\2\2\u0098\u0099\3\2\2\2\u0099#\3\2\2\2\u009a\u009b\7\5\2\2"+
		"\u009b\u009c\7\25\2\2\u009c\u009d\5\64\33\2\u009d\u009e\7\26\2\2\u009e"+
		"\u009f\7\f\2\2\u009f\u00a0\5,\27\2\u00a0\u00a1\7\r\2\2\u00a1%\3\2\2\2"+
		"\u00a2\u00a3\5\n\6\2\u00a3\u00a4\5\f\7\2\u00a4\u00a5\7\25\2\2\u00a5\u00a6"+
		"\5\22\n\2\u00a6\u00a7\7\26\2\2\u00a7\'\3\2\2\2\u00a8\u00a9\5&\24\2\u00a9"+
		"\u00aa\7\f\2\2\u00aa\u00ab\5,\27\2\u00ab\u00ac\7\r\2\2\u00ac)\3\2\2\2"+
		"\u00ad\u00b2\5(\25\2\u00ae\u00af\5&\24\2\u00af\u00b0\7\32\2\2\u00b0\u00b2"+
		"\3\2\2\2\u00b1\u00ad\3\2\2\2\u00b1\u00ae\3\2\2\2\u00b2+\3\2\2\2\u00b3"+
		"\u00b5\5\24\13\2\u00b4\u00b3\3\2\2\2\u00b5\u00b8\3\2\2\2\u00b6\u00b7\3"+
		"\2\2\2\u00b6\u00b4\3\2\2\2\u00b7-\3\2\2\2\u00b8\u00b6\3\2\2\2\u00b9\u00bc"+
		"\5\60\31\2\u00ba\u00bc\5\16\b\2\u00bb\u00b9\3\2\2\2\u00bb\u00ba\3\2\2"+
		"\2\u00bc/\3\2\2\2\u00bd\u00be\b\31\1\2\u00be\u00c6\5\4\3\2\u00bf\u00c6"+
		"\5\f\7\2\u00c0\u00c6\5\6\4\2\u00c1\u00c2\7\25\2\2\u00c2\u00c3\5\60\31"+
		"\2\u00c3\u00c4\7\26\2\2\u00c4\u00c6\3\2\2\2\u00c5\u00bd\3\2\2\2\u00c5"+
		"\u00bf\3\2\2\2\u00c5\u00c0\3\2\2\2\u00c5\u00c1\3\2\2\2\u00c6\u00d2\3\2"+
		"\2\2\u00c7\u00c8\f\5\2\2\u00c8\u00c9\t\3\2\2\u00c9\u00d1\5\60\31\6\u00ca"+
		"\u00cb\f\4\2\2\u00cb\u00cc\t\4\2\2\u00cc\u00d1\5\60\31\5\u00cd\u00ce\f"+
		"\3\2\2\u00ce\u00cf\7\22\2\2\u00cf\u00d1\5\60\31\4\u00d0\u00c7\3\2\2\2"+
		"\u00d0\u00ca\3\2\2\2\u00d0\u00cd\3\2\2\2\u00d1\u00d4\3\2\2\2\u00d2\u00d0"+
		"\3\2\2\2\u00d2\u00d3\3\2\2\2\u00d3\61\3\2\2\2\u00d4\u00d2\3\2\2\2\u00d5"+
		"\u00db\3\2\2\2\u00d6\u00d7\5.\30\2\u00d7\u00d8\t\5\2\2\u00d8\u00d9\5."+
		"\30\2\u00d9\u00db\3\2\2\2\u00da\u00d5\3\2\2\2\u00da\u00d6\3\2\2\2\u00db"+
		"\63\3\2\2\2\u00dc\u00dd\5\62\32\2\u00dd\65\3\2\2\2\22<CM[^fm\u0094\u0098"+
		"\u00b1\u00b6\u00bb\u00c5\u00d0\u00d2\u00da";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}