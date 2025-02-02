import unittest
from app import app

class FlaskAppTestCase(unittest.TestCase):
    def setUp(self):
        """Set up test client."""
        app.testing = True
        self.client = app.test_client()
    
    def test_moscow_time_route(self):
        """Test the root route to check if it returns a valid response."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'The current time in Moscow is:', response.data)

if __name__ == "__main__":
    unittest.main()

