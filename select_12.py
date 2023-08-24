# Оцінки студентів у певній групі з певного предмета на останньому занятті.
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
SELECT g.grade_date, gr.group_name, sub.subject_name, s.student_name, g.grade
FROM grades g
JOIN students s ON g.student_id = s.id
JOIN subjects sub ON g.subject_id = sub.id
JOIN groups gr ON gr.id = s.group_id
WHERE g.student_id IN (
    SELECT s.id 
    FROM students s
    WHERE s.group_id = {group_id}) 
    AND g.subject_id = {subject_id} 
    AND g.grade_date = (
        SELECT MAX(g.grade_date)
        FROM grades g
        WHERE g.student_id IN (
            SELECT s.id 
            FROM students s
            WHERE s.group_id = {group_id})
            AND g.subject_id = {subject_id}
            );
"""

print(execute_query(sql))
