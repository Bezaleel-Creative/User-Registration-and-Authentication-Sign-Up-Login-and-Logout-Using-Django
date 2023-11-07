from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.error(request, 'Email already taken')
                return redirect('userapp:register')
            elif User.objects.filter(username=username).exists():
                messages.error(request, 'Username already taken')
                return redirect('userapp:register')
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('userapp:login')
        else:
            messages.error(request, 'Password does not match')
            return redirect('userapp:register')
    return render(request, 'userapp/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('dashboard:dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('userapp:login')

    return render(request, 'userapp/login.html')


def logout(request):
    auth.logout(request)
    return redirect('userapp:login')