from datetime import datetime
import faker
from random import randint, choice
import sqlite3
from constants import *


def generate_fake_data(number_groups, number_subjects, number_teachers, number_students) -> tuple():
    fake_groups = []  
    fake_subjects = []  
    fake_teachers = []  
    fake_students = []

    fake_data = faker.Faker()

    for _ in range(number_groups):
        fake_groups.append(fake_data.bs().title()+' Group')

    for _ in range(number_subjects):
        fake_subjects.append(fake_data.catch_phrase())

    for _ in range(number_teachers):
        fake_teachers.append(fake_data.name())

    for _ in range(number_students):
        fake_students.append(fake_data.name())

    return fake_groups, fake_subjects, fake_teachers, fake_students


def prepare_data(groups, subjects, teachers, students) -> tuple():
    for_groups = []
    
    for group in groups:
        for_groups.append((group, ))

    for_teachers = []
    
    for teacher in teachers:
        for_teachers.append((teacher, ))

    for_subjects = []
    
    for subject in subjects:
        for_subjects.append(
            (subject, randint(1, NUMBER_TEACHERS)))
        
    for_students = []
    
    for student in students:
        for_students.append(
            (student, randint(1, NUMBER_GROUPS)))

    for_grades = []

    for student_id in range(1, NUMBER_STUDENTS + 1):
        for _ in range(NUMBER_GRADES):
            date_today = datetime.now()
            year = date_today.year
            month = randint(1, date_today.month)
            if month == date_today.month:
                day_max = date_today.day
            elif month in [1, 3, 5, 7, 8, 10, 12]:
                day_max = 31
            elif month == 2:
                day_max = 28
            else:
                day_max = 30
            grade_date = datetime(year, month, randint(1, day_max)).date()
            subject_teacher = []
            while not subject_teacher:
                teacher_id = randint(1, NUMBER_TEACHERS)
                for i in range(NUMBER_SUBJECTS):
                    if for_subjects[i][1] == teacher_id:
                        subject_teacher.append(i+1)
            subject_id = choice(subject_teacher)
            for_grades.append((grade_date, student_id, teacher_id, subject_id, randint(1, 100)))

    return for_groups, for_subjects, for_teachers, for_students, for_grades


def insert_data_to_db(groups, teachers, subjects, students, grades) -> None:
    with sqlite3.connect('university.db') as con:

        cur = con.cursor()

        sql_to_groups = """INSERT INTO groups(group_name)
                               VALUES (?)"""

        cur.executemany(sql_to_groups, groups)

        sql_to_teachers = """INSERT INTO teachers(teacher_name)
                               VALUES (?)"""

        cur.executemany(sql_to_teachers, teachers)

        sql_to_subjects = """INSERT INTO subjects(subject_name, teacher_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_subjects, subjects)

        sql_to_students = """INSERT INTO students(student_name, group_id)
                               VALUES (?, ?)"""

        cur.executemany(sql_to_students, students)

        sql_to_grades = """INSERT INTO grades(grade_date, student_id, teacher_id, subject_id, grade)
                              VALUES (?, ?, ?, ?, ?)"""

        cur.executemany(sql_to_grades, grades)

        con.commit()


if __name__ == "__main__":
    groups, subjects, teachers, students, grades = prepare_data(
        *generate_fake_data(NUMBER_GROUPS, NUMBER_SUBJECTS, NUMBER_TEACHERS, NUMBER_STUDENTS))
    insert_data_to_db(groups, teachers, subjects, students, grades)
