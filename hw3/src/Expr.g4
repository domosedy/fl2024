grammar Expr;

start: expr EOF;


expr: atom #atomExpr
    | expr expr #connectExpr
    | left=expr op='|' right=expr #orExpr
    | atom '+' #plusExpr
    | atom '*' #starExpr
    | atom '?' #askExpr
    ;

atom: CHAR #charExpr
    | '(' expr ')' #parenExpr
    ;

CHAR: [a-zA-Z];
WS: [\t\r\n]+ -> skip;