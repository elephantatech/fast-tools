import unittest
from fastapi.testclient import TestClient
from app.main import app
from unittest import TestCase
from app.version import __version__

client = TestClient(app)


class test_health(unittest.TestCase):
    def test_read_health(self):
        resp = client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(
            resp.json(),
            {
                "status": "ok",
                "version": __version__,
            },
        )