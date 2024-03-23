from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .forms import LoginForm
from .forms import SignupForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the index.")


def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print("User:", user)  # Debugging statement
            if user is not None:
                login(request, user)
                print("User logged in successfully")  # Debugging statement
                return redirect('index')  # Replace 'index' with the name of your index view
            else:
                print(form.errors)  # Debugging statement
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login'})
        else:
            print(form.errors)  # Debugging statement
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # print("hello there")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            # password1 = form.cleaned_data['password1']
            user = User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
        else:
            print(form.errors)
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


