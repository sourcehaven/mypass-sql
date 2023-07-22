import re

from ply import lex, yacc

from mypass.where import tokens
from mypass.where import parser


if __name__ == '__main__':
    lexer = lex.lex(module=tokens, reflags=re.IGNORECASE, debug=True)
    parser = yacc.yacc(module=parser)
    ret = parser.parse("WHERE x=5 AND y=15")
    print(ret)
