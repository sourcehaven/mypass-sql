import re
from typing import Sequence, Type

from mypass.tokens import Token
from mypass.util import is_non_overlapping


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


def get_tokens_between(
        tokens: Sequence[Token], start_token: str | Type[Token] = None, end_token: str | Type[Token] = None):
    start_token = str.upper(start_token if isinstance(start_token, str) else start_token.name)
    end_token = str.upper(end_token if isinstance(end_token, str) else end_token.name)

    start_index, end_index = 0, None

    if start_token:
        for i in range(len(tokens)):
            if tokens[i].name.upper() == start_token:
                start_index = i
                break
        else:
            return []

    if end_token:
        for i in range(start_index, len(tokens)):
            if tokens[i].name.upper() == end_token:
                end_index = i
                break

    return tokens[start_index+1: end_index]


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
