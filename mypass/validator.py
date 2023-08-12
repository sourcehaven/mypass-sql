from typing import Sequence

from mypass.tokens import Token, Whitespace, Identifier, Delete, Select, Insert, Comma, Where, Equals, Literal, \
    Integer


def validator(tokens: Sequence[Token], *syntax: Token | set[Token] | tuple[Token, ...] | list[Token]):
    """
        Token = Mandatory
        set   = OR + Mandatory
        tuple = Optional
        list  = One or more in sequence separated by ','

        Example: Delete, {vault, master}, (Where), {0: Identifier, 1: Equals, 2: Literal, sep=Comma}
    """

    assert not any(isinstance(token, Whitespace) for token in tokens), f"Instances of {Whitespace.__name__} are not allowed!"

    token_position = 0
    sequence_allowed = False

    def single_mandatory():
        nonlocal sequence_allowed, token_position

        sequence_allowed = False
        if token == rule:
            token_position += 1
        else:
            raise SyntaxError(f'Missing mandatory {rule.name} token from position {token_position}!')

    def multiple_mandatory():
        nonlocal sequence_allowed, token_position

        sequence_allowed = False
        if token in rule:
            token_position += 1
        else:
            raise SyntaxError(f'{token.name} not present in {", ".join(r.name for r in rule)}')

    def multiple_optional():
        nonlocal sequence_allowed, token_position

        sequence_allowed = False
        if token in rule:
            token_position += 1

    def one_or_more_sequential():
        nonlocal sequence_allowed, token_position

        sequence_allowed = True
        for i, e in enumerate(rule):
            if tokens[token_position] == e:
                token_position += 1
            else:
                raise SyntaxError(f'{token.name} must be type of {e.name}')

    def continue_sequence():
        if sequence_allowed:
            one_or_more_sequential()
        else:
            raise SyntaxError('Comma is not allowed here!')

    for rule in syntax:
        token = tokens[token_position]

        match rule:
            case Comma():
                continue_sequence()
            case Token():
                single_mandatory()
            case set():
                multiple_mandatory()
            case tuple():
                multiple_optional()
            case list():
                one_or_more_sequential()

    return True


validator(
    [Delete(), Insert(), Where(), Identifier(), Equals(), Integer(), Comma(), Identifier(), Equals(), Integer()],
    Delete(), {Select(), Insert()}, (Where(),), [Identifier(), Equals(), Literal()]
)

