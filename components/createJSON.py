import json


class CreateFile:
    resume = {} #   Local variable to manage the candidates object

    def __init__(self, resume):
        self.resume = resume
        self.create_json()

    def create_json(self):
        result = json.dumps(self.resume)
        with open('candidates.json', 'w') as f:
            f.write(result)

