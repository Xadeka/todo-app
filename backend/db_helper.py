import sqlite3

db_name = 'todo.db'

def create_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("CREATE TABLE tasks (uuid text primary key, name text, isComplete boolean)")
    conn.commit()
    conn.close()
    

def create_task(uuid, name, isComplete=False):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO tasks(uuid, name, isComplete) VALUES (?,?,?)", (uuid, name, isComplete,))
    conn.commit()
    conn.close()
