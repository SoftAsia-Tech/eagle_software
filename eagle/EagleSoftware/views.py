from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm
from .forms import SignUpForm
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
            if user is not None:
                login(request, user)
                # Redirect to a success page.
                return redirect('index')  # Replace 'index' with the name of your index view
            else:
                # Return an 'invalid login' error message.
                return render(request, 'login.html', {'form': form, 'error_message': 'Invalid login'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

# def user_signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#                 # Redirect to a success page or login page
#                 return redirect('login')  # Replace 'login' with the name of your login URL pattern
#             except Exception as e:
#                 error_message = "An error occurred while processing your request. Please try again later."
#         else:
#             # print(form.errors)
#             error_message = "Form submission is invalid. Please correct the errors below."
#             # error_message = print(form.errors)
#     else:
#         form = SignUpForm()
#         error_message = None
    
#     return render(request, 'signup.html', {'form': form, 'error_message': error_message})

def user_signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Print form errors to console for debugging
            print(form.errors)
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
