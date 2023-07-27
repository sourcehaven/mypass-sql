from typing import Iterable


def is_between_any(span: tuple[int, int], spans: Iterable[tuple[int, int]]):
    """
    Check if the given span is fully contained within any of the spans in the iterable.

    Args:
        span (tuple[int, int]): The span to check, represented as a tuple of two integers (start and end points).
        spans (Iterable[tuple[int, int]]): An iterable of spans, where each span is represented as a tuple of two integers.

    Returns:
        bool: True if the given span is fully contained within any of the spans in the iterable; otherwise, False.

    Doctests:
        >>> is_between_any((5, 10), [(1, 8), (5, 12), (15, 20)])
        True

        >>> is_between_any((1, 2), [(0, 2)])
        True

        >>> is_between_any((1, 6), [(6, 8), (10, 15)])
        False

        >>> is_between_any((1, 6), [])
        False
    """
    for s in spans:
        if span[0] >= s[0] and span[1] >= s[1]:
            return True
    return False


def is_overlapping(span: tuple[int, int], spans: Iterable[tuple[int, int]]):
    """Check if the given span is overlapping with any of the spans in the iterable.

    Args:
        span (tuple[int, int]): The span to check, represented as a tuple of two integers (start and end points).
        spans (Iterable[tuple[int, int]]): An iterable of spans, where each span is represented as a tuple of two integers.

    Returns:
        bool: True if the given span overlaps with any of the spans in the iterable; otherwise, False.

    Doctests:
        >>> is_overlapping((2, 6), [(4, 5)])
        True

        >>> is_overlapping((2, 6), [(4, 8)])
        True

        >>> is_overlapping((2, 6), [(0, 4)])
        True

        >>> is_overlapping((2, 6), [(0, 1)])
        False

        >>> is_overlapping((2, 6), [(7, 12)])
        False
    """

    for s in spans:

        if span[1] >= s[0] and span[0] <= s[1]:
            return True

    return False


def is_non_overlapping(span: tuple[int, int], spans: Iterable[tuple[int, int]]):
    """
    Check if the given span is non-overlapping with all the spans in the iterable.

    Args:
        span (tuple[int, int]): The span to check, represented as a tuple of two integers (start and end points).
        spans (Iterable[tuple[int, int]]): An iterable of spans, where each span is represented as a tuple of two integers.

    Returns:
        bool: True if the given span does not overlap with any of the spans in the iterable; otherwise, False.

    Doctests:
        >>> is_non_overlapping((2, 6), [(4, 5)])
        False

        >>> is_non_overlapping((2, 6), [(4, 8)])
        False

        >>> is_non_overlapping((2, 6), [(0, 4)])
        False

        >>> is_non_overlapping((2, 6), [(0, 1)])
        True

        >>> is_non_overlapping((2, 6), [(7, 12)])
        True
    """
    for s in spans:
        if span[0] < s[1] and span[1] > s[0]:
            return False

    return True


def cast(text: str, remove_quotes=True):
    """
    Convert the input text to the appropriate data type based on its content.

    This function performs type conversion on the input text, returning a Python data type that best represents
    the content of the text. It supports conversion to bool, int, float, and retains the original text as a string
    if no other conversion is possible.

    Args:
        text (str): The text to be converted to a suitable data type.
        remove_quotes (bool, optional): Flag to determine if surrounding quotes should be removed for string values.
            Defaults to True.

    Returns:
        Union[bool, int, float, str]: The converted value. Returns a boolean True or False if the input text is
        'true' or 'false' (case-insensitive). Returns an integer if the input text is an integer. Returns a float
        if the input text is a float. Otherwise, returns the original text as a string.

    Doctests:
        >>> cast('true')
        True

        >>> cast('42')
        42

        >>> cast('3.14')
        3.14

        >>> cast('Hello, World!')
        'Hello, World!'

        >>> cast("'quoted string'")
        'quoted string'
    """
    if text.lower() == 'true':
        return True
    elif text.lower() == 'false':
        return False
    try:
        return int(text)
    except ValueError:
        try:
            return float(text)
        except ValueError:
            if remove_quotes:
                if (text.startswith("'") and text.endswith("'")) or (text.startswith('"') and text.endswith('"')):
                    return text[1:-1]

            return text
