from typing import Sequence

from mypass.exceptions import InvalidSqlStatement
from mypass.lexer import Lexer
from mypass.tokens import Token


class Validator:

    def __init__(self, tokens: Sequence[Token]):
        self.tokens = tokens

    @classmethod
    def from_sql(cls, sql: str):
        return cls(Lexer(sql).get_tokens())

    @property
    def command_type(self):
        return self.tokens[0].standardized_value

    def validate(self):
        if self.tokens[0].type != 'COMMAND':
            raise InvalidSqlStatement('Statement must start with a COMMAND!')
        if self.command_type == 'SELECT':
            self.validate_select()
        elif self.command_type == 'INSERT INTO':
            self.validate_insert()
        ...

    def validate_select(self):
        print('SELECT validation will go here')

    def validate_insert(self):
        print('INSERT validation will go here')


x = Validator.from_sql('SELECT * FROM table1;')

print(x.validate())
