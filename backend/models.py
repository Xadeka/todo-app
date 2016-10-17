
class Task:
    def __init__(self, id, name, isCompleted=False):
        self.id = id
        self.type = 'tasks'
        self.name = name
        self.isCompleted = isCompleted

    def to_dict(self):
        result = {}
        result['id'] = self.id
        result['type'] = self.type
        result['attributes'] = {}
        result['attributes']['name'] = self.name
        result['attributes']['is-completed'] = self.isCompleted
        return result


