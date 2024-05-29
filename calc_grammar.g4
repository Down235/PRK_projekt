grammar calc_grammar;

// PARSER RULES

syntax
    : expr EOF
    ;

expr
    : term (PLUS term)*
    ;

term
    : factor (MLPLY factor)*
    ;

factor
    : LPAREN expr RPAREN
    | nmr
    ;

nmr
    : ZERO (COMMA digits)?
    | digits (COMMA digits)?
    | inv
    | log
    ;

inv
    : InvStart expr RPAREN
    ;

log
    : LogStart expr RPAREN
    ;

digits
    : digit+
	;

digit
    : ZERO
    | NonZeroD
    ;

// LEXER RULES

COMMA : ',' ;

LPAREN : '(' ;
RPAREN : ')' ;

PLUS : '+' ;
MLPLY : '*' ;

ZERO : [0] ;
NonZeroD : [1-9] ;

InvStart : 'inv(' ;
LogStart : 'log(' ;

WS : [ \t\r\n]+ -> skip ;