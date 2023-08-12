from .tokens import tokens
from ..tokenizer import tokenize as main_tokenizer


def tokenize(string: str, remove_spaces: bool = False):
    return main_tokenizer(string, tokens=tokens, remove_spaces=remove_spaces)
