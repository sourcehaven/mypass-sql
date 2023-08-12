import abc
import copy
import re
from typing import AnyStr, Iterable, Type


class Token(abc.ABC):
    color: str = 'ansidefault'
    pattern: re.Pattern = None

    __slots__ = 'value', 'line_no', 'start', 'end'

    def __init__(self, value: AnyStr = None, start: int = None, end: int = None, line_no: int = None):
        self.value = value
        self.start = start
        self.end = end
        self.line_no = line_no

    def __eq__(self, other):
        return isinstance(other, type(self)) or isinstance(self, type(other))

    def __hash__(self):
        return hash(type(self))

    def true_value(self):
        return self.value

    def copy(self):
        """
        Returns a shallow copy, by using copy function from copy module on self
        """
        new = copy.copy(self)
        return new

    def span(self):
        return self.start, self.end, self.line_no

    @property
    def name(self):
        return type(self).__name__

    def __str__(self):
        return (f"Token("
                f"class={self.name}"
                f", pattern=r'{self.pattern.pattern}'"
                f", span={self.span()!r}"
                f", value={self.value!r})")

    def __repr__(self):
        return (f"Token("
                f"class={self.name}"
                f", pattern=r'{self.pattern.pattern}'"
                f", span={self.span()!r}"
                f", value={self.value!r})")


class Command(Token):
    color = 'ansigreen'


class SubCommand(Token):
    color = 'ansibrightgreen'


class Punctuation(Token, abc.ABC):
    color = 'ansigray'


class Literal(Token, abc.ABC):
    ...


class Comparison(Token, abc.ABC):
    color = 'ansiyellow'


class Arithmetic(Token, abc.ABC):
    color = 'ansibrightmagenta'


class Unknown(Token):
    color = 'ansired'
    pattern = re.compile('.+')


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


class Asterisk(Arithmetic):
    pattern = re.compile(r'\*')


class Divide(Arithmetic):
    pattern = re.compile(r'/')


class Plus(Arithmetic):
    pattern = re.compile(r'\+')


class Minus(Arithmetic):
    pattern = re.compile(r'-')


class Backslash(Punctuation):
    pattern = re.compile(r'\\')


class Slash(Punctuation):
    pattern = re.compile(r'/')


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


class QuotationMark(Punctuation):
    pattern = re.compile('"')


class Ampersand(Punctuation):
    pattern = re.compile('&')


class Apostrophe(Punctuation):
    pattern = re.compile("'")


class AtSign(Punctuation):
    pattern = re.compile('@')


class Underscore(Punctuation):
    pattern = re.compile('_')


class Backtick(Punctuation):
    pattern = re.compile('`')


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
    color = 'ansibrightgreen'
    pattern = re.compile(r'"[^"]*"|\'[^\']*\'')

    def true_value(self):
        return self.value[1:-1]


class Float(Literal):
    color = 'ansibrightcyan'
    pattern = re.compile(r'\d*\.\d+|\d+\.\d*')

    def true_value(self):
        return float(self.value)


class Integer(Literal):
    color = 'ansibrightcyan'
    pattern = re.compile(r'\d+')

    def true_value(self):
        return int(self.value)


class Boolean(Literal):
    color = 'ansibrightyellow'
    pattern = re.compile(r'\b(?:true|false|on|off)\b', re.I)

    def true_value(self):
        return self.value.lower() in ('true', 'on')


class Whitespace(Token):
    pass


class Space(Whitespace):
    pattern = re.compile(r' ')


class NewLine(Whitespace):
    pattern = re.compile(r'\n')


class Tabulator(Whitespace):
    pattern = re.compile(r'\t')


class CarriageReturn(Whitespace):
    pattern = re.compile(r'\r')


class FormFeed(Whitespace):
    pattern = re.compile(r'\f')


class Option(Token):
    pass


class LongOption(Option):
    pattern = re.compile(r'--\w+')


class ShortOption(Option):
    pattern = re.compile(r'-\w+')


def _get_keywords(__tokens: Iterable[Type[Token]], /, subclass: object = None):

    def split_patterns():
        for token in __tokens:
            pattern_split = token.pattern.pattern.split('|')
            for pattern in pattern_split:
                yield pattern.lower(), token

    keywords = (
        re.sub(r'\\b', '', re.sub(r'\\s\+', ' ', pattern))
        for pattern, token in split_patterns()
        if issubclass(token, subclass if subclass else object)
    )

    return (keyword for keyword in keywords if re.match(r'\w+', keyword))


literal_tokens = String, Float, Integer, Boolean

arithmetic_tokens = Asterisk, Divide, Plus, Minus

comparison_tokens = NotEquals, GreaterEquals, LessEquals, Equals, Greater, Less

space_tokens = Space, NewLine, Tabulator, CarriageReturn, FormFeed

punctuation_tokens = (
    Backslash, Slash, Dot, Caret, Dollar,
    Tilde, Comma, Hashtag, Percentage,
    ExclamationMark, QuestionMark,
    DoubleColon, Semicolon,
    QuotationMark, Ampersand, Apostrophe, AtSign, Underscore, Backtick
)

paired_tokens = (
    LeftBracket, RightBracket,
    LeftCurlyBracket, RightCurlyBracket,
    LeftParenthesis, RightParenthesis,
)

tokens = *literal_tokens, *arithmetic_tokens, *comparison_tokens, *punctuation_tokens, *paired_tokens, *space_tokens
