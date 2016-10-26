from app import db
from app.models import Task


def get_all_tasks():
    query = None
    try:
        query = Task.query
        db.session.expunge_all()
    except:
        db.session.rollback()
        query = None
    finally:
        db.session.close()

    return query


def get_task(uuid):
    query = None
    try:
        query = Task.query.filter_by(uuid=uuid).first()
        db.session.expunge(query)
    except:
        db.session.rollback()
        query = None
    finally:
        db.session.close()

    return query


def create_task(uuid, name, isComplete=False):
    task = Task(uuid, name, isComplete=isComplete)
    try:
        db.session.add(task)
        db.session.commit()
        db.session.expunge(task)
    except:
        db.session.rollback()
        task = None
    finally:
        db.session.close()

    return task


def update_task(task):
    query = None
    try:
        query = Task.query.filter_by(uuid=task.uuid).first()
        query.name = task.name
        query.isComplete = task.isComplete
        db.session.commit()
        db.session.expunge(query)
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return query


def delete_task(uuid):
    task = None
    try:
        task = Task.query.filter_by(uuid=uuid).first()
        db.session.delete(task)
        db.session.commit()
        db.session.expunge(task)
    except:
        db.session.rollback()
        task = None
    finally:
        db.session.close()

    return task
