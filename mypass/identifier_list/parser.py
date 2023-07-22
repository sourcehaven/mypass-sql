from .tokens import tokens


def p_identifier_list_within_paren(p):
    """
    identifier_list_within_paren : identifier_list
                                 | LEFT_PARENTHESIS identifier_list RIGHT_PARENTHESIS
    """
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = p[2]


def p_identifier_list(p):
    """
    identifier_list : IDENTIFIER
                    | identifier_list COMMA IDENTIFIER
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = p[1] + [p[3]]
