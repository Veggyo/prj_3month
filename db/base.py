import sqlite3
from pathlib import Path
from config import bot
# from aiogram import types


DB_NAME = 'db.sqlite3'  # 'products.db'
DB_PATH = Path(__file__).parent.parent
db = sqlite3.connect(DB_PATH / DB_NAME)
cursor = db.cursor()
def init_db():
    global db, cursor


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
           id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           age INTEGER ,
           who TEXT NOT NULL,
           course TEXT NOT NULL,
           user_id INTEGER
       )""")
    db.commit()


def insert_survey():
    cursor.execute("""INSERT INTO Students(name, age, who, course, user_id)
    VALUES("Adelina", 16, 'студент','backend', 234567),
    ("Gulina", 16, 'ментор', 'backend', 425673),
    ("Aldiyar", 19, 'ментор', 'backend', 426632),
    ("Mirlan", 16, 'ментор', 'backend', 425732),
    ("Abdumalik", 16, 'ментор', 'backend', 428632)
    """)
    db.commit()


def get_students():
    cursor.execute('''SELECT * FROM Students''')
    return cursor.fetchall()

def get_mentor(mentor_id: int):
    cursor.execute("SELECT * FROM Students WHERE Students.id = :mentor_id", {'mentor_id': mentor_id})
    return cursor.fetchone()

if __name__ == '__main__':
    create_tables()
    insert_survey()
    get_students()
