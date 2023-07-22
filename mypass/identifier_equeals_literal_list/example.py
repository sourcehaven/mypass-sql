import re

from ply import lex, yacc

from mypass.identifier_equeals_literal_list import tokens
from mypass.identifier_equeals_literal_list import parser


if __name__ == '__main__':
    lexer = lex.lex(module=tokens, reflags=re.IGNORECASE, debug=True)
    parser = yacc.yacc(module=parser)
    ret = parser.parse("x=15 AND y=20 AND z='sajt'")
    print(ret)
