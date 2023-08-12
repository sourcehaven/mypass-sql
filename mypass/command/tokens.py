import re

from ..tokens import Command, SubCommand, _get_keywords


class Quit(Command):
    pattern = re.compile(r'QUIT|EXIT', re.I)


class Help(Command):
    pattern = re.compile(r'HELP', re.I)


class Clear(Command):
    pattern = re.compile(r'CLEAR\s+SCREEN|CLEAR|CLS', re.I)


class History(Command):
    pattern = re.compile(r'HISTORY', re.I)


class Host(Command):
    pattern = re.compile(r'HOST', re.I)


class Port(Command):
    pattern = re.compile(r'PORT', re.I)


class Vault(Command):
    pattern = re.compile(r'VAULT', re.I)


class Master(Command):
    pattern = re.compile(r'MASTER', re.I)


class Create(SubCommand):
    pattern = re.compile(r'ADD|CREATE|NEW|INSERT', re.I)


class Read(SubCommand):
    pattern = re.compile(r'READ|SELECT|GET', re.I)


class Update(SubCommand):
    pattern = re.compile('UPDATE|CHANGE', re.I)


class Delete(SubCommand):
    pattern = re.compile(r'DELETE|REMOVE', re.I)


class Copy(SubCommand):
    pattern = re.compile(r'COPY', re.I)


class List(SubCommand):
    pattern = re.compile(r'LIST|SHOW', re.I)


command_tokens = Clear, Quit, History, Help, Host, Port, Vault, Master
subcommand_tokens = Create, Read, Update, Delete, Copy, List

tokens = *command_tokens, *subcommand_tokens

primary_keywords = tuple(_get_keywords(command_tokens))
secondary_keywords = tuple(_get_keywords(subcommand_tokens))
