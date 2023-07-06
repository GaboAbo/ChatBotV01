from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from bs4 import BeautifulSoup

from .views import MainView

# Test case: Main view reques.POST, API communication and render handling
class ViewTestCase(TestCase):
    # Creating a simulated POST request and declaring the input and desired output
    def setUp(self):
        # Simulated POST request for testing purposes
        self.factory = RequestFactory()
        self.input_value  = "Say the word 'Hi"
        self.output_value = "Hi"

    # Setting up the POST request and calling the MainView function located at views.py
    def test_api_request(self):
        request = self.factory.post('', {'content': self.input_value})
        request.user = AnonymousUser()

        # Calling the MainView and store the http response into a variable
        response = MainView(request)

        # Using the BeautifulSoup dependency to parse the http response
        parsed_response = BeautifulSoup(response.content, 'html.parser')
        # Getting the OpenAI API content using the class specified at home.html (ai)
        ai_response = parsed_response.select_one('.ai')
    
        return ai_response.text

    def test_post_to_render(self):
        self.assertEqual(self.test_api_request(), self.output_value)