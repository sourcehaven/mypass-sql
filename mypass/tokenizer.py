import re
from typing import Sequence, Type, Iterable

from .tokens import Token, Whitespace, NewLine, Unknown
from .util import is_non_overlapping, find_between


def tokenize(string: str, tokens: Sequence[Type[Token]], remove_spaces=False):
    token_spans = []

    def generate_unknown_token_spans():
        prev_end = 0

        for start, end in token_spans:
            if start > prev_end:
                yield prev_end, start
            prev_end = end

        if len(string) > prev_end:
            yield prev_end, len(string)

    def generate_tokens():
        for token in tokens:
            for match in re.finditer(token.pattern, string):
                curr_span = match.span()
                if is_non_overlapping(curr_span, token_spans):
                    token_spans.append(curr_span)
                    instance = token(value=match.group(), start=curr_span[0], end=curr_span[1], line_no=None)
                    yield instance

    matching_tokens = list(generate_tokens())
    token_spans.sort(key=lambda s: s[0])

    missing_tokens = [
        Unknown(string[span[0]: span[1]], start=span[0], end=span[1])
        for span in generate_unknown_token_spans()
    ]

    sorted_tokens = sorted(matching_tokens + missing_tokens, key=lambda t: t.start)

    line_no = 1
    for token in sorted_tokens:
        token.line_no = line_no
        if isinstance(token, NewLine):
            line_no += 1

    if remove_spaces:
        return [token for token in sorted_tokens if not isinstance(token, Whitespace)]

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
