from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
    # password1 = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("This username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered.")
        return email
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Email Address Or Username', widget=forms.TextInput(attrs={'placeholder': 'Enter your Email or Username'}), max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),)
    # remember_me = forms.BooleanField(label='Remember me', required=False)

