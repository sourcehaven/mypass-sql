from typing import Optional, Iterable, Sequence

from ..tokens import Token, _get_values, Identifier, Equals, Comma, Integer, Float, String, Space, Pipe, Literal
from ..util import command


class Command(Token):
    color = "ansigreen"


@command("create", "add", "new", default="add")
class Add(Command):
    pass


@command("clear", "cls", default="cls", windows="cls", linux="clear")
class Cls(Command):
    pass


@command("copy", "cp", default="copy", windows="copy", linux="cp")
class Copy(Command):
    pass


@command("pwd", "chdir", default="pwd")
class Pwd(Command):
    """Print working directory"""
    pass


@command("cd")
class Cd(Command):
    """Change directory"""
    pass


@command("delete", "remove", "rm", "del", default="del", windows="del", linux="rm")
class Remove(Command):
    pass


@command("exit", "quit", "q", default="exit")
class Exit(Command):
    pass


@command("help")
class Help(Command):
    pass


@command("history", "hist")
class History(Command):
    pass


@command("host")
class Host(Command):
    pass


@command("list", "dir", "ls", default="ls")
class List(Command):
    pass


@command("mkdir", "md")
class MkDir(Command):
    pass


@command("port")
class Port(Command):
    pass


@command("show", "grep", "find", default="show", linux="grep", windows="find")
class Show(Command):
    pass


@command("update", "change", default="update")
class Update(Command):
    pass


@command("whoami")
class WhoAmI(Command):
    pass


class CommandHierarchy:

    def __init__(self, hierarchy: dict):
        self.hierarchy = hierarchy

    def validate_tokens(self, tokens: Sequence[Token]):
        for i, token in enumerate(tokens):
            if type(token) in self.hierarchy:
                self.hierarchy = self.hierarchy[type(token)]


command_tokens = (
    Add,
    Cls,
    Copy,
    Pwd,
    Remove,
    Exit,
    Help,
    History,
    Host,
    List,
    MkDir,
    Port,
    Show,
    Update,
    WhoAmI,
    Pipe,
    String,
    Identifier,
    Integer,
    Float,
    Equals,
    Comma,
    Space,
)



commands = _get_values(command_tokens)
