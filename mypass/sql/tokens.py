import abc

from ..command.tokens import Command
from ..tokens import (
    Token,
    String,
    Boolean,
    NotEquals,
    GreaterEquals,
    LessEquals,
    Greater,
    Less,
    Equals,
    Asterisk,
    Divide,
    Plus,
    Minus,
    Semicolon,
    Comma,
    RightParenthesis,
    LeftParenthesis,
    Identifier,
    LeftBracket,
    RightBracket,
    Float,
    Integer,
    Dot,
    Space,
    NewLine,
    Tabulator,
    CarriageReturn,
    _get_values,
)
from ..util import command


@command("sql")
class SqlCommand(Command):
    pass


@command(r"--.*")
class SqlComment(Token):
    color = "ansibrightblack"


class SqlKeyword(Token, abc.ABC):
    color = "ansibrightblue"


@command(r"INSERT INTO", "INSERT")
class Insert(SqlKeyword):
    pass


@command(r"DELETE FROM", "DELETE")
class Delete(SqlKeyword):
    pass


@command(r"TRUNCATE TABLE", "TRUNCATE")
class Truncate(SqlKeyword):
    pass


@command(r"ORDER BY")
class OrderBy(SqlKeyword):
    pass


@command("ASCENDING", "ASC", default="ASC")
class Ascending(SqlKeyword):
    pass


@command("DESCENDING", "DESC", default="DESC")
class Descending(SqlKeyword):
    pass


@command("SELECT")
class Select(SqlKeyword):
    pass


@command("FROM")
class From(SqlKeyword):
    pass


@command("VALUES")
class Values(SqlKeyword):
    pass


@command("UPDATE")
class Update(SqlKeyword):
    pass


@command("SET")
class Set(SqlKeyword):
    pass


@command("WHERE")
class Where(SqlKeyword):
    pass


@command("AND", "&")
class And(SqlKeyword):
    pass


@command("OR", r"\|")
class Or(SqlKeyword):
    pass


sql_tokens = (
    SqlComment,
    String,
    Boolean,
    SqlCommand,
    Insert,
    Delete,
    Truncate,
    OrderBy,
    Ascending,
    Descending,
    Select,
    From,
    Values,
    Update,
    Set,
    Where,
    And,
    Or,
    NotEquals,
    GreaterEquals,
    LessEquals,
    Greater,
    Less,
    Equals,
    Asterisk,
    Divide,
    Plus,
    Minus,
    Comma,
    Semicolon,
    LeftParenthesis,
    RightParenthesis,
    LeftBracket,
    RightBracket,
    Identifier,
    Float,
    Integer,
    Dot,
    Space,
    NewLine,
    Tabulator,
    CarriageReturn,
)


sql_commands = _get_values(
    (
        Select,
        From,
        Where,
        Insert,
        Update,
        Delete,
        Truncate,
        Set,
        Values,
        And,
        Or,
        Ascending,
        Descending,
        OrderBy,
    )
)
