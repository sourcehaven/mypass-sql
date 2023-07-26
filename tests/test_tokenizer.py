from mypass.tokens import *
from mypass.tokenizer import tokenize


def test_select():
    sql = 'SELECT * FROM people WHERE name="John" AND age=20'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0] == Select('SELECT', start=0, end=6)
    assert tokens[1] == Times('*', start=7, end=8)
    assert tokens[2] == From('FROM', start=9, end=13)


def test_insert():
    sql = 'INSERT INTO people (id, name, age) VALUES (1, "John", 25);'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0].name == INSERT and tokens[0].value == 'INSERT INTO'
    assert tokens[1].name == IDENTIFIER and tokens[1].value == 'people'
    assert tokens[2].name == LEFT_PARENTHESIS and tokens[2].value == '('
    assert tokens[3].name == IDENTIFIER and tokens[3].value == 'id'
    assert tokens[4].name == COMMA and tokens[4].value == ','
    assert tokens[5].name == IDENTIFIER and tokens[5].value == 'name'
    assert tokens[6].name == COMMA and tokens[6].value == ','
    assert tokens[7].name == IDENTIFIER and tokens[7].value == 'age'
    assert tokens[8].name == RIGHT_PARENTHESIS and tokens[8].value == ')'
    assert tokens[9].name == VALUES and tokens[9].value == 'VALUES'
    assert tokens[10].name == LEFT_PARENTHESIS and tokens[10].value == '('
    assert tokens[11].name == LITERAL and tokens[11].value == '1'
    assert tokens[12].name == COMMA and tokens[12].value == ','
    assert tokens[13].name == LITERAL and tokens[13].value == '"John"'
    assert tokens[14].name == COMMA and tokens[14].value == ','
    assert tokens[15].name == LITERAL and tokens[15].value == '25'
    assert tokens[16].name == RIGHT_PARENTHESIS and tokens[16].value == ')'
    assert tokens[17].name == SEMICOLON and tokens[17].value == ';'


def test_update():
    sql = "UPDATE Employees SET Department = 'Finance' WHERE EmployeeID = 101;"

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0].name == UPDATE and tokens[0].value == 'UPDATE'
    assert tokens[1].name == IDENTIFIER and tokens[1].value == 'Employees'
    assert tokens[2].name == SET and tokens[2].value == 'SET'
    assert tokens[3].name == IDENTIFIER and tokens[3].value == 'Department'
    assert tokens[4].name == EQUALS and tokens[4].value == '='
    assert tokens[5].name == LITERAL and tokens[5].value == "'Finance'"
    assert tokens[6].name == WHERE and tokens[6].value == 'WHERE'
    assert tokens[7].name == IDENTIFIER and tokens[7].value == 'EmployeeID'
    assert tokens[8].name == EQUALS and tokens[8].value == '='
    assert tokens[9].name == LITERAL and tokens[9].value == '101'


def test_delete():
    sql = 'DELETE FROM my_table WHERE x >= 5'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0].name == DELETE and tokens[0].value == 'DELETE FROM'
    assert tokens[1].name == IDENTIFIER and tokens[1].value == 'my_table'
    assert tokens[2].name == WHERE and tokens[2].value == 'WHERE'
    assert tokens[3].name == IDENTIFIER and tokens[3].value == 'x'
    assert tokens[4].name == GREATER_EQUALS and tokens[4].value == '>='
    assert tokens[5].name == LITERAL and tokens[5].value == '5'


def test_truncate():
    sql = 'TRUNCATE TABLE xy;'

    tokens = tokenize(sql, sql_tokens)

    assert tokens[0].name == TRUNCATE and tokens[0].value == 'TRUNCATE TABLE'
    assert tokens[1].name == IDENTIFIER and tokens[1].value == 'xy'
    assert tokens[2].name == SEMICOLON and tokens[2].value == ';'
