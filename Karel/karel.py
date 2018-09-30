import ply.lex as lex

tokens = [
     'CONDICIONALSINO','ENTONCES','APAGARSE','MIENTRAS',
     'POR','DIVIDE','COMANDO','MAS','NUMERO','CONDICIONALSI'
     ,'OPERADORY','OPERADORO','OPERADORNO','HACER','GUION','COMMENT','REPETIR',
     'TANTASVECES']

t_ignore = ' \t'
t_ignore_GUION= r'-'
t_ignore_COMMENT = r'\#.*'
t_MAS = r'\+'
t_POR = r'\*'
t_DIVIDE = r'/'
t_COMANDO = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_NUMERO(t):
    r'\d+'
    t.value = int(t.value)
    return t
def t_HACER(t):
    r'hacer'
    return t
def t_CONDICIONALSINO(t):
    r'sino'
    return t

def t_CONDICIONALSI(t):
    r'si'
    return t
def t_ENTONCES(t):
    r'entonces'
    return t
def t_APAGARSE(t):
    r'apagate'
    return t
def t_MIENTRAS(t):
    r'mientras'
    return t
def t_OPERADORY(t):
    r'y'
    return t
def t_OPERADORO(t):
    r'mientras'
    return t
def t_OPERADORNO(t):
    r'mientras'
    return t
def t_REPETIR(t):
    r'repetir'
    return t
def t_TANTASVECES(t):
    r'veces'
    return t


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lex.lex() # Build the lexer

f = open ('karel.txt' , 'r')

message = f.read()

f.close()

lex.input(message)
while True:
    tok = lex.token()
    if not tok: break
    print str(tok.value) + " - " + str(tok.type)
