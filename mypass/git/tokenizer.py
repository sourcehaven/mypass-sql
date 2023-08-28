from .tokens import git_tokens
from ..tokenizer import tokenize as main_tokenizer


def tokenize(string: str, remove_spaces=False):
    return main_tokenizer(string, tokens=git_tokens, remove_spaces=remove_spaces)
