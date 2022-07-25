'''
PROGRAM → STATEMENT |  FUNCLIST | ε 
FUNCLIST → FUNCDEF FUNCLIST1
FUNCLIST1 → FUNCLIST | ε 
FUNCDEF → def ident ( PARAMLIST STATELIST1 ){STATELIST} 
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

RETURNSTAT → return RETURNSTAT1 LVALUE
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
    'string_constante':'STRING_CONSTANT', 
    'null' :'NULL'

 }
 
tokens = ['IDENT', 'NUMBER'] + list(reserved.values())

literals = ['=', '<', '>', '!', '+', '-', '*', '/','%' , '(', ')', '[', ']', ';', ',']
 
def t_IDENT(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENT')    # Check for reserved words
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)    
    return t

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
def p_program(p):
    '''program : statement 
                | funclist
                | '''

def p_funclist(p):
    '''funclist : funcdef funclist1'''

def p_funclist1(p):
    '''funclist1 : funclist
                    | '''

def p_funcdef(p):
    '''funcdef : DEF IDENT '(' paramlist ')' '{' statelist1 '}' '''

def p_type(p):
    '''ifstat1 : INT 
                | FLOAT
                | STRING'''

def p_ifstat(p):
    '''ifstat1 : IF '(' expression ')' statement ifstat1
                | '''

def p_ifstat1(p):
    '''ifstat1 : ELSE statement 
                | '''

def p_forstat(p):
    '''forstat : FOR '(' atribstat ';' expression ';' atribstat ')' statement
                    | '''

def p_statelist(p):
    '''statelist : statement statelist1
                    | '''

def p_statelist1(p):
    '''statelist1 : statelist
                    | '''
                             


erros_sin = []
def p_error(p):
    if p:
        erros_sin.append("Syntax error at '%s' \n" % p.value)
    else:
        erros_sin.append("Syntax error at EOF")
        

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