from mypass.sql.tokenizer import tokenize
from mypass.sql.tokens import Select, From, Truncate, Delete, Where, Set, Update, Insert, Values
from mypass.tokens import (
    Asterisk, Semicolon, Identifier, Space, GreaterEquals, Integer, Equals, String,
    RightParenthesis, Comma, LeftParenthesis, Float
)


def test_select():
    sql = 'SELECT * FROM people WHERE name="John" AND age=20'

    tokens = tokenize(sql, remove_spaces=True)

    assert tokens[0] == Select('SELECT', start=0, end=6)
    assert tokens[1] == Asterisk('*', start=7, end=8)
    assert tokens[2] == From('FROM', start=9, end=13)


def test_insert():
    sql = 'INSERT INTO people (id, name, age) VALUES (1, "John", 25.5);'

    tokens = tokenize(sql, remove_spaces=True)

    assert tokens[0].exact_eq(Insert('INSERT INTO', 0, 11, 1))
    assert tokens[1].exact_eq(Identifier('people', 12, 18, 1))
    assert tokens[2].exact_eq(LeftParenthesis('(', 19, 20, 1))
    assert tokens[3].exact_eq(Identifier('id', 20, 22, 1))
    assert tokens[4].exact_eq(Comma(',', 22, 23, 1))
    assert tokens[5].exact_eq(Identifier('name', 24, 28, 1))
    assert tokens[6].exact_eq(Comma(',', 28, 29, 1))
    assert tokens[7].exact_eq(Identifier('age', 30, 33, 1))
    assert tokens[8].exact_eq(RightParenthesis(')', 33, 34, 1))
    assert tokens[9].exact_eq(Values('VALUES', 35, 41, 1))
    assert tokens[10].exact_eq(LeftParenthesis('(', 42, 43, 1))
    assert tokens[11].exact_eq(Integer('1', 43, 44, 1))
    assert tokens[11].true_value() == 1
    assert tokens[12].exact_eq(Comma(',', 44, 45, 1))
    assert tokens[13].exact_eq(String('"John"', 46, 52, 1))
    assert tokens[13].true_value() == 'John'
    assert tokens[14].exact_eq(Comma(',', 52, 53, 1))
    assert tokens[15].exact_eq(Float('25.5', 54, 58, 1))
    assert tokens[15].true_value() == 25.5
    assert tokens[16].exact_eq(RightParenthesis(')', 58, 59, 1))
    assert tokens[17].exact_eq(Semicolon(';', 59, 60, 1))


def test_update():
    sql = "UPDATE Employees SET Department = 'Finance' WHERE EmployeeID = 10;"

    tokens = tokenize(sql, remove_spaces=True)

    assert tokens[0].exact_eq(Update('UPDATE', 0, 6, 1))
    assert tokens[1].exact_eq(Identifier('Employees', 7, 16, 1))
    assert tokens[2].exact_eq(Set('SET', 17, 20, 1))
    assert tokens[3].exact_eq(Identifier('Department', 21, 31, 1))
    assert tokens[4].exact_eq(Equals('=', 32, 33, 1))
    assert tokens[5].exact_eq(String("'Finance'", 34, 43, 1))
    assert tokens[5].true_value() == 'Finance'
    assert tokens[6].exact_eq(Where('WHERE', 44, 49, 1))
    assert tokens[7].exact_eq(Identifier('EmployeeID', 50, 60, 1))
    assert tokens[8].exact_eq(Equals('=', 61, 62, 1))
    assert tokens[9].exact_eq(Integer('10', 63, 65, 1))
    assert tokens[9].true_value() == 10


def test_delete():
    sql = 'DELETE FROM my_table WHERE x >= 5'

    tokens = tokenize(sql, remove_spaces=True)

    assert tokens[0].exact_eq(Delete('DELETE FROM', 0, 11, 1))
    assert tokens[1].exact_eq(Identifier('my_table', 12, 20, 1))
    assert tokens[2].exact_eq(Where('WHERE', 21, 26, 1))
    assert tokens[3].exact_eq(Identifier('x', 27, 28, 1))
    assert tokens[4].exact_eq(GreaterEquals('>=', 29, 31, 1))
    assert tokens[5].exact_eq(Integer('5',  32, 33, 1))


def test_truncate():
    sql = 'TRUNCATE TABLE xy;'

    tokens = tokenize(sql)

    assert tokens[0].exact_eq(Truncate('TRUNCATE TABLE', 0, 14, 1))
    assert tokens[1].exact_eq(Space(' ', 14, 15, 1))
    assert tokens[2].exact_eq(Identifier('xy', 15, 17, 1))
    assert tokens[3].exact_eq(Semicolon(';', 17, 18, 1))
