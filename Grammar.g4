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
signed_int: (PLUS | MINUS |) UNSIGNED_INT;
UNSIGNED_INT: [0-9]+;
float_number: (PLUS | MINUS |) UNSIGNED_INT POINT UNSIGNED_INT;
DIGIT: [0-9];
WS: [ \n\t\r]+ -> skip;
CONST: 'const';
UNDERSCORE: '_';
INT: 'int';
CHAR: 'char';
FLOAT: 'float';
VOID: 'void';
RETURN: 'return';
types: INT | CHAR | FLOAT;
function_types: types | VOID;
ID: [_a-zA-Z][_a-zA-Z0-9]*;
variable: ID index*?;
noIndexVariable: ID;
CHARACTER: '\'' . '\'';
character : CHARACTER;
COMMA: ',';
arg: types variable;
arguments : ((arg) (COMMA arg)*)?;
parameters: ((expression) (COMMA expression)*)?;
index : LSB UNSIGNED_INT RSB;


statement: definition | declaration | assignment | selection_sequence | while_statement | 
function_definition | for_statement | unnamed_scope | break_statement | continue_statement | function_call SEMICOLON | return_statement;


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