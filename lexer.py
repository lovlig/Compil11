from ply import lex


reserved = {
        'def':'DEF',
        'return':'RETURN',
        'and':'AND',
        'or':'OR',
        'not':'NOT',
        'print':'PRINT',
        'while':'WHILE',
        'if':'IF',
        'break':'BREAK',
        'continue':'CONTINUE',
        'int':'INT',
        'real':'REAL',
        'boolean':'BOOLEAN',
        'vars':'VARS',
        'str':'STRING'
}

tokens = list(reserved.values()) + [
        'RAVNO',
        'DP',
        'CM',
        'OP',
        'CP',
        'OF',
        'CF',
        'PRISV',
        'SC',
        'SUM',
        'SUB',
        'MUL',
        'DIV',
        'MORE',
        'LESS',
        'NUMBER_INT',
        'NUMBER_REAL',
        'ID',
        ]



t_DP = r'\:'
t_RAVNO = r'\='
t_PRINT = r'print'
t_OP = r'\('
t_CP = r'\)'
t_CM = r'\,'
t_OF = r'\{'
t_CF = r'\}'
t_PRISV = r'\:='
t_SC = r'\;'
t_SUM = r'\+'
t_SUB = r'\-'
t_MUL = r'\*'
t_DIV = r'\/'
t_MORE = r'\>'
t_LESS = r'\<'
t_NUMBER_INT = r'\d+'
t_NUMBER_REAL = r'\d+\.\d+'
t_STRING = r'\"[^\'\n]*\"'


def t_comment(t):
    r'/\*([^*]|[\r\n]|(\*+([^*/]|[\r\n])))*\*+/'
    pass



def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t



def t_newline(t):
    r'\n+'
    t.lineno += len(t.value)




t_ignore  = ' \t'




def t_error(t):
    print ("Недопустимый символ '%s'" % t.value[0])



lex.lex()



