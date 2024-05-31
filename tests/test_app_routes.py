from run import create_app
import unittest

class TestAppRoutes(unittest.TestCase):
    def setUp(self):
        # Create a test client
        self.app = create_app()
        self.client = self.app.test_client()

    def test_index_route_get(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Cairo', response.data)

    def test_index_route_post_city(self):
        response = self.client.post('/', data={'city': 'New York'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New York', response.data)

    def test_index_route_post_coordinates(self):
        response = self.client.post('/', data={'latitude': '40.7128', 'longitude': '-74.0060'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'New York', response.data)
    def test_about_route(self):
        # Test the about route
        response = self.client.get('/about')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About WeatherWise', response.data)
     
        
    def test_blog_route(self):
        # Test the blog route
        response = self.client.get('/blog')
        self.assertEqual(response.status_code, 200)


if __name__ == '__main__':
    unittest.main()

