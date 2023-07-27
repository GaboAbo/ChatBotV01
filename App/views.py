from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from .forms  import Form, RegisterForm, LogInForm
from .models import HistoryModel

import openai
import os
from datetime import datetime


# Api key stored outside the function so it won't be requested in every call
openai.api_key = os.environ.get("OPENAI_API_KEY")

#@login_required
def MainView(request):
    user_request = Form(request.POST or None)
    history      = request.GET.get('history')
    print('after redirect', history)

    context = {
        'form': Form(),
        'history': history
    }

    # If is a POST request and is valid(content is Not empty)
    if user_request.is_valid():
        user_message = user_request.clean_content()
        user_time    = datetime.now()
        user_id      = request.user

        # Sending the request to the OpenAI API and storing the result into a variable
        api_response = openai.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": user_message}],
            temperature = 0.7
        )

        # The current time is save to be used as the ai message time or failure time
        api_time = datetime.now()

        # If the api_response is not empty, it means the request returned a valid dictionary
        if api_response:
            context['u_message']  = user_message
            context['u_time']     = user_time
            context['ai_message'] = api_response['choices'][0]['message']['content']
            context['ai_time']    = api_time

            HistoryModel.objects.create(
                message = user_message, 
                msgtime = user_time,
                user    = user_id
            )
            HistoryModel.objects.create(
                message = api_response['choices'][0]['message']['content'], 
                msgtime = api_time,
                user    = user_id
            )
        else:
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

        user_id = User.objects.get(username=request.user.username).id
        history = HistoryModel.objects.get(pk=user_id)
        print('before redirect', history)

        return redirect('/', history=history)
    
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