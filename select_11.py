# Середній бал, який певний викладач ставить певному студентові.
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
SELECT s.student_name, t.teacher_name, AVG(g.grade)
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN teachers t ON g.teacher_id = t.id
WHERE g.student_id = {student_id} AND g.teacher_id = {teacher_id}
GROUP BY s.student_name;
"""

print(execute_query(sql))
