# Знайти, які курси читає певний викладач.
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
SELECT t.teacher_name, sub.subject_name
FROM subjects sub
JOIN teachers t ON t.id = sub.teacher_id
WHERE t.id = {teacher_id};
"""

print(execute_query(sql))
