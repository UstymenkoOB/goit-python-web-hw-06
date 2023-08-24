# Знайти список студентів у певній групі.
from constants import *
from random import randint
import sqlite3

def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()

group_id = randint(1, NUMBER_GROUPS)
sql = f"""
SELECT g.group_name, s.student_name
FROM students s
JOIN groups g ON g.id = s.group_id
WHERE g.id = {group_id}
ORDER BY s.student_name;
"""

print(execute_query(sql))
