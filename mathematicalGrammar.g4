grammar mathematicalGrammar;

startRule: arithmetic_expression SEMICOLON | conditional_expression SEMICOLON | logical_expression SEMICOLON;
PLUS: '+';
MINUS: '-';
TIMES: '*';
DIV: '/';
MODULO: '%';

GT: '>';
ST: '<';
GET: '>=';
SET: '<=';
EQ: '==';
NEQ: '!=';

OR: '||';
AND: '&&';
NOT: '!';

LP: '(';
RP: ')';
SEMICOLON: ';';
INT: [0-9]+;
WS: [ \n\t\r]+ -> skip;


arithmetic_expression :
    INT
    | arithmetic_expression (PLUS | MINUS) arithmetic_expression
    | arithmetic_expression (TIMES | DIV) arithmetic_expression
    | arithmetic_expression MODULO arithmetic_expression
    | LP arithmetic_expression RP;

conditional_expression :
    arithmetic_expression
    | conditional_expression (GT | ST) conditional_expression
    | conditional_expression (GET | SET) conditional_expression
    | conditional_expression (EQ | NEQ) conditional_expression
    | LP conditional_expression RP;

logical_expression :
    conditional_expression
    | logical_expression OR logical_expression
    | logical_expression AND logical_expression
    | NOT logical_expression
    | LP logical_expression RP;


