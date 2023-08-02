import re
from typing import Sequence, Type, Iterable

from .tokens import Token
from .util import is_non_overlapping, find_between


def tokenize(string: str, tokens: Sequence[Type[Token]]):
    token_spans = []

    def generate_tokens():
        for token in tokens:
            for match in re.finditer(token.pattern, string):
                curr_span = match.span()

                if is_non_overlapping(curr_span, token_spans):
                    token_spans.append(curr_span)
                    instance = token(value=match.group(), start=curr_span[0], end=curr_span[1], line_no=None)
                    yield instance

    sorted_tokens = sorted(generate_tokens(), key=lambda t: t.start)

    return sorted_tokens


def find_tokens_between(
        tokens: Sequence[Token], start_token: Type[Token] = None, end_tokens: Type[Token] | Sequence[Type[Token]] = (),
        require_start=False, require_end=False):

    start_token = start_token.__name__

    if isinstance(end_tokens, Iterable):
        end_tokens = [end_token.__name__ for end_token in end_tokens]
    else:
        end_tokens = end_tokens.__name__,

    token_names = [token.name for token in tokens]
    indexes = find_between(token_names, start_token, end_tokens, require_start=require_start, require_end=require_end)

    return tokens[indexes[0]: indexes[1]]


def validate_grammar(source: Sequence, target: Sequence):
    """
    Returns True if all `target` token is in `source` in sequenced order.
    """

    if len(target) == 0:
        return False

    i = 0
    for s in source:
        if s.name == target[i].name:
            i += 1
            if len(target) == i:
                return True

    return False
