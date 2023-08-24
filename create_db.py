import sqlite3


def create_db():
    with open('university.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.executescript(sql)


if __name__ == "__main__":
    create_db()
