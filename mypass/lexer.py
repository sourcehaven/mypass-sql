import abc
import re

from mypass.tokens import Token


def get_concrete_classes(cls):
    concrete_classes = []
    for subclass in cls.__subclasses__():
        if abc.ABC not in subclass.__bases__:
            concrete_classes.append(subclass)
        else:
            concrete_classes.extend(get_concrete_classes(subclass))
    return concrete_classes


class Lexer:
    def __init__(self, sql: str):
        self.sql = sql
        self.position = 0

    def _tokenize(self):
        concrete_classes = get_concrete_classes(Token)

        while self.position < len(self.sql):
            match = None
            for TokenClass in concrete_classes:
                match = re.match(TokenClass.PATTERN, self.sql[self.position:])
                if match:
                    value = match.group(1)
                    token = TokenClass(value)
                    print(f'DEBUG LOG - Token: {token!r}')
                    yield token
                    self.position += match.end()
                    break

            if not match:
                self.position += 1

    def get_tokens(self):
        return list(self._tokenize())
