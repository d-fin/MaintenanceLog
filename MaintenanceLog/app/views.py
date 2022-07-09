import email
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.db import connection
from django.contrib.auth.admin import * 
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout 
from .forms import CreateUserForm, DropdownMenuForm
import pdb
# Create your views here.

#home page 
def home(request):
    siteCode = 1
    maintenanceData = {}
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM app_maintenance WHERE siteCode = " + str(siteCode))
        for i in cursor: 
            x = 0
            temp = []
            for j in i:
                if x == 0: pass 
                else: temp.append(j)
                x += 1
            maintenanceData[temp[0]] = temp

    context = {

    }
    return render(request, 'index.html')

def addBrush(request):
    form = DropdownMenuForm()
    if request.method == 'POST':        
        form = DropdownMenuForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('brushType')
            """ with connection.cursor() as cursor:
                cursor.execute() """
            return redirect('home')

    context = {
        'form' : form
    } 
    
    return render(request, 'add_brush.html', context)

#User register page
def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')

    context = {
        'form' : form
    }

    return render(request, 'register.html', context)

#User login page 
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Error logging in")
  
    return render(request, 'login.html')

# user logout page
def logoutUser(request):
    logout(request)
    return redirect('home')

def userAccount(request):
    return render(request, 'profile.html')