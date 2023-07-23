from itertools import groupby
from typing import Sequence

from mypass.exceptions import InvalidSqlStatement
from mypass.tokens import Token, TRUNCATE, DELETE, UPDATE, INSERT, SELECT, SEMICOLON


def split_statements(tokens: Sequence[Token]):
    def is_semicolon(token: Token):
        return token.id == SEMICOLON

    statements = [list(g) for is_semicolon, g in groupby(tokens, key=is_semicolon) if not is_semicolon]
    return statements


class SqlStatement:

    start_tokens = (SELECT, INSERT, UPDATE, DELETE, TRUNCATE)

    def __init__(self, tokens: Sequence[Token]):
        if len(tokens) == 0:
            raise InvalidSqlStatement(
                f'No SQL statement was provided! Use one from {self.start_tokens} statements!')

        if tokens[0].id not in self.start_tokens:
            raise InvalidSqlStatement(
                f'SQL statement must start with: {self.start_tokens}, not {tokens[0].value!r}.')

        self.tokens = tokens
