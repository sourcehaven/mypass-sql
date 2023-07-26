from typing import Iterable


def is_between_any(span: tuple[int, int], spans: Iterable[tuple[int, int]]):
    """

    >>> is_between_any((2, 3), [(1, 4), (6, 12)])
    True

    >>> is_between_any((2, 3), [(0, 1), (4, 6), (6, 12)])
    False
    """
    for s in spans:
        if s[0] <= span[0] <= s[1] or s[0] <= span[1] <= s[1]:
            return True

    return False


def is_not_between_any(span: tuple[int, int], spans: Iterable[tuple[int, int]]):
    for s in spans:
        if s[0] <= span[0] and span[1] <= s[1]:
            return False

    return True


def is_non_overlapping(span: tuple[int, int], spans: Iterable[tuple[int, int]]):
    for s in spans:
        if span[0] < s[1] and span[1] > s[0]:
            return False

    return True
