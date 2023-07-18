import unittest

from mypass.parser import SqlStatement


class TestSum(unittest.TestCase):

    def test_multiple(self):
        multiple = SqlStatement.from_multiple('; ;; SELECT * FROM table1 WHERE a=5 AND b=3; ;;TRUNCATE TABLE table1;;')
        self.assertEqual(len(multiple), 2)
        self.assertEqual(multiple[0].sql, 'SELECT * FROM table1 WHERE a=5 AND b=3')
        self.assertEqual(multiple[1].sql, 'TRUNCATE TABLE table1')

    def test_select(self):
        query1 = SqlStatement('SELECT * FROM table1;')
        self.assertEqual(query1.command, 'SELECT')
        self.assertEqual(query1.fields, ['*'])
        self.assertEqual(query1.table, 'table1')
        self.assertEqual(query1.where, None)
        self.assertEqual(query1.order_by, None)

        query2 = SqlStatement('SELECT id, name, age FROM table1 WHERE id=2 AND name="John" ORDER BY id DESC, name, age ASCENDING;')
        self.assertEqual(query2.command, 'SELECT')
        self.assertEqual(query2.fields, ['id', 'name', 'age'])
        self.assertEqual(query2.table, 'table1')
        self.assertEqual(query2.where.value, 'id=2 AND name="John"')
        self.assertEqual(query2.order_by, {'id': 'DESC', 'name': 'ASC', 'age': 'ASC'})

    def test_truncate(self):
        truncate = SqlStatement('TRUNCATE table1;')
        self.assertEqual(truncate.command, 'TRUNCATE')
        self.assertEqual(truncate.table, 'table1')
        self.assertEqual(truncate.where, None)
        self.assertEqual(truncate.fields, None)
        self.assertEqual(truncate.order_by, None)

        truncate = SqlStatement('TRUNCATE TABLE table1;')
        self.assertEqual(truncate.command, 'TRUNCATE')
        self.assertEqual(truncate.table, 'table1')
        self.assertEqual(truncate.where, None)
        self.assertEqual(truncate.fields, None)
        self.assertEqual(truncate.order_by, None)



if __name__ == '__main__':
    unittest.main()
