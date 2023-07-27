from itertools import groupby
from typing import Sequence

from mypass.exceptions import InvalidSqlStatement
from mypass.tokens import (
    Token, Semicolon, And, Identifier, Times, Comma,
    Equals, Literal, LeftParenthesis, RightParenthesis
)


def split_statements(tokens: Sequence[Token]):
    def is_semicolon(token: Token):
        return token.name == Semicolon.__name__

    statements = [list(g) for is_semicolon, g in groupby(tokens, key=is_semicolon) if not is_semicolon]
    return statements


def remove_parenthesis(tokens: Sequence[Token]):
    if isinstance(tokens[0], LeftParenthesis) and isinstance(tokens[-1], RightParenthesis):
        return tokens[1:-1]
    if isinstance(tokens[0], LeftParenthesis) and not isinstance(tokens[-1], RightParenthesis):
        raise InvalidSqlStatement('Missing ")" from statement!')
    if not isinstance(tokens[0], LeftParenthesis) and isinstance(tokens[-1], RightParenthesis):
        raise InvalidSqlStatement('Missing "(" from statement!')
    return tokens


def get_identifier_list(tokens: Sequence[Token]):
    def generate_values():
        for i, token in enumerate(tokens):
            if i % 2 == 0:
                if isinstance(token, Identifier):
                    yield token.value
                else:
                    raise InvalidSqlStatement('Must be in Identifier!')
            else:
                if isinstance(token, Comma):
                    continue
                else:
                    raise InvalidSqlStatement('Must be a comma!')

    if len(tokens) == 1:
        if isinstance(tokens[0], (Identifier, Times)):
            return [tokens[0].value]
        raise InvalidSqlStatement('Must be an identifier or "*"!')

    return list(generate_values())


def get_table_name(tokens: Sequence[Token]):
    if len(tokens) != 1:
        raise InvalidSqlStatement('Must be single table!')
    elif isinstance(tokens[0], Identifier):     # and tokens[0].value.lower() in ('vault', 'master'):
        return tokens[0].value
    raise InvalidSqlStatement('Must be an Identifier and table is called "vault" or "master"!')


def get_filter_dict(tokens: Sequence[Token]):
    groups = [
        tuple(group)
        for is_comma_or_and, group in groupby(tokens, lambda x: isinstance(x, (And, Comma)))
        if not is_comma_or_and
    ]

    def generate_dict():
        for group in groups:
            if len(group) == 3 \
                    and isinstance(group[0], Identifier) \
                    and isinstance(group[1], Equals) \
                    and isinstance(group[2], Literal):
                yield group[0].value, group[2].cast_value()
            else:
                raise InvalidSqlStatement('...')

    return dict(generate_dict())
