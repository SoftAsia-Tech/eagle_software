from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # email = forms.EmailField(label='Your Email', max_length=254, help_text='Required. Inform a valid email address.')
    username = forms.CharField(max_length=150, widget=forms.PasswordInput(attrs={'placeholder': 'Username'}))
    email = forms.EmailField(max_length=254, widget=forms.PasswordInput(attrs={'placeholder': 'Enter your email'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password', 'class': 'password-icon'}))
    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'password-icon'}))
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
class LoginForm(forms.Form):
    username = forms.CharField(label='Email Address Or Username', widget=forms.TextInput(attrs={'placeholder': 'Enter your Email or Username', 'class': 'email-icon'}), max_length=100)
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password', 'class': 'password-icon'}),)
    remember_me = forms.BooleanField(label='Remember me', required=False)

