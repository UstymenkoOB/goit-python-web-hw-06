# Знайти студента із найвищим середнім балом з певного предмета.
from constants import *
from random import randint
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

subject_id = randint(1, NUMBER_SUBJECTS)
sql = f"""
SELECT sub.subject_name, s.student_name, AVG(g.grade) as average_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects sub ON g.subject_id = sub.id
WHERE sub.id = {subject_id}
GROUP BY s.id
ORDER BY average_grade DESC
LIMIT 1;
"""

print(execute_query(sql))
