import re

from ply import lex, yacc

from mypass.identifier_list import tokens
from mypass.identifier_list import parser


if __name__ == '__main__':
    lexer = lex.lex(module=tokens, reflags=re.IGNORECASE, debug=True)
    parser = yacc.yacc(module=parser)
    ret = parser.parse("x, y, z")
    print(ret)

    ret = parser.parse("(x, y, z)")
    print(ret)
