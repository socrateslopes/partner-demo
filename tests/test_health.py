from application import app
import json
import unittest

class HealthTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_health_endpoint(self):
        result = self.app.get("/health")
        self.assertEqual(result.status_code,200)
        data = json.loads(result.data)
        self.assertEqual(data["ok"],True)