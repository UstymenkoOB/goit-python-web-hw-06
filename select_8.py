# Знайти середній бал, який ставить певний викладач зі своїх предметів.
from constants import *
from random import randint
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

teacher_id = randint(1, NUMBER_TEACHERS)
sql = f"""
SELECT t.teacher_name, AVG(g.grade) as average_grade
FROM teachers t
JOIN grades g ON g.teacher_id = t.id
WHERE g.teacher_id = {teacher_id};
"""

print(execute_query(sql))
