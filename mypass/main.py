from lexer import lexer
from parser import parser

# Sample SQL-like input
sql_statement = "column1, column2"

# Give the lexer some input
lexer.input(sql_statement)

# Tokenize and print the result
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)

# Parse the input using the parser
result = parser.parse(sql_statement)
