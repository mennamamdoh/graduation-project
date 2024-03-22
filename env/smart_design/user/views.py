from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomSignupForm
# from django.contrib.auth.models import User
def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home.html') 
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def user_signup(request):
    if request.method == 'POST':
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            print("tareq"*200)  # Ensure proper indentation here
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}')
            return redirect('login')
        else :
            print ("not valid data")
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
