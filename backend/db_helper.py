import sqlite3

db_name = 'todo.db'

def create_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("CREATE TABLE tasks (id integer primary key, name text, isCompleted boolean)")
    conn.commit()
    conn.close()
    

def create_task(name, isCompleted=False):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO tasks(name, isCompleted) VALUES (?,?)", (name, isCompleted,))
    conn.commit()
    conn.close()
