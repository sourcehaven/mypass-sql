class SqlException(RuntimeError):
    pass


class InvalidSqlStatement(SqlException):
    pass


class UnsupportedSqlStatement(SqlException):
    pass


class InvalidTokenException(Exception):
    pass
