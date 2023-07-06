from django import forms

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