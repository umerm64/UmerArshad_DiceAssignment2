import unittest
from app import app

class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.ctx = app.app_context()
        self.ctx.push()
        self.client = app.test_client()

    def tearDown(self):
        self.ctx.pop()

    def test_home(self):
        response = self.client.get("/")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "This is the root page."

    def test_about(self):
        response = self.client.get("/about")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "This is a test application for Dice Analytics Devops training."

    def test_test(self):
        response = self.client.get("/test")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "This is the test page."

    def test_post(self):
        response = self.client.post("/post")
        assert response.status_code == 200
        assert response.get_data(as_text=True) == "This is a test of POST method."

if __name__ == "__main__":
    unittest.main()