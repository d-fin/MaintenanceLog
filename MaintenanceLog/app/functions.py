from django.core.mail import EmailMessage
from django.conf import settings 
from django.template.loader import render_to_string

import pdb
import pandas as pd 
from django.db import connection
import datetime
from .models import * 
from dateutil.relativedelta import relativedelta

def sendNewUserEmail(newUserID):
    df = pd.DataFrame(User.objects.all().values().filter(id=newUserID))
    adminName = 'David Finley'
    adminEmail = 'dfinley5656@gmail.com'
    template = render_to_string('email_newUser.html', context = {'user' : df, 'adminName' : adminName})
    email = EmailMessage(
        'New User Alert!',
        template,
        settings.EMAIL_HOST_USER,
        [adminEmail]
    )
    # in production set fail_silently=True
    email.fail_silently = False 
    email.send()

def getHydraulicHoseData(siteCode):
    brushStyles = pd.DataFrame(list(Brush.objects.all().values_list('brushStyle').distinct()))
    brushStyles = brushStyles.values.tolist()
    brushStyles = [x[0] for x in brushStyles]

    x = {}
    for i in brushStyles:
        if i != 'Curtain':
            brush = pd.DataFrame(Brush.objects.all().values_list('id').filter(brushStyle=i).filter(siteCode=siteCode))
            brush = brush.values.tolist()
            brush = [x[0] for x in brush]
            x[i] = brush

    wrap, side, rocker = None, None, None 
    for key, val in x.items():
        if key == 'Wrap Brush':
            brushDf = pd.DataFrame(list(Brush.objects.all().values().filter(brushStyle=key).filter(siteCode=siteCode)))
            hydrHoseDf = pd.DataFrame(list(HydraulicHoses.objects.all().values().filter(brushID__in=val)))
            brushDf.rename(columns={'id':'brushID'}, inplace=True)
            wrap = pd.merge(hydrHoseDf, brushDf, on='brushID', how='left')
        if key == 'Side Washer':
            brushDf = pd.DataFrame(list(Brush.objects.all().values().filter(brushStyle=key).filter(siteCode=siteCode)))
            hydrHoseDf = pd.DataFrame(list(HydraulicHoses.objects.all().values().filter(brushID__in=val)))
            brushDf.rename(columns={'id':'brushID'}, inplace=True)
            side = pd.merge(hydrHoseDf, brushDf, on='brushID', how='left')
        if key == 'Rocker Brush':
            brushDf = pd.DataFrame(list(Brush.objects.all().values().filter(brushStyle=key).filter(siteCode=siteCode)))
            hydrHoseDf = pd.DataFrame(list(HydraulicHoses.objects.all().values().filter(brushID__in=val)))
            brushDf.rename(columns={'id':'brushID'}, inplace=True)
            rocker = pd.merge(hydrHoseDf, brushDf, on='brushID', how='left')

    wrap.drop(['siteCode_x', 'siteCode_y', 'brushStyle'], axis=1, inplace=True)
    rocker.drop(['siteCode_x', 'siteCode_y', 'brushStyle'], axis=1, inplace=True)
    side.drop(['siteCode_x', 'siteCode_y', 'brushStyle'], axis=1, inplace=True)
    
    return wrap, side, rocker

def getSpecificCompData(comp, siteCode):
    brushes =  ['Curtain', 'Rocker Brush', 'Wrap Brush', 'Side Washer']
    otherComp = ['Takeup Drum', 'Sprocket', 'Fork Cover', 'Fork Cylinder',
        'Heco Drive', 'Conveyor Hydraulic Motor', 'Chain/Rollers']
    
    brushData, brushComponents, compData, headers = None, None, None, None

    if comp in brushes: 
        brushData = getSpecificBrushData(comp, siteCode)
        ids = brushData['id'].to_list()
        brushComponents = pd.DataFrame(columns=['id', 'brushID', 'motor', 'shaft', 'bearings', 'upperBearings', 'cloth', 'siteCode'])
        
        z = []
        for i in ids:
            temp = getSpecificComponentData(i, siteCode)
            z.append(temp)
        brushData = brushData.drop(brushData.columns[[3, 4]], axis=1)
        brushComponents = brushComponents.drop(brushComponents.columns[[1, 2]], axis=1)    
        brushComponents = pd.concat(z)
        brushData = pd.merge(brushData, brushComponents, on="id", how="left")
        brushData = brushData.drop(brushData.columns[[0, 10]], axis=1)
        headers = ['Side', 'Set Num', 'Motor', 'Shaft', 'Bearings', 'Upper Bearings', 'Cloth', 'Shocks']
        brushData = brushData.values.tolist()
        for i in brushData:
            for j in range(len(i)):
                if isinstance(i[j], datetime.date) == True:
                    temp = returnDate(i[j])
                    i[j] = temp
            
        return headers, brushData
    
    if comp in otherComp:
        headers = ["Part", "Date Replaced", "Due Date", "Notes"]
        compData = pd.DataFrame(list(Maintenance.objects.all().values().filter(component = comp).filter(siteCode=siteCode)))
        compData = compData.drop(compData.columns[[5]], axis=1)
        compData = compData.values.tolist()
        for i in compData:
            for j in range(len(i)):
                if isinstance(i[j], datetime.date) == True:
                    temp = returnDate(i[j])
                    i[j] = temp

        return headers, compData 

def getTasks(siteCode):
    brushDf = returnDataFrames(siteCode)
    
    brushDfList = brushDf.values.tolist()

    compDf = returnComponentDataFrames(siteCode)
    compDf = compDf.values.tolist()

    behindDf = pd.DataFrame(columns=["side", "setNum", "brushStyle", "dateReplaced", "component"])
    upcomingDf = pd.DataFrame(columns=["side", "setNum", "brushStyle", "dateReplaced", "component"])
    behind = []
    upcoming = []

    today = datetime.date.today()
    thirtyDaysOut = today + relativedelta(days=30)
    today = date.today()
    for i in brushDfList:
        k = 0
        for j in i:
            temp = []
            upcomingTemp = []
            dontPutInBoth = False
            if isinstance(j, datetime.date) == True:
                j = j + relativedelta(months=6)
                if j < today: 
                    dontPutInBoth = True
                    if k == 4:
                        temp.append(i[1])
                        temp.append(i[2])
                        temp.append(i[3])
                        temp.append(i[4])
                        temp.append("Motor")
                        behind.append(temp)
                    if k == 5:
                        temp.append(i[1])
                        temp.append(i[2])
                        temp.append(i[3])
                        temp.append(i[5])
                        temp.append("Shaft")
                        behind.append(temp)
                    if k == 6:
                        temp.append(i[1])
                        temp.append(i[2])
                        temp.append(i[3])
                        temp.append(i[6])
                        temp.append("Bearings")
                        behind.append(temp)
                    if k == 7:
                        temp.append(i[1])
                        temp.append(i[2])
                        temp.append(i[3])
                        temp.append(i[7])
                        temp.append("Upper Bearings")
                        behind.append(temp)
                    if k == 8:
                        temp.append(i[1])
                        temp.append(i[2])
                        temp.append(i[3])
                        temp.append(i[8])
                        temp.append("CLoth")
                        behind.append(temp)
                    if k == 9:
                        temp.append(i[1])
                        temp.append(i[2])
                        temp.append(i[3])
                        temp.append(i[9])
                        temp.append("Shocks")
                        behind.append(temp)
                    if len(temp) == 0: pass 
                    else: behindDf.loc[len(behindDf)] = temp
                if j > today and j <= thirtyDaysOut and dontPutInBoth == False:
                    if k == 4:
                        upcomingTemp.append(i[1])
                        upcomingTemp.append(i[2])
                        upcomingTemp.append(i[3])
                        upcomingTemp.append(i[4])
                        upcomingTemp.append("Motor")
                        upcoming.append(temp)
                    if k == 5:
                        upcomingTemp.append(i[1])
                        upcomingTemp.append(i[2])
                        upcomingTemp.append(i[3])
                        upcomingTemp.append(i[5])
                        upcomingTemp.append("Shaft")
                        upcoming.append(temp)
                    if k == 6:
                        upcomingTemp.append(i[1])
                        upcomingTemp.append(i[2])
                        upcomingTemp.append(i[3])
                        upcomingTemp.append(i[6])
                        upcomingTemp.append("Bearings")
                        upcoming.append(temp)
                    if k == 7:
                        upcomingTemp.append(i[1])
                        upcomingTemp.append(i[2])
                        upcomingTemp.append(i[3])
                        upcomingTemp.append(i[7])
                        upcomingTemp.append("Upper Bearings")
                        upcoming.append(temp)
                    if k == 8:
                        upcomingTemp.append(i[1])
                        upcomingTemp.append(i[2])
                        upcomingTemp.append(i[3])
                        upcomingTemp.append(i[8])
                        upcomingTemp.append("CLoth")
                        upcoming.append(temp)
                    if k == 9:
                        upcomingTemp.append(i[1])
                        upcomingTemp.append(i[2])
                        upcomingTemp.append(i[3])
                        upcomingTemp.append(i[9])
                        upcomingTemp.append("Shocks")
                        upcoming.append(temp)
                    if len(upcomingTemp) == 0: pass 
                    else: upcomingDf.loc[len(upcomingDf)] = upcomingTemp
            k += 1

    return behindDf, upcomingDf

def returnDate(x):
    return x.strftime("%m/%d/%Y")
    
def getSpecificBrushData(brush, siteCode):
    return pd.DataFrame(list(Brush.objects.all().values().filter(brushStyle = brush).filter(siteCode=siteCode))) 

def getSpecificComponentData(id, siteCode):
    return pd.DataFrame(list(BrushComponent.objects.all().values().filter(brushID=id).filter(siteCode=siteCode)))

def getSpecificBrushDataById(brush, siteCode):
    return pd.DataFrame(list(Brush.objects.all().values().filter(id = brush).filter(siteCode=siteCode)))

def returnComponentDataFrames(siteCode):
    otherComp = ['Takeup Drum', 'Sprocket', 'Fork Cover', 'Fork Cylinder',
        'Heco Drive', 'Conveyor Hydraulic Motor', 'Chain/Rollers']

    df = pd.DataFrame(columns=["id", "component", "dateReplaced", "dueDate", "notes", "siteCode"])
    z = []
    for i in otherComp:
        try:
            temp = pd.DataFrame(list(Maintenance.objects.all().values().filter(component = i).filter(siteCode=siteCode)))
        except Exception as e:
            temp = []
        finally:
            z.append(temp)
    try:
        df = pd.concat(z)
    except Exception as e:
        pass 
    else:
        df = df.drop(df.columns[[5]], axis=1)

    return df

def returnDataFrames(siteCode):
    brushes =  ['Curtain', 'Rocker Brush', 'Wrap Brush', 'Side Washer']
    brushIds = None 
    if siteCode == 1: brushIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    else: brushIds = [14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

    df = pd.DataFrame(columns=['id', 'side', 'setNum', 'brushStyle', 'siteCode'])
    z = []
    for brush in brushIds:
        temp = getSpecificBrushDataById(brush, siteCode)
        z.append(temp)

    df = pd.concat(z)
    
    df2 = pd.DataFrame(columns=['id', 'brushID', 'motor', 'shaft', 'bearings', 'upperBearings', 'cloth', 'shocks', 'siteCode'])
    z2 = []
    for id in brushIds:
        temp = getSpecificComponentData(id, siteCode)
        z2.append(temp)
    df2 = pd.concat(z2)

    df = df.drop(df.columns[[4]], axis=1)
    df2 = df2.drop(df2.columns[[1, 8]], axis=1)
    
    allData = pd.merge(df, df2, on="id", how='left')
    allData.sort_values(by="id", ascending=False)
    
    return allData

def getBrushData(siteCode):
    def getBrushName(siteCode):
        brushName = []
        headers = ['brushId', 'side', 'setNum', 'brushStyle']
        with connection.cursor() as cursor:
            cursor.execute("SELECT id, side, setNum, brushStyle FROM app_brush WHERE siteCode = " + str(siteCode))
            for data in cursor:
                temp = {}
                i = 0
                for x in data: 
                    temp[headers[i]] = x 
                    i += 1
                brushName.append(temp) 
        return brushName

    def brushCompData(siteCode):
        brushData = []
        headers = ['brushId', 'motor', 'shaft', 'bearings', 'upperBearings', 'cloth', 'shocks']
        with connection.cursor() as cursor:
            cursor.execute("SELECT brushID, motor, shaft, bearings, upperBearings, cloth, shocks FROM app_brushcomponent WHERE siteCode = " + str(siteCode))
            for data in cursor:
                temp = {}
                i = 0 
                for x in data:
                    if isinstance(x, datetime.date) == True:
                         x = x.strftime("%m/%d/%Y")
                    temp[headers[i]] = x 
                    i += 1
                brushData.append(temp)
        return brushData
    
    brushName = getBrushName(siteCode)
    brushData = brushCompData(siteCode)
    df1 = pd.DataFrame(brushName)
    df2 = pd.DataFrame(brushData)
    df = pd.merge(df1, df2, on="brushId", how="left")

    wrapData = df[df['brushStyle'] == 'Wrap Brush']
    sideWasherData = df[df['brushStyle'] == "Side Washer"]
    rockerData = df[df['brushStyle'] == "Rocker Brush"]
    curtainData = df[df['brushStyle'] == "Curtain"]

    curtainData = curtainData.drop(df.columns[[0, 1, 3, 5, 6, 7, 9]], axis=1)
    rockerData = rockerData.drop(df.columns[[0, 3, 5, 7]], axis=1)
    sideWasherData = sideWasherData.drop(df.columns[[0, 3]], axis=1)
    wrapData = wrapData.drop(df.columns[[0, 3]], axis=1)

    wrap, curtain, sideWasher, rocker, = [], [], [], []

    
    wrapMax = int(wrapData['setNum'].max())
    for i in range(1, wrapMax + 1):
        temp = wrapData[wrapData['setNum'] == i]
        temp.drop(temp.columns[[1]], axis=1)
        temp = temp.to_dict('records')
        wrap.append(temp)
    curtainMax = int(curtainData['setNum'].max())
    for i in range(1, curtainMax + 1):
        temp = curtainData[curtainData['setNum'] == i]
        temp.drop(temp.columns[[1]], axis=1)
        temp = temp.to_dict('records')
        curtain.append(temp)
    sideWasherMax = int(sideWasherData['setNum'].max())
    for i in range(1, sideWasherMax + 1):
        temp = sideWasherData[sideWasherData['setNum'] == i]
        temp.drop(temp.columns[[1]], axis=1)
        temp = temp.to_dict('records')
        sideWasher.append(temp)
    rockerMax = int(rockerData['setNum'].max())
    for i in range(1, rockerMax + 1):
        temp = rockerData[rockerData['setNum'] == i]
        temp.drop(temp.columns[[1]], axis=1)
        temp = temp.to_dict('records')
        rocker.append(temp)
 
    return {
        'Curtains' : curtain,
        'Rocker Brushes' : rocker,
        'Side Washers' : sideWasher, 
        'Wrap Brushes' : wrap}

def getMaintenanceData(siteCode):
    maintenanceData = pd.DataFrame(list(Maintenance.objects.all().values().filter(siteCode=siteCode)))
    maintenanceData = maintenanceData.drop(maintenanceData.columns[[5]], axis=1)
    maintenanceData = maintenanceData.values.tolist()
    maintenanceData = convertTime(maintenanceData)
    
    return maintenanceData

def getInventoryData(siteCode):
    inventoryData = pd.DataFrame(columns=["id", "partName", "modelNumber", "quantity"])
    data = list(Inventory.objects.all().values().filter(siteCode=siteCode))
    for i in data:
        inventoryData.loc[len(inventoryData)] = i
    return inventoryData

def convertTime(df):
    for i in df:
            for j in range(len(i)):
                if isinstance(i[j], datetime.date) == True:
                    temp = returnDate(i[j])
                    i[j] = temp
    return df

def getBrushDataToDisplay(id, siteCode):
    wrapData = pd.DataFrame()
    brushData = pd.DataFrame()
    x = []
    y = []
    for i in id: 
        temp = pd.DataFrame(list(BrushComponent.objects.values().filter(siteCode=siteCode).filter(brushID=i)))
        temp2 = pd.DataFrame(list(Brush.objects.all().values().filter(siteCode=siteCode).filter(id=i)))
        x.append(temp)
        y.append(temp2)

    wrapData = pd.concat(x)
    brushData = pd.concat(y)

    brushData = brushData.drop(brushData.columns[[3, 4]], axis=1)
    wrapData = pd.merge(wrapData, brushData, on="id", how="right")

    wrapDataCurrent = wrapData[["side", "setNum", "brushID", "motor", "shaft", "bearings", "upperBearings", "cloth", "shocks"]]
    wrapDataDueDate = wrapData[["side", "setNum", "brushID", "motorDueDate", "shaftDueDate", "bearingsDueDate", "upperBearingsDueDate", "clothDueDate",  "shocksDueDate"]]
    wrapDataCurrent = wrapDataCurrent.values.tolist() 
    wrapDataDueDate = wrapDataDueDate.values.tolist()

    wrapDataCurrent = convertTime(wrapDataCurrent)
    wrapDataDueDate = convertTime(wrapDataDueDate)
    
    return wrapDataCurrent, wrapDataDueDate
