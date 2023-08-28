from itertools import groupby
from typing import Sequence

from .exceptions import SqlSyntaxError, ItemNotFound
from .tokenizer import find_tokens_between
from .tokens import (
    Token,
    Semicolon,
    Identifier,
    Asterisk,
    Comma,
    Equals,
    Literal,
    LeftParenthesis,
    RightParenthesis,
)

from .sql.tokens import (
    And,
    OrderBy,
    Where,
    From,
    Select,
    Insert,
    Truncate,
    Delete,
    Update,
    Values,
    Set,
)


def split_statements(tokens: Sequence[Token]):
    def is_semicolon(token: Token):
        return token.name == Semicolon.__name__

    statements = (
        list(g)
        for is_semicolon, g in groupby(tokens, key=is_semicolon)
        if not is_semicolon
    )
    return statements


def remove_parenthesis(tokens: Sequence[Token]):
    if isinstance(tokens[0], LeftParenthesis) and isinstance(
        tokens[-1], RightParenthesis
    ):
        return tokens[1:-1]
    if isinstance(tokens[0], LeftParenthesis) and not isinstance(
        tokens[-1], RightParenthesis
    ):
        raise SqlSyntaxError('Missing closing parenthesis ")" in statement!')
    if not isinstance(tokens[0], LeftParenthesis) and isinstance(
        tokens[-1], RightParenthesis
    ):
        raise SqlSyntaxError('Missing opening parenthesis "(" in statement!')
    return tokens


def get_field_list(tokens: Sequence[Token]):
    def generate_values():
        for i, token in enumerate(tokens):
            if i % 2 == 0:
                if isinstance(token, Identifier):
                    yield token.value
                else:
                    raise SqlSyntaxError.from_token(token)
            else:
                if isinstance(token, Comma):
                    continue
                raise SqlSyntaxError.from_token(token, expected=",")

    if len(tokens) == 0:
        raise SqlSyntaxError("Missing field(s)!")

    return list(generate_values())


def get_table_name(tokens: Sequence[Token]):
    if len(tokens) == 0:
        raise SqlSyntaxError("Table name must be specified!")

    if len(tokens) > 1:
        raise SqlSyntaxError("Only a single table name can be specified!")

    if isinstance(tokens[0], Identifier):
        return tokens[0].value

    raise SqlSyntaxError(f"Invalid table name: {tokens[0].value!r}!")


def get_field_dict(tokens: Sequence[Token]):
    groups = [
        tuple(group)
        for is_comma_or_and, group in groupby(
            tokens, lambda x: isinstance(x, (And, Comma))
        )
        if not is_comma_or_and
    ]

    def generate_dict():
        for group in groups:
            if (
                len(group) == 3
                and isinstance(group[0], Identifier)
                and isinstance(group[1], Equals)
                and isinstance(group[2], Literal)
            ):
                yield group[0].value, group[2].cast_value()
            else:
                raise SqlSyntaxError("Format must be {identifier}={literal}!")

    return dict(generate_dict())


def __parse_select(tokens: Sequence[Token]):
    try:
        field_tokens = find_tokens_between(tokens, Select, From, require_end=True)
    except ItemNotFound as e:
        raise SqlSyntaxError('Missing "FROM" keyword in "SELECT" statement!') from e

    if len(field_tokens) == 1 and isinstance(field_tokens[0], (Identifier, Asterisk)):
        fields = field_tokens[0].value
    else:
        fields = get_field_list(field_tokens)

    table_tokens = find_tokens_between(tokens, From, (Where, Semicolon))
    table = get_table_name(table_tokens)

    try:
        where_tokens = find_tokens_between(
            tokens, Where, (Semicolon, OrderBy), require_start=True
        )
        where_dict = get_field_dict(where_tokens)
    except ItemNotFound:
        where_dict = dict()

    return {"operation": "read", "table": table, "fields": fields, "where": where_dict}


def __parse_insert(tokens: Sequence[Token]):
    try:
        table_tokens = find_tokens_between(tokens, Insert, Values, require_end=True)
        table = get_table_name(table_tokens)
    except ItemNotFound as e:
        raise SqlSyntaxError('Missing "VALUES" keyword in "INSERT" statement!') from e

    value_tokens = find_tokens_between(tokens, Values, Semicolon)
    values_dict = get_field_dict(value_tokens)

    return {"operation": "create", "table": table, "fields": values_dict}


def __parse_update(tokens: Sequence[Token]):
    try:
        table_tokens = find_tokens_between(tokens, Update, Set, require_end=True)
        table = get_table_name(table_tokens)
    except ItemNotFound as e:
        raise SqlSyntaxError('Missing "SET" keyword in "UPDATE" statement!') from e

    field_tokens = find_tokens_between(tokens, Set, (Where, Semicolon))
    field_dict = get_field_dict(field_tokens)

    try:
        where_tokens = find_tokens_between(tokens, Where, Semicolon)
        where_dict = get_field_dict(where_tokens)
    except ItemNotFound:
        where_dict = dict()

    return {
        "operation": "update",
        "table": table,
        "fields": field_dict,
        "where": where_dict,
    }


def __parse_delete(tokens: Sequence[Token]):
    table_token = find_tokens_between(tokens, Delete, (Where, Semicolon))
    table = get_table_name(table_token)

    try:
        where_tokens = find_tokens_between(tokens, Where, Semicolon)
        where_dict = get_field_dict(where_tokens)
    except ItemNotFound:
        where_dict = dict()

    return {"operation": "delete", "table": table, "where": where_dict}


def __parser_truncate(tokens: Sequence[Token]):
    table_tokens = find_tokens_between(tokens, Truncate, Semicolon)

    table = get_table_name(table_tokens)

    return {
        "operation": "delete_all",
        "table": table,
    }


def parse_statement(tokens: Sequence[Token]):
    statement = tokens[0]

    if isinstance(statement, Select):
        return __parse_select(tokens)
    if isinstance(statement, Insert):
        return __parse_insert(tokens)
    if isinstance(statement, Update):
        return __parse_update(tokens)
    if isinstance(statement, Delete):
        return __parse_delete(tokens)
    if isinstance(statement, Truncate):
        return __parser_truncate(tokens)
    raise SqlSyntaxError(
        f"{statement} is not an SQL statement!"
        f"Valid statements are: {Select}, {Insert}, {Update}, {Delete}, {Truncate}"
    )


def parse_statements(tokens: Sequence[Token]):
    return (parse_statement(statement) for statement in split_statements(tokens))
