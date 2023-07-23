from typing import Sequence, Iterable

from mypass.tokens import Token, AND


def tokenize(string: str, tokens: Sequence[Token]):

    def generate_tokens():
        for token in tokens:
            for match in token.finditer(string):
                new_token = token.copy(value=match.group(), start=match.start(), end=match.end())
                yield new_token

    sorted_tokens = sorted(generate_tokens(), key=lambda t: t.start)

    def remove_duplicate_tokens():
        if len(sorted_tokens) < 1:
            return sorted_tokens

        yield sorted_tokens[0]
        for i in range(1, len(sorted_tokens)):
            if sorted_tokens[i].value != sorted_tokens[i-1].value:
                yield sorted_tokens[i]

    cleansed_tokens = list(remove_duplicate_tokens())
    return cleansed_tokens


def get_tokens_between(tokens: Iterable[Token], start_token_id=None, end_token_id=None):
    start_index, end_index = 0, None

    if start_token_id:
        for i, token in enumerate(tokens):
            if token.id == start_token_id:
                start_index = i

    if end_token_id:
        for i, token in enumerate(tokens, start=start_index):
            if token.id == end_token_id:
                end_index = i

    return tokens[start_index+1: end_index]


def get_identifier_list(tokens: Sequence[Token]):
    return [tokens[i].value for i in range(0, len(tokens), 2)]


def get_filter_dict(tokens: Sequence[Token]):
    tokens = [token for token in tokens if token.id != AND]
    return {tokens[i].value: tokens[i+2].value for i in range(0, len(tokens), 3)}
