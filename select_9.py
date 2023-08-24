# Знайти список курсів, які відвідує студент.
from constants import *
from random import randint
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

student_id = randint(1, NUMBER_STUDENTS)
sql = f"""
SELECT s.student_name, sub.subject_name
FROM students s
JOIN grades g ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
WHERE g.student_id = {student_id}
GROUP BY sub.subject_name;
"""

print(execute_query(sql))
