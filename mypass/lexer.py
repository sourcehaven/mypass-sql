
import re

from ply import lex

from tokens import tokens # noqa


t_PLUS = r'\+'
t_MINUS = r'-'
t_MULTIPLY = r'\*'
t_DIVIDE = r'/'
t_LP = r'\('
t_RP = r'\)'
t_COMMA = r','
t_SEMICOLON = r';'

t_NE = r'!=|<>'
t_GE = r'>='
t_LE = r'<='
t_EQ = r'='
t_GT = r'>'
t_LT = r'<'


def t_STR(t):
    r'("[^"]*"|\'[^\']*\')'
    return t


def t_SELECT(t):
    r'SELECT'
    return t


def t_INSERT(t):
    r'INSERT|INSERT\s+INTO'
    return t


def t_UPDATE(t):
    r'UPDATE'
    return t


def t_DELETE(t):
    r'DELETE|DELETE\s+FROM'
    return t


def t_TRUNCATE(t):
    r'TRUNCATE|TRUNCATE\s+TABLE'
    return t


def t_FROM(t):
    r'FROM'
    return t


def t_WHERE(t):
    r'WHERE'
    return t


def t_SET(t):
    r'SET'
    return t


def t_AND(t):
    r'AND|&'
    return t


def t_OR(t):
    r'OR|\|'
    return t


def t_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_FLOAT(t):
    r'(\d*\.\d+|\d+\.\d*)'
    t.value = float(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


t_ignore = ' \t'


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lexer = lex.lex(reflags=re.IGNORECASE)
