from app import db
from app.models import Task


def get_all_tasks():
    return Task.query


def get_task(uuid):
    query = Task.query.filter_by(uuid=uuid).first()
    return query


def create_task(uuid, name, isComplete=False):
    task = Task(uuid, name, isComplete=isComplete)
    db.session.add(task)
    db.session.commit()


def update_task(task):
    uTask = Task.query.filter_by(uuid=task.uuid).first()
    uTask.name = task.name
    uTask.isComplete = task.isComplete
    db.session.commit()


def delete_task(uuid):
    task = Task.query.filter_by(uuid=task.uuid).first()
    db.session.delete(query)
    db.session.commit()
