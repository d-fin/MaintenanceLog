import pandas as pd 
from django.core.mail import EmailMessage
from django.conf import settings 
from django.template.loader import render_to_string

from .models import * 
from .functions import getTasks

from celery import shared_task


@shared_task
def sendBrushUpdateEmail():
    #----------------------------------------------
    # email testing 
    siteCode = 1
    admin = User.objects.all().values_list('username', 'email').filter(id=17)
    adminUsername = admin[0][0]
    adminEmail = admin[0][1]

    # Below is retrieving data to populate email 
    brushes = list(Brush.objects.all().values_list('brushStyle').distinct())
    brushes = [x[0] for x in brushes]
    behindForEmail, upcomingForEmail = getTasks(siteCode)
    behindForEmail = behindForEmail.values.tolist()
    upcomingForEmail = upcomingForEmail.values.tolist()
    x = []
    for i in behindForEmail:
        temp = []
        tempStr = None
        tempStr = f'Set # {i[1]}'
        if i[0] == 'D': tempStr += ' - Driver'
        else: tempStr += ' - Passenger'
        temp = [tempStr, i[2], i[4], i[3].strftime("%m/%d/%Y")]
        x.append(temp)
    for i in upcomingForEmail:
        temp = []
        tempStr = None
        tempStr = f'Set # {i[1]}'
        if i[0] == 'D': tempStr += ' - Driver'
        else: tempStr += ' - Passenger'
        temp = [tempStr, i[2], i[4], i[3].strftime("%m/%d/%Y")]
        x.append(temp)
    #-----------------------------------------------------------
    # making and sending email. 
    newDf = pd.DataFrame(x, columns=['Set/Side', 'Brush', 'Component', 'DateReplaced'])
    template = render_to_string('email_updateBrushes.html', {'name' : adminUsername, 'df' : newDf})
    email = EmailMessage(
        'It\'s almost time to update a piece of equipment!',
        template, 
        settings.EMAIL_HOST_USER, 
        [adminEmail]
    )

    # in production set fail_silently=True
    email.fail_silently = False 
    email.send()
    #----------------------------------------------