import sqlite3

from common.metaclass.singleton import SingletonMetaclass
from .type import Customer


class CustomerController(metaclass=SingletonMetaclass):
    query_dict = {
        'init': 'CREATE TABLE customer(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, rented_dvd TEXT)',
        'create': 'INSERT INTO customer(name, rented_dvd) values (?, ?)',
        'update': 'UPDATE customer SET {} = {} WHERE id = {}',
        'delete': 'DELETE FROM customer WHERE id = {}',
        'read': 'SELECT * FROM customer WHERE id = {}',
        'read_all': 'SELECT * FROM customer',
    }

    def __init__(self):
        self.conn = sqlite3.connect("customer.db")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(self.query_dict['init'])
        except sqlite3.OperationalError:
            # if it is already existed
            pass

        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def add(self, name):
        rented_dvd = ''
        self.cur.execute(
            self.query_dict['create'],
            (name, rented_dvd)
        )
        self.conn.commit()
        return self.cur.lastrowid

    def update(self, db_id, **kwargs):
        for field, value in kwargs.items():
            self.cur.execute(
                self.query_dict['update'].format(
                    field,
                    value if isinstance(value, int) else f'"{value}"',
                    db_id
                )
            )
        else:
            self.conn.commit()

    def delete(self, db_id):
        self.cur.execute(self.query_dict['delete'].format(db_id))
        self.conn.commit()

    def fetch_all(self):
        result = []

        self.cur.execute(self.query_dict['read_all'])
        for row in self.cur.fetchall():
            result.append(
                Customer(
                    db_id=row['id'],
                    name=row['name'],
                    rented_dvd=row['rented_dvd'].split(',') if row['rented_dvd'] != '' else [],
                )
            )
        else:
            return result

    def fetch(self, db_id):
        self.cur.execute(self.query_dict['read'].format(db_id))

        row = self.cur.fetchone()

        return Customer(
            db_id=row['id'],
            name=row['name'],
            rented_dvd=row['rented_dvd'],
        )
