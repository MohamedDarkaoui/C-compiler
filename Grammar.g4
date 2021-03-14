grammar Grammar;

startRule: statement* EOF;


PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
MODULO: '%';
LP: '(';
RP: ')';
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
types: INT | CHAR | FLOAT;
ID: [_a-zA-Z][_a-zA-Z0-9]*;
variable: ID;
CHARACTER: '\'' . '\'';

statement: definition | declaration | assignment | comment;
declaration: types (TIMES|AMPERSAND)? variable SEMICOLON;
definition: CONST? types (TIMES|AMPERSAND)? variable ASSIGN  expression SEMICOLON;
assignment: (TIMES|AMPERSAND)? variable ASSIGN expression SEMICOLON;


expression: arithmetic_expression | character;
arithmetic_expression:
    signed_int
    | (TIMES|AMPERSAND)? variable
    | float_number
    | LP arithmetic_expression RP
    | arithmetic_expression (TIMES | DIV) arithmetic_expression
    | arithmetic_expression (PLUS|MINUS) arithmetic_expression
    | arithmetic_expression MODULO arithmetic_expression;