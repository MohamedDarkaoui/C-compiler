grammar Grammar;

startRule: block EOF;




IF: 'if';
ELSE: 'else';
WHILE: 'while';
FOR: 'for';
BREAK: 'break';
CONTINUE: 'continue';
EQ: '==';
NEQ: '!=';
GT: '>';
ST: '<';
GET: '>=';
SET: '<=';
LB: '{';
RB: '}';
LSB: '[';
RSB: ']';
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
MODULO: '%';
BC: '/*';
EC: '*/';
LP: '(';
RP: ')';
COMMENT1:'/*' .*? '*/' -> skip;
COMMENT2:'//' .*? '\n' -> skip;
ASSIGN: '=';
SEMICOLON: ';';
POINT: '.';
AMPERSAND: '&';
UNSIGNED_INT: [0-9]+;
DIGIT: [0-9];
WS: [ \n\t\r]+ -> skip;
CONST: 'const';
UNDERSCORE: '_';
INT: 'int';
CHAR: 'char';
FLOAT: 'float';
VOID: 'void';
RETURN: 'return';
PRINTF: 'printf';
STDIO: '#include <stdio.h>';
CODE: '"%d"' | '"%i"'| '"%s"'| '"%f"' | '"%c"';
STRING: '"' .*? '"';
ID: [_a-zA-Z][_a-zA-Z0-9]*;
CHARACTER: '\'' . '\'';
COMMA: ',';



printf: PRINTF LP CODE COMMA (expression|string) RP SEMICOLON; 
string: STRING;
signed_int: (PLUS | MINUS |) UNSIGNED_INT;
float_number: (PLUS | MINUS |) UNSIGNED_INT POINT UNSIGNED_INT;
types: INT | CHAR | FLOAT;
function_types: types | VOID;
variable: ID index*?;
noIndexVariable: ID;
character : CHARACTER;
arg: types variable;
arguments : ((arg) (COMMA arg)*)?;
parameters: ((expression) (COMMA expression)*)?;
index : LSB UNSIGNED_INT RSB;


statement: definition | declaration | assignment | selection_sequence | while_statement | stdio | printf |
function_definition | for_statement | unnamed_scope | break_statement | continue_statement | function_call SEMICOLON | return_statement;

stdio: STDIO;
declaration: types variable SEMICOLON;
definition: CONST? types  variable ASSIGN  expression SEMICOLON | CONST? types  variable ASSIGN array_initializator SEMICOLON;
assignment:  variable ASSIGN expression SEMICOLON;
for_assignment: variable ASSIGN expression;
if_statement: IF LP condition RP LB block RB;
else_if_statement: ELSE IF LP condition RP LB block RB;
else_statement: ELSE LB block RB;
selection_sequence: if_statement else_if_statement*? else_statement?;
while_statement: WHILE LP condition RP LB block RB;
function_definition: function_types noIndexVariable LP arguments RP LB block RB;
function_call: noIndexVariable LP parameters RP;
break_statement: BREAK SEMICOLON;
continue_statement: CONTINUE SEMICOLON;
return_statement: RETURN expression? SEMICOLON;
for_statement: FOR LP (definition|assignment) condition SEMICOLON for_assignment RP LB block RB;
array_initializator: LB (expression (COMMA expression)*)? RB;


block: statement*?;
unnamed_scope: LB statement*? RB;


expression: arithmetic_expression | character;
arithmetic_expression:
    signed_int
    | function_call
    | variable
    | float_number
    | LP arithmetic_expression RP
    | arithmetic_expression (TIMES | DIV) arithmetic_expression
    | arithmetic_expression (PLUS|MINUS) arithmetic_expression
    | arithmetic_expression MODULO arithmetic_expression;

comparison_expression:
    | expression (EQ | NEQ | GT | ST | GET | SET) expression;


condition: comparison_expression;