from app import db

class Task(db.Model):

    # Define the columns
    uuid = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.Text)
    isComplete = db.Column(db.Boolean)
    type = 'tasks'

    def __init__(self, uuid, name, isComplete=False):
        self.uuid = uuid
        self.name = name
        self.isComplete = isComplete


    def __repr__(self):
        return '<Task %r, %r, %r>' % (self.uuid, self.name, self.isComplete)


    def to_dict(self):
        result = {}
        result['id'] = self.uuid
        result['type'] = self.type
        result['attributes'] = {}
        result['attributes']['name'] = self.name
        result['attributes']['is-complete'] = self.isComplete
        return result
