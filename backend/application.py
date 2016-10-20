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
    for task in dbh.get_all_tasks():
        result['data'].append(task.to_dict())

    return jsonify(**result)


@application.route(base_url + '/tasks/<uuid>', methods=['GET'])
def get_task(uuid):
    task = dbh.get_task(uuid)
    if task == None:
        return jsonify({'data' : {}})
    return jsonify(**{ 'data' : task.to_dict() })


@application.route(base_url + '/tasks', methods=['POST'])
def add_task():
    uuid = request.json['data']['id']
    attr = request.json['data']['attributes']

    dbh.create_task(uuid, attr['name'])

    result = {'data' : Task(uuid, attr['name']).to_dict()}
    return jsonify(**result)


@application.route(base_url + '/tasks/<uuid>', methods=['PATCH'])
def update_task(uuid):
    attr = request.json['data']['attributes']
    task = Task(uuid, attr['name'], isComplete=attr['is-complete'])
    dbh.update_task(uuid)
    return jsonify(**{'data' : task.to_dict()})


@application.route(base_url + '/tasks/<uuid>', methods=['DELETE'])
def delete_task(uuid):
    task = dbh.get_task(uuid)
    if task == None:
        return jsonify({})

    dbh.delete_task(uuid)
    return jsonify(**{'data' : task.to_dict()})

if __name__ == '__main__':
    application.run(host='0.0.0.0')
