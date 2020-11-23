from flaskapp import app
import unittest


class BasicTest(unittest.TestCase):
    """Unit testing class"""
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        pass

    # Actual test 1
    def test_welcome_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    # Actual test 2
    def test_redis_increment(self):
        redis = Redis(host="redis-server", db=0)
        self.app.get('/visit')
        self.app.get('/visit')
        self.assertEqual(int(redis.get("counter")), 2)

if __name__ == "__main__":
    unittest.main()