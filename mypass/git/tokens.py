from ..command.tokens import Command
from ..tokens import _get_values
from ..util import command


@command("git", word_boundary=True)
class GitCommand(Command):
    pass


@command("add", word_boundary=True)
class Add(GitCommand):
    pass


@command("am", word_boundary=True)
class Am(GitCommand):
    pass


@command("archive", word_boundary=True)
class Archive(GitCommand):
    pass


@command("bisect", word_boundary=True)
class Bisect(GitCommand):
    pass


@command("blame", word_boundary=True)
class Blame(GitCommand):
    pass


@command("branch", word_boundary=True)
class Branch(GitCommand):
    pass


@command("bundle", word_boundary=True)
class Bundle(GitCommand):
    pass


@command("checkout", word_boundary=True)
class Checkout(GitCommand):
    pass


@command("cherry-pick", word_boundary=True)
class CherryPick(GitCommand):
    pass


@command("clean", word_boundary=True)
class Clean(GitCommand):
    pass


@command("clone", word_boundary=True)
class Clone(GitCommand):
    pass


@command("commit", word_boundary=True)
class Commit(GitCommand):
    pass


@command("describe", word_boundary=True)
class Describe(GitCommand):
    pass


@command("diff", word_boundary=True)
class Diff(GitCommand):
    pass


@command("fetch", word_boundary=True)
class Fetch(GitCommand):
    pass


@command("format-patch", word_boundary=True)
class FormatPatch(GitCommand):
    pass


@command("grep", word_boundary=True)
class Grep(GitCommand):
    pass


@command("init", word_boundary=True)
class Init(GitCommand):
    pass


@command("log", word_boundary=True)
class Log(GitCommand):
    pass


@command("merge", word_boundary=True)
class Merge(GitCommand):
    pass


@command("mv", word_boundary=True)
class Move(GitCommand):
    pass


@command("pull", word_boundary=True)
class Pull(GitCommand):
    pass


@command("push", word_boundary=True)
class Push(GitCommand):
    pass


@command("rebase", word_boundary=True)
class Rebase(GitCommand):
    pass


@command("reset", word_boundary=True)
class Reset(GitCommand):
    pass


@command("restore", word_boundary=True)
class Restore(GitCommand):
    pass


@command("revert", word_boundary=True)
class Revert(GitCommand):
    pass


@command("rm", word_boundary=True)
class Remove(GitCommand):
    pass


@command("reflog", word_boundary=True)
class Reflog(GitCommand):
    pass


@command("show", word_boundary=True)
class Show(GitCommand):
    pass


@command("stash", word_boundary=True)
class Stash(GitCommand):
    pass


@command("status", word_boundary=True)
class Status(GitCommand):
    pass


@command("submodule", word_boundary=True)
class Submodule(GitCommand):
    pass


@command("switch", word_boundary=True)
class Switch(GitCommand):
    pass


@command("tag", word_boundary=True)
class Tag(GitCommand):
    pass


class CustomGitCommand(GitCommand):
    pass


@command("auto-commit", word_boundary=True)
class AutoCommit(CustomGitCommand):
    pass


@command("auto-push", word_boundary=True)
class AutoPush(CustomGitCommand):
    pass


git_tokens = (
    GitCommand,
    Add,
    Am,
    Archive,
    Bisect,
    Blame,
    Branch,
    Bundle,
    Checkout,
    CherryPick,
    Clean,
    Clone,
    Commit,
    Describe,
    Diff,
    Fetch,
    FormatPatch,
    Grep,
    Init,
    Log,
    Merge,
    Move,
    Pull,
    Push,
    Rebase,
    Reset,
    Restore,
    Revert,
    Remove,
    Reflog,
    Show,
    Stash,
    Status,
    Submodule,
    Switch,
    Tag,
    AutoCommit,
    AutoPush,
)


git_commands = _get_values(git_tokens)
