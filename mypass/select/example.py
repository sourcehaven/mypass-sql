import re

from ply import lex, yacc

from mypass.select import tokens
from mypass.select import parser


if __name__ == '__main__':
    lexer = lex.lex(module=tokens, reflags=re.IGNORECASE, debug=True)
    parser = yacc.yacc(module=parser)
    ret = parser.parse("SELECT id, sajt FROM table1")
    print(ret)
