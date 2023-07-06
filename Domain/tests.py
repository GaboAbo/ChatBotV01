from django.test import TestCase

import os

SECRET_KEY  = os.environ.get('SECRET_KEY', False)
OPEN_AI_KEY = os.environ.get('OPENAI_API_KEY', False)

class SettingTestCase(TestCase):
    def test_secret_key(self):
        self.assertTrue(SECRET_KEY)
        pass

    def test_openai_api_key(self):
        self.assertTrue(OPEN_AI_KEY)
        pass