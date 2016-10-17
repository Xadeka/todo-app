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
        result['data'].append(Task(row[0], row[1], isComplete=row[2]).to_dict())

    conn.close()
    return jsonify(**result)


@app.route(base_url + '/tasks/<uuid>', methods=['GET'])
def get_task(uuid):
    row = dbh.get_task(uuid)
    if row == None:
        return jsonify({'data' : {}})
    task = Task(row[0], row[1], isComplete=row[2])
    return jsonify(**{ 'data' : task.to_dict() })


@app.route(base_url + '/tasks', methods=['POST'])
def add_task():
    uuid = request.json['data']['id']
    attr = request.json['data']['attributes']

    dbh.create_task(uuid, attr['name'])

    result = {'data' : Task(uuid, attr['name']).to_dict()}
    return jsonify(**result)


@app.route(base_url + '/tasks/<uuid>', methods=['PATCH'])
def update_task(uuid):
    attr = request.json['data']['attributes']
    task = Task(uuid, attr['name'], isComplete=attr['is-complete'])
    dbh.update_task(uuid, task)
    return jsonify(**{'data' : task.to_dict()})


@app.route(base_url + '/tasks/<uuid>', methods=['DELETE'])
def delete_task(uuid):
    row = dbh.get_task(uuid)
    print(row)
    if row == None:
        return jsonify({})
    task = Task(row[0], row[1], isComplete=row[2])

    dbh.delete_task(uuid)
    return jsonify(**{'data' : task.to_dict()})

if __name__ == '__main__':
    app.run(debug=True)
