from django.test import SimpleTestCase

class TestHomeView(SimpleTestCase):

    def test_home_http_success(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
