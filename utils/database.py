from utils.database_connections.database_con import DatabaseConnection

from typing import List, Dict, Union
"""
Concerned with storing and retrieving books from a json file
"""
Book = Dict[str, Union[str, int]]


def create_book_table() -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        sql = 'CREATE TABLE IF NOT EXISTS books(' \
              'id integer primary key,' \
              'name text,' \
              'author text,' \
              'read integer)'
        cursor.execute(sql)


def add_book(name: str, author: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        sql = "INSERT INTO books VALUES(null, ?, ?, ?)"
        cursor.execute(sql, (name, author, 0))


def get_all_books() -> List[Book]:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        sql = 'SELECT name, author, read FROM books'
        cursor.execute(sql)
        books = [{'name': row[0], 'author': row[1], 'read': row[2]}
                 for row in cursor.fetchall()]
        return books


def mark_book_as_read(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        sql = 'UPDATE books SET read=1 WHERE name=?'
        cursor.execute(sql, (name,))


def delete_book(name: str) -> None:
    with DatabaseConnection('data.db') as connection:
        cursor = connection.cursor()
        sql = 'DELETE FROM books WHERE name=?'
        cursor.execute(sql, (name,))


create_book_table()
