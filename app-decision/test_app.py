from app import create_app, DECISION_LIST
from unittest import TestCase

class TestIntegration(TestCase):
    def setUp(self):
        self.app = create_app({'RANDOM_SEED': 42}).test_client()

    def test_healthy(self):
        response = self.app.get('/decisions')
        assert response.status_code == 200

    def test_response(self):
        response = self.app.get('/decisions')
        assert response.json in DECISION_LIST
