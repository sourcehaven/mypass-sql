import abc
import re
import copy
from typing import AnyStr

from .util import cast


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


class Keyword(Token, abc.ABC):
    pass


class Punctuation(Token, abc.ABC):
    pass


class Literal(Token, abc.ABC):
    pass


class Comparison(Token, abc.ABC):
    pass


class Arithmetic(Token, abc.ABC):
    pass


class Comment(Token):
    pattern = re.compile(r'--.*')


class Insert(Keyword):
    pattern = re.compile(r'INSERT\s+INTO|INSERT', re.I)


class Delete(Keyword):
    pattern = re.compile(r'DELETE\s+FROM|DELETE', re.I)


class Truncate(Keyword):
    pattern = re.compile(r'TRUNCATE\s+TABLE|TRUNCATE', re.I)


class OrderBy(Keyword):
    pattern = re.compile(r'ORDER\s+BY', re.I)


class Ascending(Keyword):
    pattern = re.compile(r'ASCENDING|ASC|↑', re.I)


class Descending(Keyword):
    pattern = re.compile(r'DESCENDING|DESC|↓', re.I)


class Select(Keyword):
    pattern = re.compile(r'SELECT', re.I)


class From(Keyword):
    pattern = re.compile(r'FROM', re.I)


class Values(Keyword):
    pattern = re.compile(r'VALUES', re.I)


class Update(Keyword):
    pattern = re.compile(r'UPDATE', re.I)


class Set(Keyword):
    pattern = re.compile(r'SET', re.I)


class Where(Keyword):
    pattern = re.compile(r'WHERE', re.I)


class And(Keyword):
    pattern = re.compile(r'AND|&', re.I)


class Or(Keyword):
    pattern = re.compile(r'OR|\|', re.I)


class NotEquals(Comparison):
    pattern = re.compile(r'!=|<>')


class GreaterEquals(Comparison):
    pattern = re.compile(r'>=')


class LessEquals(Comparison):
    pattern = re.compile(r'<=')


class Equals(Comparison):
    pattern = re.compile(r'=')


class Greater(Comparison):
    pattern = re.compile(r'>')


class Less(Comparison):
    pattern = re.compile(r'<')


class Times(Arithmetic):
    pattern = re.compile(r'\*')


class Divide(Arithmetic):
    pattern = re.compile(r'/')


class Plus(Arithmetic):
    pattern = re.compile(r'\+')


class Minus(Arithmetic):
    pattern = re.compile(r'-')


class Backslash(Punctuation):
    pattern = re.compile(r'\\')


class Dot(Punctuation):
    pattern = re.compile(r'\.')


class Caret(Punctuation):
    pattern = re.compile(r'\^')


class Dollar(Punctuation):
    pattern = re.compile(r'\$')


class Tilde(Punctuation):
    pattern = re.compile(r'~')


class Comma(Punctuation):
    pattern = re.compile(r',')


class Hashtag(Punctuation):
    pattern = re.compile(r'#')


class NewLine(Token):
    pattern = re.compile(r'\n')


class Semicolon(Punctuation):
    pattern = re.compile(r';')


class ExclamationMark(Punctuation):
    pattern = re.compile(r'!')


class QuestionMark(Punctuation):
    pattern = re.compile(r'\?')


class Percentage(Punctuation):
    pattern = re.compile(r'%')


class DoubleColon(Punctuation):
    pattern = re.compile(r':')


class LeftBracket(Punctuation):
    pattern = re.compile(r'\[')


class RightBracket(Punctuation):
    pattern = re.compile(r']')


class LeftParenthesis(Punctuation):
    pattern = re.compile(r'\(')


class RightParenthesis(Punctuation):
    pattern = re.compile(r'\)')


class LeftCurlyBracket(Punctuation):
    pattern = re.compile(r'\{')


class RightCurlyBracket(Punctuation):
    pattern = re.compile(r'}')


class Identifier(Token):
    pattern = re.compile(r'[A-Za-z]\w*')


class String(Literal):
    pattern = re.compile(r'"[^"]*"|\'[^\']*\'')


class Float(Literal):
    pattern = re.compile(r'\d*\.\d+|\d+\.\d*')


class Integer(Literal):
    pattern = re.compile(r'\d+')


class Boolean(Literal):
    pattern = re.compile(r'\b(?:True|False)\b', re.I)


class Space(Token):
    pattern = re.compile(r'\s+')


class Unknown(Token):
    pattern = re.compile(r'\S+')


sql_tokens = (
    Comment, String, Boolean,
    Insert, Delete, Truncate, OrderBy, Ascending, Descending,
    Select, From, Values, Update, Set,
    Where, And, Or,
    NotEquals, GreaterEquals, LessEquals, Greater, Less, Equals,
    Times, Divide, Plus, Minus,
    Backslash, Caret, Dollar, Comma, Hashtag, Semicolon, ExclamationMark, QuestionMark, Percentage, DoubleColon, Tilde,
    LeftBracket, RightBracket, LeftParenthesis, RightParenthesis, LeftCurlyBracket, RightCurlyBracket,
    Identifier, Float, Integer, Dot, Space, Unknown,
)
