grammar Grammar;

startRule: expression* EOF;


PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
MODULO: '%';

LP: '(';
RP: ')';
SEMICOLON: ';';
signed_int: (PLUS | MINUS |) UNSIGNED_INT;
UNSIGNED_INT: [0-9]+;
WS: [ \n\t\r]+ -> skip;


expression: arithmetic_expression SEMICOLON;

arithmetic_expression :
    signed_int
    | LP arithmetic_expression RP
    | arithmetic_expression (TIMES | DIV) arithmetic_expression
    | arithmetic_expression (PLUS|MINUS) arithmetic_expression
    | arithmetic_expression MODULO arithmetic_expression;

