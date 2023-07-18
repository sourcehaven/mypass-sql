import abc
import re

from mypass.exceptions import InvalidTokenException


class Token(abc.ABC):
    PATTERN: str = None

    def __new__(cls, value):
        token_type = cls.__name__.upper()
        instance = super().__new__(cls)
        instance.type = token_type
        return instance

    def __init__(self, value):
        if self.PATTERN is None:
            raise NotImplementedError(f"Pattern not defined for {self.type} subclass")

        regex_pattern = re.compile(self.PATTERN)
        if not regex_pattern.match(value):
            self.raise_invalid_token()

        self.value = value
        self.standardized_value = self._standardized_value()

    def raise_invalid_token(self):
        raise InvalidTokenException(f'Invalid {self.type} "{self.value}"')

    def __str__(self) -> str:
        return self.value

    def __repr__(self) -> str:
        return f'{self.type}({self.standardized_value})'

    def __eq__(self, other) -> bool:
        if isinstance(other, Token):
            return self.value == other.value and self.type == other.type
        return NotImplemented

    def _standardized_value(self) -> str:
        return self.value


class Command(Token):
    PATTERN = r'(?i)\s*(INSERT\s*INTO|DELETE\s*FROM|TRUNCATE\s*TABLE|SELECT|UPDATE)\s*'

    def _standardized_value(self) -> str:
        value = self.value.strip().upper()
        if value.startswith("INSERT"):
            return "INSERT INTO"
        if value.startswith("DELETE"):
            return "DELETE FROM"
        if value.startswith("TRUNCATE"):
            return "TRUNCATE TABLE"
        return value


class Keyword(Token):
    PATTERN = r'(?i)\s*(FROM|WHERE|NOT\s*IN|IN)\s*'


class Function(Token):
    PATTERN = r'(?i)\s*(SUM|COUNT|MAX|MIN)\s*'


class Operator(Token, abc.ABC):
    pass


class UnaryOperator(Operator):
    PATTERN = r'\s*([-+*/=])\s*'


class LogicalOperator(Operator):
    PATTERN = r'\s*(&|\||AND|OR)\s*'

    def _standardized_value(self) -> str:
        if self.value == '&':
            return 'AND'
        elif self.value == '|':
            return 'OR'
        return self.value


class ArithmeticOperator(Operator):
    PATTERN = r'\s*([-+*/])\s*'


class ComparisonOperator(Operator):
    PATTERN = r'\s*(<>|<=|>=|!=|<|>|=)\s*'

    def _standardized_value(self) -> str:
        if self.value == '<>':
            return '!='
        return self.value


class Punctuation(Token):
    PATTERN = r'\s*(,|\(|\)|;)\s*'


class Identifier(Token):
    PATTERN = r'\s*([a-zA-Z][a-zA-Z0-9_]*)\s*'


class Literal(Token, abc.ABC):
    pass


class Float(Literal):
    PATTERN = r'\s*([0-9]+\.[0-9]+)\s*'

    def _standardized_value(self) -> float:
        return float(self.value)


class Integer(Literal):
    PATTERN = r'\s*([0-9]+)\s*'

    def _standardized_value(self) -> int:
        return int(self.value)


class String(Literal):
    PATTERN = r'\s*("[^"]*"|\'[^\']*\')\s*'

    def _standardized_value(self) -> str:
        return self.value[1:-1]


class Variable(Token):
    PATTERN = r'\s*([a-zA-Z_][a-zA-Z0-9_]*)\s*'

