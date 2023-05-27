import sqlite3
from pathlib import Path
from config import bot


DB_NAME = 'db.sqlite3'  # 'products.db'
DB_PATH = Path(__file__).parent.parent
db = sqlite3.connect(DB_PATH / DB_NAME)
cursor = db.cursor()
def init_db():
    global db, cursor


def create_tables():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS Students(
           mentor_id INTEGER PRIMARY KEY,
           name TEXT NOT NULL,
           age INTEGER ,
           who TEXT NOT NULL,
           course TEXT NOT NULL,
           user_id INTEGER
       )""")
    db.commit()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS fsm_anketa(
               student_id INTEGER PRIMARY KEY AUTOINCREMENT,
               name TEXT NOT NULL,
               age INTEGER,
               who TEXT NOT NULL,
               course TEXT NOT NULL,
               mentor_id INTEGER,
               FOREIGN KEY (mentor_id) REFERENCES Students (mentor_id)
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
    cursor.execute('''SELECT mentor_id, name, age, who, course, user_id FROM Students''')
    return cursor.fetchall()

def insert_table(data):
    data = data.as_dict()
    cursor.execute("""
        INSERT INTO fsm_anketa(name, age, who, course, mentor_id) 
        VALUES (:name, :age, :who, :course, :mentor_id)""",
                   {'name':data['name'],
                   'age':data['age'],
                   'who':data['who'],
                   'course':data['course'],
                   'mentor_id':data['mentor_id']})
    db.commit()

if __name__ == '__main__':
    create_tables()
    insert_survey()
