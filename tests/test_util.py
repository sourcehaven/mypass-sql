from mypass.util import find_between


def test_find_between():
    arr = ['a', 'b', 'c', 'd', 'e', 'f']

    assert find_between(arr, 'a', 'd') == (1, 3)
    assert find_between(arr, end_items='c') == (0, 2)
    assert find_between(arr, 'c') == (3, None)
