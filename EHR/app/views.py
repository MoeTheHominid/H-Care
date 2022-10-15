from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
import json

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def register(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        if password == password_confirm :
            if User.objects.filter(username=username).exists() :
                messages.info(request, 'Email Already Used')
                return redirect('register')
            
            else :
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
        
        else :
            messages.info(request, "Password Not The Same")
            return redirect('register')
    
    else :
        return render(request, 'register.html')

def login(request) :
    if request.method == 'POST' :
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None :
            auth.login(request, user)
            return redirect('dashboard')
        
        else :
            messages.info(request, 'Credentials Invalid')   
            return redirect('login')
        
    else :
        return render(request, 'login.html')

def logout(request) :
    auth.logout(request)
    return redirect('/')

def dashboard(request) :
    return render(request, 'dashboard.html')