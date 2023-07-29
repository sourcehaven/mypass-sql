class ItemNotFound(Exception):
    pass


class SqlSyntaxError(Exception):

    def __init__(self, msg: str):
        self.msg = f'Syntax error: {msg}'

        super().__init__(self.msg)

    @classmethod
    def from_token(cls, token, expected=None):
        msg = (f'Invalid {token.value!r} at line {token.line_no}, '
               f'from character {token.start} to {token.end}.')

        if expected is not None:
            msg += f' Expected {expected!r}.'

        return cls(msg)
