My first (actually is the fourth but it's the best I've done so far) Django ChatBot connected to the OpenAI API.

*Requirements*:

1. At least python 3.10
2. pip
3. venv


*Installation and deployment at localhost*:

If venv and .env are already set, skip to step 3

1. Create a virtual environment

`python -m venv venv`

2. Create a .env file with the following structure:
```
SECRET_KEY = you-secret-key
DEBUG = 1
ALLOWED_HOSTS = 127.0.0.1
OPENAI_API_KEY = your-openai-api-key
```

3. Install the dependencies included in the requirements.txt file

`pip install -r requirements.txt`

4. Run the server

`python manage.py runserver`


*Tests*:

There are test made for the Domain and App modules

1. Domain

`python manage.py test Domain.tests`

2. App

`python manage.py test App.tests`

3. Individual tests

`python manage.py test module.tests.test_name`

    Test List:
    Domain.tests.SettingTestCase - Check if the Secret key and Api key are set (can be change at Domain/tests.py)
    App.tests.ViewTestCase - Check if the MainView func handle the post, api and http request using a simulated POST request and a preset input and output (can be change at App/tests.py)

4. All tests

`python manage.py test`