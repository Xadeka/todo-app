from flask import Flask, request, redirect, jsonify
from flask_cors import CORS
from app.models import Task
import app.db_helper as dbh


application = Flask(__name__)
CORS(application)


version = '1'
base_url = '/api/v' + version


@application.route(base_url + '/tasks', methods=['GET'])
def get_all_tasks():
    result = {'data' : []}
    tasks = dbh.get_all_tasks()
    if tasks == None:
        return jsonify(**result)

    for task in tasks:
        result['data'].append(task.to_dict())

    return jsonify(**result)


@application.route(base_url + '/tasks/<uuid>', methods=['GET'])
def get_task(uuid):
    task = dbh.get_task(uuid)
    if task == None:
        return jsonify(**{'data' : {}})
    return jsonify(**{ 'data' : task.to_dict() })


@application.route(base_url + '/tasks', methods=['POST'])
def add_task():
    uuid = request.json['data']['id']
    attr = request.json['data']['attributes']

    task = dbh.create_task(uuid, attr['name'])

    result = {'data': ''}
    if task == None:
        return jsonify(**result)

    result['data'] = Task(uuid, attr['name']).to_dict()
    return jsonify(**result)


@application.route(base_url + '/tasks/<uuid>', methods=['PATCH'])
def update_task(uuid):
    result = {'data' : ''}

    task = dbh.update_task(uuid)
    if task == None:
        return jsonify(**result)

    result['data'] = task.to_dict()
    return jsonify(**result)


@application.route(base_url + '/tasks/<uuid>', methods=['DELETE'])
def delete_task(uuid):
    result = {'data' : ''}

    task = dbh.get_task(uuid)
    if task == None:
        return jsonify(**result)

    task = dbh.delete_task(uuid)
    if task == None:
        return jsonify(**result)

    result['data'] = task.to_dict()
    return jsonify(**result)


if __name__ == '__main__':
    application.run(host='0.0.0.0')
