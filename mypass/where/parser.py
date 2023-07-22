from .tokens import tokens


def p_where(p):
    """
    where : WHERE identifier_equals_literal_list
    """
    p[0] = p[2]


def p_identifier_equals_literal_list(p):
    """
    identifier_equals_literal_list : identifier_equals_literal
                                   | identifier_equals_literal AND identifier_equals_literal_list
    """

    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[1]
        p[0].update(p[3])


def p_identifier_equals_literal(p):
    """
    identifier_equals_literal : IDENTIFIER EQUALS LITERAL
    """
    p[0] = {p[1]: p[3]}
