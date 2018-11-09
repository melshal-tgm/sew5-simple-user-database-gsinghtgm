from server.serverwithoutsqlite import app
import unittest


class FlaskTestCase(unittest.TestCase):
    def test_index(self):
        tester=app.test_client(self)
        response=tester.get('/users',content_type='html/text')
        self.assertEqual(response.status_code,200)

