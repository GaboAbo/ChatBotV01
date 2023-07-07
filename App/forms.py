from django import forms
from django.contrib.auth.forms import UserCreationForm


# Creating a Form to handle the user input and cleaning the values
class Form(forms.Form):
    # content is the name of the field which will be specified at the form
    content = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'user-form', 'placeholder': 'Type your message'}
        )
    )

    # Cleaning the content inside the POST request
    def clean_content(self):
        # Getting the content value and storing it
        cleaned_content = self.cleaned_data.get('content')
        
        return cleaned_content
    

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(
            attrs={'class': 'auth-input', 'placeholder': 'Username'}
        )
    )
    email = forms.CharField(
        max_length=255,
        label='',
        widget=forms.TextInput(
            attrs={'class': 'auth-input', 'placeholder': 'Email'}
        )
    )
    password1 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'auth-input', 'placeholder': 'New Password'}
        )
    )
    password2 = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'auth-input', 'placeholder': 'Confirm Password'}
        )
    )


class LogInForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        label='',
        widget=forms.TextInput(
            attrs={'class': 'auth-input', 'placeholder': 'Username'}
        )
    )
    password = forms.CharField(
        label='',
        widget=forms.PasswordInput(
            attrs={'class': 'auth-input', 'placeholder': 'Password'}
        )
    )