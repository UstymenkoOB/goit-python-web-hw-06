# Знайти середній бал у групах з певного предмета.
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
SELECT sub.subject_name, gr.group_name, AVG(g.grade) as average_grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON s.group_id = gr.id
WHERE sub.id = {subject_id}
GROUP BY gr.id;
"""

print(execute_query(sql))
