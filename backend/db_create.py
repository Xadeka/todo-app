from app import db
from app.models import Task

db.create_all()

print('DB created.')
