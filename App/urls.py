from django.urls import path

from .views import (
    MainView,
    LoginView,
    RegisterView,
    LogOutView,
)


urlpatterns = [
    path('',          MainView,     name='MainView'),
    path('login/',    LoginView,    name='LoginView'),
    path('register/', RegisterView, name='RegisterView'),
    path('logout/',   LogOutView,   name='LogOutView'),
]
