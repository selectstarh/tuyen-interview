from unittest import TestCase
from app import create_app

class TestIndex(TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_index(self):
        rv = self.app.get('/api/index/nnnnnnnnnnn')
        self.assertEqual({"count": 0, "lines": []}, rv.get_json())
