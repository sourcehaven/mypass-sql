SELECT = 'SELECT'
def t_SELECT(t):
    r'SELECT'
    return t


INSERT = 'INSERT'
def t_INSERT(t):
    r'INSERT|INSERT\s+INTO'
    return t


UPDATE = 'UPDATE'
def t_UPDATE(t):
    r'UPDATE'
    return t


DELETE = 'DELETE'
def t_DELETE(t):
    r'DELETE|DELETE\s+FROM'
    return t


TRUNCATE = 'TRUNCATE'
def t_TRUNCATE(t):
    r'TRUNCATE|TRUNCATE\s+TABLE'
    return t


AND = 'AND'
def t_AND(t):
    r'AND|&'
    return t


OR = 'OR'
def t_OR(t):
    r'OR|\|'
    return t


SET = 'SET'
def t_SET(t):
    r'SET'
    return t


FROM = 'FROM'
def t_FROM(t):
    r'FROM'
    return t


WHERE = 'WHERE'
def t_WHERE(t):
    r'WHERE'
    return t


ORDER_BY = 'ORDER_BY'
def t_ORDER_BY(t):
    r'ORDER\s+BY'
    return t


ASCENDING = 'ASCENDING'
def t_ASCENDING(t):
    r'ASC|ASCENDING|↑|⇧|⇑'
    return t


DESCENDING = 'DESCENDING'
def t_DESCENDING(t):
    r'DESC|DESCENDING|↓|⇩|⇓'
    return t


COMMA = 'COMMA'
t_COMMA = r','

DOT = 'DOT'
t_DOT = r'\.'

SEMICOLON = 'SEMICOLON'
t_SEMICOLON = r';'

EQUALS = 'EQUALS'
t_EQUALS = r'='

LEFT_PARENTHESIS = 'LEFT_PARENTHESIS'
t_LEFT_PARENTHESIS = r'\('

RIGHT_PARENTHESIS = 'RIGHT_PARENTHESIS'
t_RIGHT_PARENTHESIS = r'\)'

TIMES = 'TIMES'
t_TIMES = r'\*'


LITERAL = 'LITERAL'
def t_LITERAL(t):
    r'(\d*\.\d+|\d+\.\d*|\d+|"[^"]*"|\'[^\']*\'|True|False)'
    if t.value.isdigit():
        t.value = int(t.value)
    elif '.' in t.value:
        t.value = float(t.value)
    elif t.value.lower() == 'true':
        t.value = True
    elif t.value.lower() == 'false':
        t.value = False
    else:
        t.value = t.value[1:-1]
    return t


IDENTIFIER = 'IDENTIFIER'
def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
