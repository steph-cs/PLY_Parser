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
def p_statement_func_null(p):
    "func : DEF IDENT '(' ')' "
    
def p_statement_func(p):
    "func : DEF IDENT '(' expression ')' "
  
def p_expression_params(p):
    '''expression : IDENT ',' expression
                    | NUMBER ',' expression'''
   

def p_expression_id(p):
    '''expression : IDENT 
                    | NUMBER '''


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