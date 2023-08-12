from mypass import tokenize


def test_select():
    sql = 'SELECT * FROM people WHERE name="John" AND age=20'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0] == Select('SELECT', start=0, end=6)
    assert tokens[1] == Times('*', start=7, end=8)
    assert tokens[2] == From('FROM', start=9, end=13)


def test_insert():
    sql = 'INSERT INTO people (id, name, age) VALUES (1, "John", 25.5);'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0] == Insert('INSERT INTO')
    assert tokens[1] == Identifier('people')
    assert tokens[2] == LeftParenthesis('(')
    assert tokens[3] == Identifier('id')
    assert tokens[4] == Comma(',')
    assert tokens[5] == Identifier('name')
    assert tokens[6] == Comma(',')
    assert tokens[7] == Identifier('age')
    assert tokens[8] == RightParenthesis(')')
    assert tokens[9] == VALUES and tokens[9].value == 'VALUES'
    assert tokens[10] == LeftParenthesis('(')
    assert tokens[11] == LITERAL and tokens[11].value == '1'
    assert tokens[12] == Comma(',')
    assert tokens[13] == LITERAL and tokens[13].value == '"John"'
    assert tokens[14] == Comma(',')
    assert tokens[15] == Literal('25.5',) == 25.5
    assert tokens[16] == RightParenthesis(')')
    assert tokens[17] == Semicolon(';')


def test_update():
    sql = "UPDATE Employees SET Department = 'Finance' WHERE EmployeeID = 10;"

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0] == Update('UPDATE', 0, 6)
    assert tokens[1] == Identifier('Employees', 7, 16)
    assert tokens[2] == Set('SET',17, 20)
    assert tokens[3] == Identifier('Department', 21, 31)
    assert tokens[4] == Equals('=',32, 33)
    assert tokens[5] == String("'Finance'", 34, 43); assert tokens[5].cast_value() == 'Finance'
    assert tokens[6] == Where('WHERE', 44, 49)
    assert tokens[7] == Identifier('EmployeeID', 50, 60)
    assert tokens[8] == Equals('=', 61, 62)
    assert tokens[9] == Integer('10', 63, 65); assert tokens[9].cast_value() == 10


def test_delete():
    sql = 'DELETE FROM my_table WHERE x >= 5'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0] == Delete('DELETE FROM', 0, 11)
    assert tokens[1] == Identifier('my_table', 12, 20)
    assert tokens[2] == Where('WHERE', 21, 26)
    assert tokens[3] == Identifier('x', 27, 28)
    assert tokens[4] == GreaterEquals('>=', 29, 31)
    assert tokens[5] == Literal('5',  32, 33)


def test_truncate():
    sql = 'TRUNCATE TABLE xy;'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0] == Truncate('TRUNCATE TABLE', 0, 14)
    assert tokens[1] == Identifier('xy', 15, 17)
    assert tokens[2] == Semicolon(';', 17, 18)
