from server.serverwithoutsqlite import app
import unittest


class FlaskTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        # creates a test client
        self.app = app.test_client()
        # propagate the exceptions to the test client
        self.app.testing = True

    def test_index(self):
        result = self.app.get('/users')
        self.assertEqual(result.status_code,200)
    def test_user_data(self):
        result = self.app.get('/users/user5')
        self.assertEqual(result.data, '{"username": "gsingh5", "email": "gsinghmail", "picture": "gsinghpic"}\n')
