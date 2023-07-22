from mypass.tokens import (
    AND, EQUALS, IDENTIFIER, LITERAL,
    t_AND, t_EQUALS, t_IDENTIFIER, t_LITERAL,
    t_ignore,
)

identifier_equals_literal_tokens = (
    AND,
    EQUALS,
    IDENTIFIER,
    LITERAL,
)

tokens = identifier_equals_literal_tokens
