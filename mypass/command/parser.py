from typing import Sequence, Iterable

from .tokens import Command, Add, Update, Copy, Remove, Show
from ..tokens import Token, Whitespace, Pipe


def _parse_field_assignment_list(tokens):
    for i in range(0, len(tokens), 4):
        field = tokens[i]
        value = tokens[i + 2]
        yield field, value


def _parse_field_list(tokens):
    for i in range(0, len(tokens), 2):
        field = tokens[i]
        yield field


def _split_by_pipe(tokens: list[Token]):
    index = tokens.index(Pipe())

    return tokens[:index], tokens[index+1:]


def parse(tokens: Sequence[Token]):
    tokens = [token for token in tokens if not isinstance(token, Whitespace)]

    if isinstance(tokens[0], Command):
        yield tokens[0]
    
    field_tokens = lambda: tokens[1:]

    # add syntax: add username="user1", password="pass123"
    # del syntax: del title="github", tag="personal"
    if isinstance(tokens[0], (Add, Remove)):
        yield from _parse_field_assignment_list(field_tokens())

    # update syntax: update username="new_name" | title="facebook"
    elif isinstance(tokens[0], Update):
        update, crit = _split_by_pipe(field_tokens())
        yield from _parse_field_assignment_list(update)
        yield from _parse_field_assignment_list(crit)

    # copy syntax: copy username, password | title="facebook"
    # read syntax: read username, password | title="facebook
    elif isinstance(tokens[0], (Copy, Show)):
        fields, field_assignment_list = _split_by_pipe(field_tokens())
        yield from _parse_field_list(fields)
        yield from _parse_field_assignment_list(field_assignment_list)


def tokens_to_dict(token_pairs: Iterable[tuple[Token, Token]]):
    return {str(key): val.true_value() for key, val in token_pairs}


def tokens_to_list(tokens: Iterable[Token]):
    return [str(token) for token in tokens]
