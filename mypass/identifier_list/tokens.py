from mypass.tokens import (
    COMMA, IDENTIFIER, LEFT_PARENTHESIS, RIGHT_PARENTHESIS,
    t_COMMA, t_IDENTIFIER, t_LEFT_PARENTHESIS, t_RIGHT_PARENTHESIS,
    t_ignore
)

identifier_tokens = (
    COMMA,
    IDENTIFIER,
    LEFT_PARENTHESIS,
    RIGHT_PARENTHESIS,
)

tokens = identifier_tokens
