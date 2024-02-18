from flask import Flask
from flask_restful import Resource, Api
import random

app = Flask(__name__)
api = Api(app)

class Decisions(Resource):
    DECISION_LIST = [
        'A random decision',
        'Another random item',
        'This is just an example'
    ]

    def get(self):
        return random.choice(Decisions.DECISION_LIST)

api.add_resource(Decisions, '/decisions')

if __name__ == '__main__':
    app.run(debug=True)

