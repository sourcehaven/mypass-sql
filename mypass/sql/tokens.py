import abc
import re

from ..tokens import (
    Token, String, Boolean, NotEquals, GreaterEquals, LessEquals, Greater, Less, Equals, Asterisk,
    Divide, Plus, Minus, Semicolon, Comma, RightParenthesis, LeftParenthesis, Identifier, LeftBracket, RightBracket,
    Float, Integer, Dot, Space, NewLine, Tabulator, CarriageReturn, Command, _get_keywords
)


class SqlCommand(Command):
    pattern = re.compile(r'SQL', re.I)


class SqlComment(Token):
    color = 'ansibrightblack'
    pattern = re.compile(r'--.*')


class SqlKeyword(Token, abc.ABC):
    color = 'ansibrightblue'


class Insert(SqlKeyword):
    pattern = re.compile(r'INSERT\s+INTO|INSERT', re.I)


class Delete(SqlKeyword):
    pattern = re.compile(r'DELETE\s+FROM|DELETE', re.I)


class Truncate(SqlKeyword):
    pattern = re.compile(r'TRUNCATE\s+TABLE|TRUNCATE', re.I)


class OrderBy(SqlKeyword):
    pattern = re.compile(r'ORDER\s+BY', re.I)


class Ascending(SqlKeyword):
    pattern = re.compile(r'ASCENDING|ASC|↑', re.I)


class Descending(SqlKeyword):
    pattern = re.compile(r'DESCENDING|DESC|↓', re.I)


class Select(SqlKeyword):
    pattern = re.compile(r'SELECT', re.I)


class From(SqlKeyword):
    pattern = re.compile(r'FROM', re.I)


class Values(SqlKeyword):
    pattern = re.compile(r'VALUES', re.I)


class Update(SqlKeyword):
    pattern = re.compile(r'UPDATE', re.I)


class Set(SqlKeyword):
    pattern = re.compile(r'SET', re.I)


class Where(SqlKeyword):
    pattern = re.compile(r'WHERE', re.I)


class And(SqlKeyword):
    pattern = re.compile(r'AND|&', re.I)


class Or(SqlKeyword):
    pattern = re.compile(r'OR|\|', re.I)


statement_tokens = (Select, Insert, Update, Delete, Truncate)

tokens = (
    SqlComment, String, Boolean, SqlCommand,
    Insert, Delete, Truncate, OrderBy, Ascending, Descending,
    Select, From, Values, Update, Set,
    Where, And, Or,
    NotEquals, GreaterEquals, LessEquals, Greater, Less, Equals,
    Asterisk, Divide, Plus, Minus,
    Comma, Semicolon,
    LeftParenthesis, RightParenthesis,
    LeftBracket, RightBracket,
    Identifier, Float, Integer, Dot, Space, NewLine, Tabulator, CarriageReturn
)


primary_keywords = tuple(_get_keywords(tokens, SqlCommand))
secondary_keywords = tuple(_get_keywords(statement_tokens))
