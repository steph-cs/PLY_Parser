#analise lexica
reserved = {
    'def' : 'DEF' ,
    'int' : 'INT', 
    'float' : 'FLOAT', 
    'string' : 'STRING', 
    'break' : 'BREAK', 
    'print' : 'PRINT', 
    'read' : 'READ', 
    'return' : 'RETURN', 
    'if' : 'IF', 
    'else' : 'ELSE', 
    'for' : 'FOR', 
    'new' : 'NEW', 
    'null' :'NULL'
 }


tokens = ['IDENT', 'INT_CONSTANT', 'FLOAT_CONSTANT','STRING_CONSTANT'] + list(reserved.values())

literals = ['=', '<', '>', '!', '+', '-', '*', '/','%' , '(', ')', '[', ']', '{', '}' ,';', ',']

def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENT')    # Check for reserved words
    return t

t_INT_CONSTANT = r'[0-9]+'
t_FLOAT_CONSTANT = r'[0-9]+.[0-9]+'
t_STRING_CONSTANT = r'\"([^\\\"]|\\.)*\"'


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")



erros_lex = []
def t_error(t):
    erros_lex.append("Illegal character '%s'" % t.value[0])
    #print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
from ast import Return
import ply.lex as lex
lexer = lex.lex()


#analise sintatica

def p_PROGRAM(p):
    """PROGRAM : STATEMENT
    | FUNCLIST
    | EMPTY"""
    pass

def p_FUNCLIST(p):
    """FUNCLIST : FUNCDEF FUNCLIST_2"""
    pass

def p_FUNCLIST_2(p):
    """FUNCLIST_2 : FUNCLIST
    | EMPTY"""
    pass

def p_FUNCDEF(p):
    """FUNCDEF : DEF IDENT '(' PARAMLIST ')' '{' STATELIST '}' """  # noqa
    pass

def p_PARAMLIST(p):
    """PARAMLIST : PARAMLIST_2
    | EMPTY"""
    pass

def p_PARAMLIST_2(p):
    """PARAMLIST_2 : INT_OR_FLOAT_OR_STRING IDENT PARAMLIST_3"""
    pass

def p_INT_OR_FLOAT_OR_STRING(p):
    """INT_OR_FLOAT_OR_STRING : INT
    | FLOAT
    | STRING"""
    pass

def p_PARAMLIST_3(p):
    """PARAMLIST_3 : ',' PARAMLIST
    | EMPTY"""
    pass

def p_STATEMENT(p):
    """STATEMENT : VARDECL ';'
    | ATRIBSTAT ';'
    | PRINTSTAT ';'
    | READSTAT ';'
    | RETURNSTAT ';'
    | IFSTAT
    | FORSTAT
    | '{' STATELIST '}'
    | BREAK ';'
    | ';'"""
    pass

def p_VARDECL(p):
    """VARDECL : INT_OR_FLOAT_OR_STRING IDENT VARDECL_2"""
    pass

def p_VARDECL_2(p):
    """VARDECL_2 : '[' INT_CONSTANT ']' VARDECL_2
    | EMPTY"""
    pass

def p_ATRIBSTAT(p):
    """ATRIBSTAT : LVALUE '=' ATRIBSTAT_2"""
    pass

def p_ATRIBSTAT_2(p):
    """ATRIBSTAT_2 : FUNCCALL_EXPRESSION
    | ALLOCEXPRESSION"""
    pass

def p_FUNCCALL_EXPRESSION(p):
    """FUNCCALL_EXPRESSION : '+' FACTOR TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | '-' FACTOR TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | INT_CONSTANT TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | FLOAT_CONSTANT TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | STRING_CONSTANT TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | NULL TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | '(' NUMEXPRESSION ')' TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | FUNCCALL"""  # noqa
    pass

def p_FUNCCALL(p):
    """FUNCCALL : IDENT FUNCCALL_2"""
    pass

def p_FUNCCALL_2(p):
    """FUNCCALL_2 : ALLOCEXPRESSION_2 TERM_2 NUMEXPRESSION_2 EXPRESSION_2
    | '(' PARAMLISTCALL ')'"""

def p_PARAMLISTCALL(p):
    """PARAMLISTCALL : IDENT PARAMLISTCALL_2
    | EMPTY"""
    pass

def p_PARAMLISTCALL_2(p):
    """PARAMLISTCALL_2 : ',' PARAMLISTCALL
    | EMPTY"""
    pass

def p_PRINTSTAT(p):
    """PRINTSTAT : PRINT EXPRESSION"""
    pass

def p_READSTAT(p):
    """READSTAT : READ LVALUE"""
    pass

def p_RETURNSTAT(p):
    """RETURNSTAT : RETURN"""
    pass

def p_IFSTAT(p):
    """IFSTAT : IF '(' EXPRESSION ')' STATEMENT IFSTAT_2"""  # noqa
    pass

def p_IFSTAT_2(p):
    """IFSTAT_2 : ELSE STATEMENT
    | EMPTY"""
    pass

def p_FORSTAT(p):
    """FORSTAT : FOR '(' ATRIBSTAT ';' EXPRESSION ';' ATRIBSTAT ')' STATEMENT"""  # noqa
    pass

def p_STATELIST(p):
    """STATELIST : STATEMENT STATELIST_2"""
    pass

def p_STATELIST_2(p):
    """STATELIST_2 : STATELIST
    | EMPTY"""
    pass

def p_ALLOCEXPRESSION(p):
    """ALLOCEXPRESSION :  NEW INT_OR_FLOAT_OR_STRING '[' NUMEXPRESSION ']' ALLOCEXPRESSION_2"""  # noqa
    pass

def p_ALLOCEXPRESSION_2(p):
    """ALLOCEXPRESSION_2 : '[' NUMEXPRESSION ']' ALLOCEXPRESSION_2
    | EMPTY"""  # noqa
    pass

def p_EXPRESSION(p):
    """EXPRESSION : NUMEXPRESSION EXPRESSION_2"""
    pass

def p_EXPRESSION_2(p):
    """EXPRESSION_2 : COMPAREOPERANDS NUMEXPRESSION
    | EMPTY"""
    pass

def p_COMPAREOPERANDS(p):
    """COMPAREOPERANDS : '<'
    | '>'
    | '<' '=' 
    | '>' '=' 
    | '=' '='
    | '!' '='"""
    pass

def p_NUMEXPRESSION(p):
    """NUMEXPRESSION : TERM NUMEXPRESSION_2"""
    pass

def p_NUMEXPRESSION_2(p):
    """NUMEXPRESSION_2 : NUMEXPRESSION_3 TERM NUMEXPRESSION_2
    | EMPTY"""
    pass

def p_NUMEXPRESSION_3(p):
    """NUMEXPRESSION_3 : '+'
    | '-'"""
    pass

def p_TERM(p):
    """TERM : UNARYEXPRESSION TERM_2"""
    pass

def p_TERM_2(p):
    """TERM_2 : MULT_OR_DIV_OR_MOD TERM
    | EMPTY"""
    pass

def p_MULT_OR_DIV_OR_MOD(p):
    """MULT_OR_DIV_OR_MOD : '*'
    | '/'
    | '%'"""
    pass

def p_UNARYEXPRESSION(p):
    """UNARYEXPRESSION : NUMEXPRESSION_3 FACTOR
    | FACTOR"""
    pass

def p_FACTOR(p):
    """FACTOR : INT_CONSTANT
    | FLOAT_CONSTANT
    | STRING_CONSTANT
    | NULL
    | LVALUE
    | '(' NUMEXPRESSION ')'"""
    pass

def p_LVALUE(p):
    """LVALUE : IDENT ALLOCEXPRESSION_2"""
    pass

def p_EMPTY(p):
    """EMPTY :"""
    pass

erros_sin = []
def p_error(p):
    if p:
        erros_sin.append("Syntax error at '%s'" % p.value)
    else:
        erros_sin.append("Syntax error at EOF")

import ply.yacc as yacc
parser = yacc.yacc()


import sys
if len(sys.argv) < 2:
    print("Erro: arquivo lcc necessário como argumento")
    quit()

erros_lex = []
f = open(sys.argv[1], "r")
file_content = f.read()

lexer.input(file_content)
while True:
    tok = lexer.token()
    if not tok:
        break
    print(tok)
print("Erros lexicos = '%d'" % len(erros_lex))
for err in erros_lex:
    print(err)
#se n houver erros lexicos -> analise sintatica
if len(erros_lex) == 0:
    #analise sintatica
    result = parser.parse(file_content)
    if len(erros_sin) == 0:
        print("Compilado sem erros.")
    else:
        print("Erros sintaticos = '%d'" % len(erros_sin))
        for err in erros_sin:
            print(err)