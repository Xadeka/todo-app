from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
import sqlite3
import db_helper as dbh
from models import Task

app = Flask(__name__)
CORS(app)

db_name = 'todo.db'

version = '1'
base_url = '/api/v' + version


@app.route(base_url + '/tasks', methods=['GET'])
def get_all_tasks():
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    result = {'data' : []}
    for row in c.execute("SELECT * FROM tasks"):
        print(row)
        result['data'].append(Task(row[0], row[1], isCompleted=row[2]).to_dict())

    conn.close()
    return jsonify(**result)


@app.route(base_url + '/tasks', methods=['POST'])
def add_task():
    data = request.json['data']['attributes']

    dbh.create_task(data['name'])

    result = {'data' : []}
    return jsonify(**result)


if __name__ == '__main__':
    app.run(debug=True)
