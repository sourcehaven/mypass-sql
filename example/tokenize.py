from mypass.sql.tokenizer import tokenize


def main():
    sql_query = 'SELECT * FROM table WHERE x > 5;'

    tokens = tokenize(sql_query)

    for token in tokens:
        print(token.__repr__())

    return tokens


if __name__ == "__main__":
    main()
