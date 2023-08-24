# Знайти оцінки студентів в окремій групі з певного предмета.
from constants import *
from random import randint
import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

group_id = randint(1, NUMBER_GROUPS)
subject_id = randint(1, NUMBER_SUBJECTS)
sql = f"""
SELECT g.group_name, sub.subject_name, s.student_name, gr.grade
FROM students s
JOIN groups g ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
JOIN subjects sub ON sub.id = gr.subject_id
WHERE s.id IN (SELECT s.id FROM students s
                WHERE g.id = {group_id})
                AND gr.subject_id = {subject_id}
ORDER BY s.student_name;
"""

print(execute_query(sql))
