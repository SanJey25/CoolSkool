import sqlite3
from random import randint

db_name = 'quiz.sqlite'
conn = None
cursor = None

def open():
    global conn, cursor
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

def close():
    cursor.close()
    conn.close()

def do(query):
    cursor.execute(query)
    conn.commit()

def clear_db():
    ''' deletes all tables '''
    open()
    query = '''DROP TABLE IF EXISTS homework'''
    do(query)

    close()

def create():
    open()
    cursor.execute('''PRAGMA foreign_keys=on''')
    
    do('''CREATE TABLE IF NOT EXISTS homework (
            id INTEGER PRIMARY KEY, 
            subject VARCHAR,
            task VARCHAR)'''
    )
    close()
def fill_table():
    open()
    subjuct_list=[("Math","None"),("Physics","None"),("Geography","None"),("Georgian language","None")]
    query = '''INSERT INTO homework (subject, task) VALUES(?,?)'''
    cursor.executemany(query, subjuct_list)
    conn.commit()
    close()

def show(table):
    query = 'SELECT * FROM ' + table
    open()
    cursor.execute(query)
    print(cursor.fetchall())
    close()
def get_list():
    open()
    query = '''SELECT * FROM homework'''
    cursor.execute(query)
    return cursor.fetchall()
def insert(id,shmask):
    query ='''UPDATE homework SET task = ? WHERE id = ?'''
    open()
    cursor.execute(query,[shmask,id])
    conn.commit()
    close()

def main():
    clear_db()
    create()
    fill_table()
    show("homework")
    
if __name__ == "__main__":
    main()