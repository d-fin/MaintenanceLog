from email.message import Message
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.db import connection
from django.contrib.auth.admin import * 
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout 
from .forms import CreateUserForm, DropdownMenuForm, updateCompValueForm, editProfileForm
from django.contrib.auth.decorators import login_required
from django.db.models import Max
import pdb

from dateutil import parser
import numpy as np 
import plotly.express as px 
import pandas as pd 

from app.functions import *
# Create your views here.


#home page 
@login_required
def home(request):
    changeSite = request.GET.get('id','')

    if changeSite == "":
        currentUser = request.user
        id = currentUser.id
        siteCode = id
    else:
        if int(changeSite) == 1:
            siteCode = int(changeSite)
        elif int(changeSite) == 2:
            siteCode = int(changeSite)
    request.session['siteCode'] = siteCode
        #request.session['id'] == ""
    
    maintenanceData = getMaintenanceData(siteCode)
    brushData = getBrushData(siteCode)

    curtains = [brushData['Curtains']]
    wraps = [brushData['Wrap Brushes']]
    sideWashers = [brushData['Side Washers']]
    rockers = [brushData['Rocker Brushes']]

    df = returnDataFrames(siteCode)
    df1 = df.values.tolist()
    today = datetime.date.today().strftime("%m/%d/%Y")
    total, pastDay = 0, 0
    for i in df1:
        for j in i:
            if isinstance(j, datetime.date) == True or j == None:
                if j == None:
                    pastDay += 1
                    total += 1
                else:
                    j = j.strftime("%m/%d/%Y")
                    if j < today: 
                        pastDay += 1
                        total += 1
                    else: total += 1

    allGood = total - pastDay
    pastDuePercent = round(((pastDay / total) * 100), 2)
    upToDatePercent = round((100 - pastDuePercent), 2)
    
    behind, upcoming, behindCount, upcomingCount = None, None, 0, 0
    behind, upcoming = getTasks(siteCode)
    behindUpcomingHeaders = ["Side", "Set Number", "Brush", "Date Replaced", "Component"]

    behindCount = behind.shape[0]
    upcomingCount = upcoming.shape[0]
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
        'behind' : behind,
        'behindHeaders' : behindUpcomingHeaders,
        'behindCount' : behindCount,
        'upcoming' : upcoming,
        'upcomingCount' : upcomingCount,
    }

    return render(request, 'index.html', context)

@login_required
def updateSchedule(request):

    siteCode = request.session.get('siteCode', '')

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
                    headersBrushes, temp = getSpecificCompData(i, siteCode)
                    z.append(temp)
                for j in z:
                    for x in j:
                        brushes.append(x)
            elif int(data) == 13:
                z = []
                brushes = []
                for i in brushesStrings:
                    headersBrushes, temp = getSpecificCompData(i, siteCode)
                    z.append(temp)
                for j in z:
                    for x in j:
                        brushes.append(x)
                a = []
                compData = []       
                for i in otherCompStrings:
                    headersComp, temp = getSpecificCompData(i, siteCode)
                    a.append(temp)
                for j in a:
                    for x in j:
                        compData.append(x)
            else:
                for i in choices: 
                    if int(data) == int(i[0]):
                        comp = i[1]
                        break 
                component = comp
                if comp in brushesStrings:
                    headersBrushes, brushes = getSpecificCompData(comp, siteCode)
                elif comp in otherCompStrings:
                    headersComp, compData = getSpecificCompData(comp, siteCode)
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

@login_required
def update_inventory(request):
    siteCode = request.session.get('siteCode', '')
    inventory = getInventoryData(siteCode)
    inventoryHeaders = ["Part", "Model Number", "Quantity"]
    context = {
        'inventory' : inventory,
        'headers' : inventoryHeaders,
    }
    return render(request, 'update_inventory.html', context)

@login_required
def inventory_details(request):
    context = {

    }
    return render(request, 'inventory_details.html', context)

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
    currentUser = request.user
    id = currentUser.id

    if request.method == "POST":
        if 'edit' in request.POST:
            return redirect('edit_profile')
        if 'light' in request.POST:
            theme = False
        if 'dark' in request.POST:
            theme = True

        employee = Employee.objects.get(user_id=id)
        employee.darkMode = theme
        employee.save()
    
    userData = pd.DataFrame(list(User.objects.all().values().filter(id=id)))
    userData = userData.drop(userData.columns[[1, 2, 3, 8, 9, 10]], axis=1)
    site = pd.DataFrame(list(Employee.objects.all().values().filter(id=id)))
    site = site.drop(site.columns[[0, 2]], axis=1)
    site = site.values.tolist()
    site = site[0][0]

    x = None 
    if int(site) == 1:
        x = "Gull Rd."
    elif int(site) == 2:
        x = "Stadium Dr."

    userData['site'] = x

    context = {
        'site' : x,
        'df' : userData,
    }
    return render(request, 'profile.html', context)

def edit_profile(request):
    currentUser = request.user
    id = currentUser.id

    if request.method == 'POST':
        form = editProfileForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('name')
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            site = form.cleaned_data.get('site')
            # update auth_user 
            userData = User.objects.get(id=id)
            name = name.split(" ")
            firstName = name[0]
            lastName = name[1]
            userData.first_name = firstName
            userData.last_name = lastName
            userData.username = username 
            userData.email = email 

            # update extended user - employee 
            extendedUserData = Employee.objects.get(user_id=id)
            extendedUserData.site=site 

            userData.save()
            extendedUserData.save()
            return redirect('profile')
    else:
        form = editProfileForm()

    context={
        'form' : form
    }
    return render(request, 'edit_profile.html', context)

#---------------------------------------
# Below are my ajax/json parsers that recieve data from my table in "Update Schedule"/"Update Inventory"
def saveInventory(request):
    siteCode = request.session['siteCode']
    delete = request.POST.get('delete', '')

    if delete == "True":
        id = int(request.POST.get('id', ''))
        data = Inventory.objects.get(id=id)
        data.delete()

    if delete == "False":
        id = request.POST.get('id', '')
        value = request.POST.get('value', '')
        type = request.POST.get("type", '')
        if id == "":
            maxId = Inventory.objects.aggregate(Max('id'))
            maxId = int(maxId['id__max'])
            newId = int(maxId) + 1
            #if type == "" or value == "":
            newObj = Inventory(newId, None, None, 0, siteCode)
            newObj.save()
            """ if type == 'partName':
                newObj = Inventory(newId, value, None, 0)
                newObj.save()
            if type == 'modelNumber':
                newObj = Inventory(newId, None, value, 0)
                newObj.save()
            if type == 'quantity':
                newObj = Inventory(newId, None, None, value)
                newObj.save() """
        else:
            inventoryData = Inventory.objects.get(id=id)
            if type == 'partName':
                inventoryData.partName = value 
            if type == 'modelNumber':
                inventoryData.modelNumber = value
            if type == 'quantity':
                inventoryData.quantity = value 
            inventoryData.save()
        
    return JsonResponse({"success" : "Updated"})

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