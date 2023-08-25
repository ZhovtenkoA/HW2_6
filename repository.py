from faker import Faker
import random
import sqlite3

fake = Faker()
teachers = []
groups = []
subjects = []

def create_db():
    with open('tables.sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.executescript(sql)

# Заповнення таблиці груп
def add_groups():
    global groups
    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        groups = ['Group A', 'Group B', 'Group C']
        for group in groups:
            cur.execute("INSERT INTO groups (name) VALUES (?)", (group,))
            con.commit()

# Заповнення таблиці викладачів
def add_teachers():
    global teachers
    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        teachers = [fake.name() for _ in range(5)]
        for teacher in teachers:
            cur.execute("INSERT INTO teachers (name) VALUES (?)", (teacher,))
        con.commit()

# Заповнення таблиці предметів
def add_subjects():
    global subjects
    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        subjects = ['Math', 'Physics', 'Chemistry', 'English', 'History']
        for subject in subjects:
            teacher_id = random.randint(1, len(teachers))
            cur.execute(
                "INSERT INTO subjects (name, teacher_id) VALUES (?, ?)", (subject, teacher_id))
        con.commit()

# Заповнення таблиці студентів і оцінок
def add_students_and_grades():
    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        for _ in range(50):
            name = fake.name()
            group_id = random.randint(1, len(groups))
            cur.execute(
                "INSERT INTO students (name, group_id) VALUES (?, ?)", (name, group_id))
            student_id = cur.lastrowid
            for subject_id in range(1, len(subjects)+1):
                for _ in range(5):
                    grade = random.randint(1, 12)
                    date = fake.date_between(start_date='-1y', end_date='today')
                    cur.execute("INSERT INTO grades (student_id, subject_id, grade, date) VALUES (?, ?, ?, ?)",
                                (student_id, subject_id, grade, date))
        con.commit()


def check_db():
    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from students;")
        result = cur.fetchall()
    print('Таблица студентов:')
    print(result)
    print('------------------------------------')

    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from groups;")
        result = cur.fetchall()
    print('Таблица групп:')
    print(result)
    print('------------------------------------')

    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from teachers;")
        result = cur.fetchall()
    print('Таблица учителей:')
    print(result)
    print('------------------------------------')

    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from subjects;")
        result = cur.fetchall()
    print('Таблица предметов:')
    print(result)
    print('------------------------------------')

    with sqlite3.connect('study.db') as con:
        cur = con.cursor()
        cur.execute("SELECT * from grades;")
        result = cur.fetchall()
    print('Таблица оценок:')
    print(result)
    print('------------------------------------')

    

def init_db():
    create_db()
    add_groups()
    add_teachers()
    add_subjects()
    add_students_and_grades()
