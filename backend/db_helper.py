import sqlite3

db_name = 'todo.db'

def create_db():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("CREATE TABLE tasks (uuid text primary key, name text, isComplete boolean)")
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    result = c.fetchall()
    conn.close()
    return result


def get_task(uuid):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("SELECT * from tasks WHERE uuid=(?)", (uuid,))
    result = c.fetchone()
    conn.close()
    return result


def create_task(uuid, name, isComplete=False):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("INSERT INTO tasks(uuid, name, isComplete) VALUES (?,?,?)", (uuid, name, isComplete,))
    conn.commit()
    conn.close()


def update_task(uuid, task):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("UPDATE tasks SET name=?, isComplete=? WHERE uuid=?", (task.name, task.isComplete, uuid,))
    conn.commit()
    conn.close()


def delete_task(uuid):
    conn = sqlite3.connect(db_name)
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE uuid=?", (uuid,))
    conn.commit()
    conn.close()
