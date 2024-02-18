from flask import Flask, current_app
from flask_restful import Resource, Api
import random

DECISION_LIST = [
    'A random decision',
    'Another random item',
    'This is just an example'
]

class Decisions(Resource):
    def get(self):
        seed = current_app.config['RANDOM_SEED']
        self.rng = random.Random(seed)
        return self.rng.choice(DECISION_LIST)

class Health(Resource):
    def get(self):
        return ""

def create_app(test_config=None):
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Decisions, '/decisions')
    api.add_resource(Health, '/healthz')

    # Default configuration
    app.config.from_mapping(
        SECRET_KEY='dev',
        RANDOM_SEED=None
    )
    app.config.from_prefixed_env() # Load config from FLASK_* env variables
    if test_config is not None:
        app.config.from_mapping(test_config) # Override with test_config, if present
    return app

if __name__ == '__main__':
    create_app().run(debug=True)

