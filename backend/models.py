
class Task:
    def __init__(self, uuid, name, isComplete=False):
        self.uuid = uuid
        self.type = 'tasks'
        self.name = name
        self.isComplete = isComplete

    def to_dict(self):
        result = {}
        result['id'] = self.uuid
        result['type'] = self.type
        result['attributes'] = {}
        result['attributes']['name'] = self.name
        result['attributes']['is-complete'] = self.isComplete
        return result


