from ply import yacc

from lexer import tokens # noqa


def p_expression(p):
    """expression : ID
                  | INT
                  | FLOAT
                  | STR
                  | expression GT expression
                  | expression LT expression
                  | expression GE expression
                  | expression LE expression
                  | expression EQ expression
                  | expression NE expression
                  | LP expression RP"""
    # Perform actions here to handle the expression
    pass


def p_condition(p):
    """condition : expression
                 | expression AND expression
                 | expression OR expression"""
    # Perform actions here to handle the condition
    pass


def p_optional_where(p):
    """optional_where : WHERE condition
                      | empty"""
    # empty is a placeholder for an empty production (no WHERE clause)
    pass


def p_id_list(p):
    """id_list : ID
               | id_list COMMA ID"""
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]


parser = yacc.yacc()
