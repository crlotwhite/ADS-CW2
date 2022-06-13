import sqlite3

from common.metaclass.singleton import SingletonMetaclass
from .type import DVD


class DVDController(metaclass=SingletonMetaclass):
    query_dict = {
        'init': 'CREATE TABLE dvd(id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, stars TEXT, producer TEXT, director TEXT, production_company TEXT, copies INTEGER, total_quantity INTEGER)',
        'create': 'INSERT INTO dvd(name, starts, producer, director, production_company, copies, total_quantity) values (?, ?, ?, ?, ?, ?, ?)',
        'update': 'UPDATE dvd SET {} = {} WHERE id = {}',
        'delete': 'DELETE FROM dvd WHERE id = {}',
        'read': 'SELECT * FROM dvd WHERE id = {}',
        'read_all': 'SELECT * FROM dvd',
    }

    def __init__(self):
        self.conn = sqlite3.connect("dvd.db")
        self.conn.row_factory = sqlite3.Row
        self.cur = self.conn.cursor()
        try:
            self.cur.execute(self.query_dict['init'])
        except sqlite3.OperationalError:
            # if it is already existed.
            pass

        self.conn.commit()

    def __del__(self):
        self.conn.close()

    def add(self, name, starts, producer, director, production_company, total_quantity):
        copies = total_quantity
        self.cur.execute(
            self.query_dict['create'],
            (name, starts, producer, director, production_company, copies, total_quantity)
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
                DVD(
                    db_id=row['id'],
                    name=row['name'],
                    stars=row['stars'],
                    producer=row['producer'],
                    director=row['director'],
                    production_company=row['production_company'],
                    copies=row['copies'],
                    total_quantity=row['total_quantity']
                )
            )
        else:
            return result

    def fetch(self, db_id):
        self.cur.execute(self.query_dict['read'].format(db_id))

        row = self.cur.fetchone()

        return DVD(
            db_id=row['id'],
            name=row['name'],
            stars=row['stars'],
            producer=row['producer'],
            director=row['director'],
            production_company=row['production_company'],
            copies=row['copies'],
            total_quantity=row['total_quantity']
        )

from os import getcwd