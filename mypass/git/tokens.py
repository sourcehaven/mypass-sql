import re

from ..command.tokens import Command
from ..tokens import Space, ShortOption, LongOption, _get_keywords


class GitCommand(Command):
    pattern = re.compile(r'\bgit\b')


class Add(GitCommand):
    pattern = re.compile(r'\badd\b')


class Am(GitCommand):
    pattern = re.compile(r'\bam\b')


class Archive(GitCommand):
    pattern = re.compile(r'\barchive\b')


class Bisect(GitCommand):
    pattern = re.compile(r'\bbisect\b')


class Blame(GitCommand):
    pattern = re.compile(r'\bblame\b')


class Branch(GitCommand):
    pattern = re.compile(r'\bbranch\b')


class Bundle(GitCommand):
    pattern = re.compile(r'\bbundle\b')


class Checkout(GitCommand):
    pattern = re.compile(r'\bcheckout\b')


class CherryPick(GitCommand):
    pattern = re.compile(r'\bcherry-pick\b')


class Clean(GitCommand):
    pattern = re.compile(r'\bclean\b')


class Clone(GitCommand):
    pattern = re.compile(r'\bclone\b')


class Commit(GitCommand):
    pattern = re.compile(r'\bcommit\b')


class Describe(GitCommand):
    pattern = re.compile(r'\bdescribe\b')


class Diff(GitCommand):
    pattern = re.compile(r'\bdiff\b')


class Fetch(GitCommand):
    pattern = re.compile(r'\bfetch\b')


class FormatPatch(GitCommand):
    pattern = re.compile(r'\bformat-patch\b')


class Grep(GitCommand):
    pattern = re.compile(r'\bgrep\b')


class Init(GitCommand):
    pattern = re.compile(r'\binit\b')


class Log(GitCommand):
    pattern = re.compile(r'\blog\b')


class Merge(GitCommand):
    pattern = re.compile(r'\bmerge\b')


class Move(GitCommand):
    pattern = re.compile(r'\bmv\b')


class Pull(GitCommand):
    pattern = re.compile(r'\bpull\b')


class Push(GitCommand):
    pattern = re.compile(r'\bpush\b')


class Rebase(GitCommand):
    pattern = re.compile(r'\brebase\b')


class Reset(GitCommand):
    pattern = re.compile(r'\breset\b')


class Restore(GitCommand):
    pattern = re.compile(r'\brestore\b')


class Revert(GitCommand):
    pattern = re.compile(r'\brevert\b')


class Remove(GitCommand):
    pattern = re.compile(r'\brm\b')


class Reflog(GitCommand):
    pattern = re.compile(r'\breflog\b')


class Show(GitCommand):
    pattern = re.compile(r'\bshow\b')


class Stash(GitCommand):
    pattern = re.compile(r'\bstash\b')


class Status(GitCommand):
    pattern = re.compile(r'\bstatus\b')


class Submodule(GitCommand):
    pattern = re.compile(r'\bsubmodule\b')


class Switch(GitCommand):
    pattern = re.compile(r'\bswitch\b')


class Tag(GitCommand):
    pattern = re.compile(r'\btag\b')


class CustomGitCommand(GitCommand):
    pass


class AutoCommit(CustomGitCommand):
    pattern = re.compile(r'\bauto-commit\b')


class AutoPush(CustomGitCommand):
    pattern = re.compile(r'\bauto-push\b')


primary_keywords = (GitCommand,)
secondary_keywords = (
    Add, Am, Archive, Bisect, Blame, Branch, Bundle, Checkout, CherryPick, Clean,
    Clone, Commit, Describe, Diff, Fetch, FormatPatch, Grep, Init, Log, Merge,
    Move, Pull, Push, Rebase, Reset, Restore, Revert, Remove, Reflog, Show, Stash,
    Status, Submodule, Switch, Tag, AutoCommit, AutoPush
)

tokens = (
    Space, LongOption, ShortOption,
    *primary_keywords, *secondary_keywords,
)

primary_keywords = tuple(_get_keywords(primary_keywords))
secondary_keywords = tuple(_get_keywords(secondary_keywords))
