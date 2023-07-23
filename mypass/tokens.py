import re
import copy


SELECT = 'SELECT'
STAR = 'STAR'
COMMA = 'COMMA'
EQUALS = 'EQUALS'
LEFT_PARENTHESIS = 'LEFT_PARENTHESIS'
RIGHT_PARENTHESIS = 'RIGHT_PARENTHESIS'
FROM = 'FROM'
INSERT = 'INSERT'
UPDATE = 'UPDATE'
SET = 'SET'
DELETE = 'DELETE'
TRUNCATE = 'TRUNCATE'
WHERE = 'WHERE'
AND = 'AND'
OR = 'OR'
ORDER_BY = 'ORDER_BY'
ASCENDING = 'ASCENDING'
DESCENDING = 'DESCENDING'
LITERAL = 'LITERAL'
IDENTITY = 'IDENTITY'
NEW_LINE = 'NEW_LINE'
SEMICOLON = 'SEMICOLON'
IDENTIFIER = 'IDENTIFIER'


class Token:

    __slots__ = 'id', 'pattern', 'compiled_pattern', 'value', 'line_no', 'start', 'end'

    def __init__(self, id: str, pattern: str, flags: int | re.RegexFlag = 0):
        self.id = id
        self.pattern = pattern
        self.compiled_pattern = re.compile(pattern=pattern, flags=flags)

        self.value = None
        self.line_no = None
        self.start = None
        self.end = None

    def copy(self, value: str = None, line_no: int = None, start: int = None, end: int = None):
        """Create a copy of the Token object with optional parameters."""

        new = copy.copy(self)

        if value is not None:
            new.value = value
        if line_no is not None:
            new.line_no = line_no
        if start is not None:
            new.start = start
        if end is not None:
            new.end = end

        return new

    def match(self, string: str):
        """Try to apply the pattern at the start of the string, returning
        a Match object, or None if no match was found."""
        return self.compiled_pattern.match(string=string)

    def findall(self, string: str):
        """Return a list of all non-overlapping matches in the string.

        If one or more capturing groups are present in the pattern, return
        a list of groups; this will be a list of tuples if the pattern
        has more than one group.

        Empty matches are included in the result."""
        return self.compiled_pattern.findall(string=string)

    def finditer(self, string: str):
        """Return an iterator over all non-overlapping matches in the
        string.  For each match, the iterator returns a Match object.

        Empty matches are included in the result."""
        return self.compiled_pattern.finditer(string=string)

    def count(self, string: str):
        count = 0
        for _ in self.finditer(string):
            count += 1
        return count

    def fullmatch(self, string):
        """Try to apply the pattern to all the string, returning
        a Match object, or None if no match was found."""
        return self.compiled_pattern.fullmatch(string=string)

    def search(self, string):
        """Scan through string looking for a match to the pattern, returning
        a Match object, or None if no match was found."""
        return self.compiled_pattern.search(string=string)

    def span(self):
        return self.start, self.end

    def __repr__(self):
        return f"Token(id={self.id!r}, pattern=r'{self.pattern}', span={self.span()!r}, value={self.value!r})"


sql_tokens = (
    Token(SELECT, r'\bSELECT\b', re.IGNORECASE),
    Token(FROM, r'\bFROM\b', re.IGNORECASE),
    Token(INSERT, r'\bINSERT\b|\bINSERT\s+INTO\b', re.IGNORECASE),
    Token(UPDATE, r'\bUPDATE\b', re.IGNORECASE),
    Token(SET, r'\bSET\b', re.IGNORECASE),
    Token(DELETE, r'\bDELETE\b|\bDELETE\s+FROM\b', re.IGNORECASE),
    Token(TRUNCATE, r'\bTRUNCATE\b|TRUNCATE\s+TABLE\b', re.IGNORECASE),
    Token(WHERE, r'\bWHERE\b', re.IGNORECASE),
    Token(AND, r'\bAND\b|\b&\b', re.IGNORECASE),
    Token(OR, r'\bOR\b|\b\|\b', re.IGNORECASE),
    Token(ORDER_BY, r'\bORDER\s+BY\b', re.IGNORECASE),
    Token(ASCENDING, r'\bASC\b|\bASCENDING\b|\b↑\b', re.IGNORECASE),
    Token(DESCENDING, r'\bDESC\b|\bDESCENDING\b|\b↓\b', re.IGNORECASE),
    Token(STAR, r'\*'),
    Token(COMMA, r','),
    Token(EQUALS, r'='),
    Token(LEFT_PARENTHESIS, r'\('),
    Token(RIGHT_PARENTHESIS, r'\)'),
    Token(NEW_LINE, r'\n'),
    Token(SEMICOLON, r';'),
    Token(LITERAL, r'\b(\d*\.\d+|\d+\.\d*|\d+|"[^"]*"|\'[^\']*\'|True|False)\b'),
    Token(IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
)
