from email.message import Message
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.admin import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import CreateUserForm, DropdownMenuForm, updateCompValueForm
from django.contrib.auth.decorators import login_required
import pdb
from datetime import date
from dateutil import parser
import numpy as np 

from app.functions import *
# Create your views here.

#home page 
@login_required
def home(request):

    siteCode = 1
    maintenanceData = getMaintenanceData(siteCode)
    brushData = getBrushData(siteCode)

    curtains = [brushData['Curtains']]
    wraps = [brushData['Wrap Brushes']]
    sideWashers = [brushData['Side Washers']]
    rockers = [brushData['Rocker Brushes']]

    
    df = returnDataFrames()
    df1 = df.values.tolist()
    today = datetime.date.today().strftime("%m/%d/%Y")
    total, pastDay = 0, 0
    for i in df1:
        for j in i:
            if isinstance(j, datetime.date) == True:
                j = j.strftime("%m/%d/%Y")
                if j < today: 
                    pastDay += 1
                    total += 1
                else: total += 1

    allGood = total - pastDay
    pastDuePercent = round(((pastDay / total) * 100), 2)
    upToDatePercent = round((100 - pastDuePercent), 2)
    

    context = {
        'df' : maintenanceData,
        'curtains' : curtains,
        'wraps' : wraps,
        'sideWashers' : sideWashers,
        'rockers' : rockers,
        'total' : allGood,
        'pastDue' : pastDay,
        'pastDuePercent' : pastDuePercent,
        'upToDatePercent' : upToDatePercent,
    }

    return render(request, 'index.html', context)

@login_required
def updateSchedule(request):
    choices =  [(0, 'Select'), (1, 'Curtain'), (2, 'Rocker Brush'),
         (3, 'Wrap Brush'), (4, 'Side Brush'),
         (5, 'Takeup Drum'), (6, 'Sprocket'),
         (7, 'Fork Cover'), (8, 'Fork Cylinder'),
         (9, 'Heco Drive'), (10, 'Conveyor Hydraulic Motor'),
         (11, 'Chain/Rollers'), (12, "All Brushes"), (13, "All Components")]

    brushesStrings =  ['Curtain', 'Rocker Brush', 'Wrap Brush', 'Side Washer']
    otherCompStrings = ['Takeup Drum', 'Sprocket', 'Fork Cover', 'Fork Cylinder',
        'Heco Drive', 'Conveyor Hydraulic Motor', 'Chain/Rollers']
    
    brushes, headersBrushes, component, component2, headersComp, compData = None, None, None, None, None, None
    formSelect = updateCompValueForm()

    if request.method == 'POST':
        comp = None
        formSelect = updateCompValueForm(request.POST)
        if formSelect.is_valid():
            data = formSelect.cleaned_data.get('component')
            if int(data) == 0:
                return redirect('update_schedule')
            elif int(data) == 12:
                z = []
                brushes = []
                for i in brushesStrings:
                    headersBrushes, temp = getSpecificCompData(i)
                    z.append(temp)
                for j in z:
                    for x in j:
                        brushes.append(x)
            elif int(data) == 13:
                z = []
                brushes = []
                for i in brushesStrings:
                    headersBrushes, temp = getSpecificCompData(i)
                    z.append(temp)
                for j in z:
                    for x in j:
                        brushes.append(x)
                a = []
                compData = []       
                for i in otherCompStrings:
                    headersComp, temp = getSpecificCompData(i)
                    a.append(temp)
                for j in a:
                    for x in j:
                        compData.append(x)
            else:
                for i in choices: 
                    if int(data) == int(i[0]):
                        comp = i[1]
                component = comp

                if comp in brushesStrings:
                    headersBrushes, brushes = getSpecificCompData(comp)
                elif comp in otherCompStrings:
                    headersComp, compData = getSpecificCompData(comp)
            if int(data) == 13:
                component = "All Brushes"
                component2 = "All Components"        
    context = {
        'formSelect' : formSelect,
        'component' : component,
        'component2' : component2,
        'headers' : headersBrushes,
        'brushes' : brushes,
        'headersComp' : headersComp,
        'compData' : compData,
    }
    return render(request, 'update_schedule.html', context)

def addBrush(request):
    form = DropdownMenuForm()
    if request.method == 'POST':        
        form = DropdownMenuForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data.get('brushType')
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

#---------------------------------------
# Below are my ajax/jsom parsers that recieve data from my table in "Update Schedule"
def getUpdate_SchedulePage():
    return 

def saveSchedule(request):
    id = request.POST.get('id', '')
    value = request.POST.get('value', '')
    type = request.POST.get("type", '')
    
    dateString, day, month, year = None, None, None, None
    if type == "name" or type == "notes2":
        pass 
    else:
        try: 
            data = value.split("/")
            month = data[0]
            day = data[1] 
            year = data[2] 
        except Exception as e: 
            print(e)
            dateString = value
        else: dateString = year + "/" + month + "/" + day
        finally: 
            value = parser.parse(dateString)

    
    if type == "name" or type == "dateReplaced" or type == "dueDate" or type == "notes2":
        compData = Maintenance.objects.get(id=id)
        if type == "name":
            compData.component = value 
        if type == "dateReplaced":
            compData.dateReplaced = value 
        if type == "dueDate":
            compData.dueDate = value 
        if type == "notes2":
            compData.notes = value 
        compData.save()

    else:
        brushComp = BrushComponent.objects.get(brushID=id)
        brushData = Brush.objects.get(id=id)
        if type == "side":
            brushData.side = value
        if type == "setNum":
            brushData.setNum = value
        if type == "motor":
            brushComp.motor = value
        if type == "shaft":
            brushComp.shaft = value
        if type == "bearings":
            brushComp.bearings = value
        if type == "upperBearings":
            brushComp.upperBearings = value
        if type == "cloth":
            brushComp.cloth = value
        if type == "shocks":
            brushComp.shocks = value 

        if type == "side" or type == "setNum":
            brushData.save()
        else:
            brushComp.save()

    return JsonResponse({"success" : "Updated"})