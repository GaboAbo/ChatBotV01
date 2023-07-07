from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .forms  import Form, RegisterForm, LogInForm

import openai
import os
from datetime import datetime


# Api key stored outside the function so it won't be requested in every call
openai.api_key = os.environ.get("OPENAI_API_KEY")

#@login_required
def MainView(request):
    # If there is no POST request the Form will be empty
    user_request = Form(request.POST or None)
    # Setting an empty form to be sent to home.html using the render method
    context = {
        'form': Form(),
    }

    # If is a POST request and is valid(content is Not empty)
    if user_request.is_valid():
        # The clean method to get the content is called
        user_message = user_request.clean_content()
        # The current time is saved to be used as the user message time
        user_time = datetime.now()

        # Sending the request to the OpenAI API and storing the result into a variable
        api_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": user_message}],
            temperature = 0.7
        )

        # The current time is save to be used as the ai message time or failure time
        context['ai_time'] = datetime.now()

        # If the api_response is not empty, it means the request returned a valid dictionary
        if api_response:
            context['u_message']  = user_message
            context['u_time']     = user_time
            # The content is stored into the ai_message by accesing to the api_response dict
            context['ai_message'] = api_response['choices'][0]['message']['content']
        # If the api_response is empty, some setting, communication to the API failed
        else:
            # Then an error message is stored into the ai_message
            context['ai_message'] = 'Something wrong happened, please try again.'

    """The render method is use to return a http request to home.html and all the values
    stored in the context dictionary"""
    return render(request, 'home.html', context=context)


def LoginView(request):
    Form = LogInForm(request.POST or None)
    if Form.is_valid():
        username = Form.cleaned_data.get("username")
        password = Form.cleaned_data.get("password")

        user = authenticate(
            request,
            username = username,
            password = password
        )
        if user is None:
            context = {'error': "Invalid username or password"}
            return render(request, 'auth/login.html', context=context)
        
        login(request, user)
        return redirect('/')
    
    context = {
        'Form': Form
    }

    return render(request, 'auth/login.html', context=context)


def RegisterView(request):
    Form = RegisterForm(request.POST or None)

    context = {}

    if Form.is_valid():
        Form.save()
        context['created'] = True
        return redirect('/login')

    context['Form'] = Form
    
    return render(request, 'auth/register.html', context=context)


def LogOutView(request):
    if request.method == "POST":
        logout(request)
        return redirect("/login/")
    
    return render(request, 'auth/logout.html', {})