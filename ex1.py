'''
PROGRAM → STATEMENT |  FUNCLIST | ε 
FUNCLIST → FUNCDEF FUNCLIST1
FUNCLIST1 → FUNCLIST | ε 
FUNCDEF → def ident ( PARAMLIST ){STATELIST} 
TYPE → int | float | string 

PARAMLIST → TYPE ident PARAMLIST1 | ε 
PARAMLIST1 → , PARAMLIST | ε 

STATEMENT → VARDECL ; | 
ATRIBSTAT ; | 
PRINTSTAT ; | 
READSTAT ; | 
RETURNSTAT ; | 
IFSTAT | 
FORSTAT | 
{STATELIST} | 
break; | ; 

VARDECL → TYPE ident ARRAY1 
ARRAY1 → [int_constant] | ε 

ATRIBSTAT → LVALUE = ATRIB 
ATRIB → EXPRESSION | FUNCCALL | ALLOCEXPRESSION 
FUNCCALL → ident(PARAMLISTCALL)
PARAMLISTCALL → ident PARAMLISTCALL1 | ε 
PARAMLISTCALL1 → , PARAMLISTCALL | ε 
PRINTSTAT → print EXPRESSION 
READSTAT → read LVALUE

RETURNSTAT → return RETURNSTAT1
RETURNSTAT1 → ident | ε 
LVALUE → ident OPT_NUMEXPRESSION
OPT_NUMEXPRESSION → [NUMEXPRESSION] | ε

IFSTAT → if(EXPRESSION) STATEMENT IFSTAT1 
IFSTAT1 → else STATEMENT | ε

FORSTAT → for(ATRIBSTAT; EXPRESSION; ATRIBSTAT)STATEMENT

STATELIST → STATEMENT STATELIST1
STATELIST1 → STATELIST | ε

ALLOCEXPRESSION → new TYPE [ NUMEXPRESSION ]
NUMEXPRESSION → TERM NUMEXPRESSION1 
NUMEXPRESSION1 → OP1 TERM | ε
OP1 → + | -
OP2 → * | / | %
TERM → UNARYEXPR TERM1
TERM1 → OP2 UNARYEXPR | ε
 FACTOR → int_constant | 
float_constant | 
string_constant | 
null |
LVALUE |
(NUMEXPRESSION)
UNARYEXPR → OP_FACTOR FACTOR
OP_FACTOR → OP1 | ε

EXPRESSION → NUMEXPRESSION OPT_EXPRESSION
OPT_EXPRESSION → OP NUMEXPRESSION | ε
OP → < | > | <= | >= | == | !=

'''



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
    'int_constant': 'INT_CONSTANT',
    'float_constant':'FLOAT_CONSTANT', 
    'string_constant':'STRING_CONSTANT', 
    'null' :'NULL'
 }


tokens = ['IDENT'] + list(reserved.values())

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
import ply.lex as lex
lexer = lex.lex()



#analise sintatica

# precedence = (
#     ("left", "'<'", "'<' '=' ", "'>'", "'>' '=' "),
#     ("left", "'+'", "'-'"),
#     ("left", "'*'", "'/'"),
#     ("left", "'('", "')'"),
# )

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
    """FUNCDEF : DEF IDENT '(' PARAMLIST ')' '[' STATELIST ']'"""  # noqa
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
    | '[' STATELIST ']'
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

# def p_error(token: lex.LexToken):
#         print(f"Erro de sintaxe! Token: {token.type}; Linha: {token.lineno}")

erros_sin = []
def p_error(p):
    if p:
        erros_sin.append("Syntax error at '%s' \n" % p.value)
    else:
        erros_sin.append("Syntax error at EOF")

# def p_program(p):
#     '''program : statement
#                 | funclist
#                 | empty'''
        
# def p_funclist(p):
#     '''funclist : funcdef funclist1'''

# def p_funclist1(p):
#     '''funclist1 : funclist
#                 | empty'''

# def p_funcdef(p):
#     '''funcdef : DEF IDENT '(' paramlist ')' '{' statelist '}' '''

# def p_type(p):
#     '''type : INT 
#                 | FLOAT
#                 | STRING'''

# def p_paramlist(p):
#     '''paramlist : type IDENT paramlist1
#                 | empty'''

# def p_paramlist1(p):
#     '''paramlist1 : ',' paramlist
#                 | empty'''

# def p_statement(p):
#     '''statement : vardecl ';'
#                 | atribstat ';'
#                 | printstat ';'
#                 | readstat ';'
#                 | returnstat ';'
#                 | ifstat
#                 | forstat
#                 | '{' statelist '}'
#                 | BREAK ';'
#                 | ';' '''   

# def p_vardecl(p):
#     '''vardecl : type IDENT array1'''  

# def p_array1(p):
#     '''array1 : '[' INT_CONSTANT ']' 
#                 | empty''' 

# def p_atribstat(p):
#     '''atribstat : lvalue '=' atrib'''

# def p_atrib(p):
#     '''atrib : expression 
#                 | funccall
#                 | allocexpression'''

# def p_funccall(p):
#     '''funccall : IDENT '(' paramlistcall ')' '''

# def p_paramlistcall(p):
#     '''paramlistcall : IDENT paramlistcall1
#                 | empty'''

# def p_paramlistcall1(p):
#     '''paramlistcall1 : ',' paramlistcall 
#                 | empty'''
                
# def p_printstat(p):
#     '''printstat : PRINT expression '''

# def p_readstat(p):
#     '''readstat : READ lvalue '''

# def p_returnstat(p):
#     '''returnstat : RETURN returnstat1'''

# def p_returnstat1(p):
#     '''returnstat1 : IDENT
#                 | empty'''

# def p_lvalue(p):
#     '''lvalue : IDENT opt_numexpression'''

# def p_opt_numexpression(p):
#     '''opt_numexpression : '[' numexpression ']'
#                 | empty'''

# def p_ifstat(p):
#     '''ifstat : IF '(' expression ')' statement ifstat1
#                 | empty'''

# def p_ifstat1(p):
#     '''ifstat1 : ELSE statement 
#                 | empty'''

# def p_forstat(p):
#     '''forstat : FOR '(' atribstat ';' expression ';' atribstat ')' statement
#                 | empty'''

# def p_statelist(p):
#     '''statelist : statement statelist1
#                 | empty'''


# def p_statelist1(p):
#     '''statelist1 : statelist
#                 | empty'''

# def p_op1(p):
#     '''op1 : '+'
#                 | '-' '''

# def p_op2(p):
#     '''op2 : '*'
#                 | '/' 
#                 | '%' '''

# def p_op(p):
#     '''op : '<' 
#                 | '>' 
#                 | '<' '=' 
#                 | '>' '=' 
#                 | '=' '='
#                 | '!' '=' '''

# def p_allocexpression(p):
#     '''allocexpression : NEW type '[' numexpression ']' '''

# def p_numexpression(p):
#     '''numexpression : term numexpression1'''

# def p_numexpression1(p):
#     '''numexpression1 : op1 term
#                 | empty'''

# def p_term(p):
#     '''term : unaryexpr term1'''

# def p_term1(p):
#     '''term1 : op2 unaryexpr
#                 | empty'''

# def p_factor(p):
#     '''factor : INT_CONSTANT
#                 | FLOAT_CONSTANT
#                 | STRING_CONSTANT
#                 | NULL
#                 | lvalue
#                 | '(' numexpression ')' '''                             

# def p_unaryexpr(p):
#     '''unaryexpr : op_factor factor'''

# def p_op_factor(p):
#     '''op_factor : op1
#                 | empty'''

# def p_expression(p):
#     '''expression : numexpression opt_expression '''

# def p_opt_expression(p):
#     '''opt_expression : op numexpression
#                 | empty'''


# def p_empty(p):
#     'empty : '
#     pass

# erros_sin = []
# def p_error(p):
#     if p:
#         erros_sin.append("Syntax error at '%s' \n" % p.value)
#     else:
#         erros_sin.append("Syntax error at EOF")
        

import ply.yacc as yacc
parser = yacc.yacc()
 


while True:
    try:
        s = input('cod > ')
    except EOFError:
        break
    if not s: continue
    #analise lexica
    lexer.input(s)
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
        result = parser.parse(s)
        if len(erros_sin) == 0:
            print("Compilado sem erros.")
        else:
            print("Erros sintaticos = '%d'" % len(erros_sin))
            for err in erros_sin:
                print(err)    