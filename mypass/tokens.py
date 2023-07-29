import abc
import re
import copy
from typing import AnyStr

from mypass.util import cast


class Token(abc.ABC):
    pattern = None

    __slots__ = 'value', 'line_no', 'start', 'end'

    def __init__(self, value: AnyStr = None, start: int = None, end: int = None, line_no: int = None):
        self.value = value
        self.start = start
        self.end = end
        self.line_no = line_no

    def cast_value(self, remove_quotes=True):
        return cast(self.value, remove_quotes)

    def __eq__(self, other):
        return isinstance(other, Token) \
            and other.name == self.name \
            and other.span() == self.span() \
            and other.value == self.value

    def copy(self):
        """
        Returns a shallow copy, by using copy function from copy module on self
        """
        new = copy.copy(self)
        return new

    def span(self):
        return self.start, self.end

    @property
    def name(self):
        return type(self).__name__

    def __repr__(self):
        return (f"Token("
                f"class={self.name}"
                f", pattern=r'{self.pattern.pattern}'"
                f", span={self.span()!r}"
                f", value={self.value!r})")


class Comment(Token):
    pattern = re.compile(r'--.*')


class Insert(Token):
    pattern = re.compile(r'INSERT\s+INTO|INSERT', re.I)


class Delete(Token):
    pattern = re.compile(r'DELETE\s+FROM|DELETE', re.I)


class Truncate(Token):
    pattern = re.compile(r'TRUNCATE\s+TABLE|TRUNCATE', re.I)


class OrderBy(Token):
    pattern = re.compile(r'ORDER\s+BY', re.I)


class Ascending(Token):
    pattern = re.compile(r'ASCENDING|ASC|↑', re.I)


class Descending(Token):
    pattern = re.compile(r'DESCENDING|DESC|↓', re.I)


class Select(Token):
    pattern = re.compile(r'SELECT', re.I)


class From(Token):
    pattern = re.compile(r'FROM', re.I)


class Values(Token):
    pattern = re.compile(r'VALUES', re.I)


class Update(Token):
    pattern = re.compile(r'UPDATE', re.I)


class Set(Token):
    pattern = re.compile(r'SET', re.I)


class Where(Token):
    pattern = re.compile(r'WHERE', re.I)


class And(Token):
    pattern = re.compile(r'AND|&', re.I)


class Or(Token):
    pattern = re.compile(r'OR|\|', re.I)


class NotEquals(Token):
    pattern = re.compile(r'!=|<>')


class GreaterEquals(Token):
    pattern = re.compile(r'>=')


class LessEquals(Token):
    pattern = re.compile(r'<=')


class Greater(Token):
    pattern = re.compile(r'>')


class Less(Token):
    pattern = re.compile(r'<')


class Times(Token):
    pattern = re.compile(r'\*')


class Divide(Token):
    pattern = re.compile(r'/')


class Plus(Token):
    pattern = re.compile(r'\+')


class Minus(Token):
    pattern = re.compile(r'-')


class Backslash(Token):
    pattern = re.compile(r'\\')


class Dot(Token):
    pattern = re.compile(r'\.')


class Caret(Token):
    pattern = re.compile(r'\^')


class Dollar(Token):
    pattern = re.compile(r'\$')


class Comma(Token):
    pattern = re.compile(r',')


class Equals(Token):
    pattern = re.compile(r'=')


class Hashtag(Token):
    pattern = re.compile(r'#')


class NewLine(Token):
    pattern = re.compile(r'\n')


class Semicolon(Token):
    pattern = re.compile(r';')


class ExclamationMark(Token):
    pattern = re.compile(r'!')


class QuestionMark(Token):
    pattern = re.compile(r'\?')


class Percentage(Token):
    pattern = re.compile(r'%')


class LeftBracket(Token):
    pattern = re.compile(r'\[')


class RightBracket(Token):
    pattern = re.compile(r']')


class LeftParenthesis(Token):
    pattern = re.compile(r'\(')


class RightParenthesis(Token):
    pattern = re.compile(r'\)')


class LeftCurlyBracket(Token):
    pattern = re.compile(r'\{')


class RightCurlyBracket(Token):
    pattern = re.compile(r'}')


class Identifier(Token):
    pattern = re.compile(r'[A-Za-z]\w*')


class Literal(Token, abc.ABC):
    pass


class String(Literal):
    pattern = re.compile(r'"[^"]*"|\'[^\']*\'')


class Float(Literal):
    pattern = re.compile(r'\d*\.\d+|\d+\.\d*')


class Integer(Literal):
    pattern = re.compile(r'\d+')


class Boolean(Literal):
    pattern = re.compile(r'\b(?:True|False)\b', re.I)


class Unknown(Token):
    pattern = re.compile(r'[^\t ]+')


sql_tokens = (
    Comment, String, Boolean,
    Insert, Delete, Truncate, OrderBy, Ascending, Descending,
    Select, From, Values, Update, Set,
    Where, And, Or,
    NotEquals, GreaterEquals, LessEquals, Greater, Less, Equals,
    Times, Divide, Plus, Minus,
    Backslash, Caret, Dollar, Comma, Hashtag, Semicolon, ExclamationMark, QuestionMark, Percentage,
    LeftBracket, RightBracket, LeftParenthesis, RightParenthesis, LeftCurlyBracket, RightCurlyBracket,
    Identifier, Float, Integer, Dot, Unknown,
)
