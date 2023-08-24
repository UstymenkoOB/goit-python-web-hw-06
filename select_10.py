# Список курсів, які певному студенту читає певний викладач.
from constants import *
from random import randint
import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

teacher_id = randint(1, NUMBER_TEACHERS)
student_id = randint(1, NUMBER_STUDENTS)
sql = f"""
SELECT s.student_name, t.teacher_name, sub.subject_name
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN teachers t ON g.teacher_id = t.id
WHERE g.student_id = {student_id} AND g.teacher_id = {teacher_id}
GROUP BY sub.subject_name;
"""

print(execute_query(sql))
