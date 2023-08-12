def test_token_pattern():
    s1 = Select.pattern.search('SELECT')
    assert s1.group() == 'SELECT'
    assert s1.span() == (0, 6)

    s2 = Select.pattern.search('SeL SelEcT')
    assert s2.group() == 'SelEcT'
    assert s2.span() == (4, 10)


def test_token_equality():
    select = Select('SELECT', 0, 6)

    assert select == Select('SELECT', 0, 6)
    assert select != Select('SeLecT', 0, 6)
    assert select != Select('SELECT', 2, 8)
    assert select != Identifier('SELECT', 0, 6)
