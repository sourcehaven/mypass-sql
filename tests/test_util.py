from mypass import find_between


def test_find_between():
    arr = ['a', 'b', 'c', 'd', 'e', 'f']

    assert find_between(arr, 'a', 'd') == ['b', 'c']
    assert find_between(arr, end_items='c') == ['a', 'b']
    assert find_between(arr, 'c') == ['d', 'e', 'f']
