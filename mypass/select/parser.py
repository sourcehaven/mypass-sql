from .tokens import tokens


start = 'select'


def p_select(p):
    """
    select : SELECT identifier_equals_literal_list FROM IDENTIFIER where
    """
    p[0] = p[2], p[4]
    print(p[0])


from mypass.identifier_list.parser import p_identifier_list_within_paren, p_identifier_list
from mypass.where.parser import p_where, p_identifier_equals_literal_list, p_identifier_equals_literal
from mypass.parser import p_error
