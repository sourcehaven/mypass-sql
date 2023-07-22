def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {p.lexpos}: "
              f"Unexpected token '{p.value}' of type '{p.type}'")
    else:
        print("Syntax error: Incomplete expression")
