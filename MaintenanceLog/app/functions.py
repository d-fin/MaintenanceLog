import pdb
import pandas as pd 
from django.db import connection
import datetime
from .models import * 
from dateutil.relativedelta import relativedelta

def getSpecificCompData(comp):
    brushes =  ['Curtain', 'Rocker Brush', 'Wrap Brush', 'Side Washer']
    otherComp = ['Takeup Drum', 'Sprocket', 'Fork Cover', 'Fork Cylinder',
        'Heco Drive', 'Conveyor Hydraulic Motor', 'Chain/Rollers']
    
    dataDict = {
        "TakeUp Drum" : "drum",
        "Sprocket" : "sprocket",
        "Fork Cover" : "forkCover",
        "Fork Cylinder" : "forkCylinder",
        "Heco Drive" : "hecoDrive",
        "Conveyor Hydraulic Motor" : "convHydMotor",
        "Chain/Rollers" : "chainRollers"
    }

    brushData, brushComponents, compData, headers = None, None, None, None

    if comp in brushes: 
        brushData = getSpecificBrushData(comp)
        ids = brushData['id'].to_list()
        brushComponents = pd.DataFrame(columns=['id', 'brushID', 'motor', 'shaft', 'bearings', 'upperBearings', 'cloth', 'siteCode'])
        
        z = []
        for i in ids:
            temp = getSpecificComponentData(i)
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
        """ ids = [1, 2, 3, 4, 5, 6, 7]
        compData = pd.DataFrame(columns=["id", "component", "dateReplaced", "dueDate", "notes", "siteCode"])
        z = []
        for i in ids:
            temp = getSpecificComponentData(i)
            z.append(temp)
        compData = pd.concat(z) """
        #comp = dataDict[comp]
        compData = pd.DataFrame(list(Maintenance.objects.all().values().filter(component = comp)))
        compData = compData.drop(compData.columns[[5]], axis=1)
        compData = compData.values.tolist()
        for i in compData:
            for j in range(len(i)):
                if isinstance(i[j], datetime.date) == True:
                    temp = returnDate(i[j])
                    i[j] = temp

        return headers, compData 

def returnDate(x):
    #x = x + relativedelta(months=6)
    x = x.strftime("%m/%d/%Y")
    return x

def getSpecificBrushData(brush):
    return pd.DataFrame(list(Brush.objects.all().values().filter(brushStyle = brush))) 

def getSpecificComponentData(id):
    return pd.DataFrame(list(BrushComponent.objects.all().values().filter(brushID=id)))

def getSpecificBrushDataById(brush):
    return pd.DataFrame(list(Brush.objects.all().values().filter(id = brush)))

def returnDataFrames():
    brushes =  ['Curtain', 'Rocker Brush', 'Wrap Brush', 'Side Washer']
    otherComp = ['Takeup Drum', 'Sprocket', 'Fork Cover', 'Fork Cylinder',
        'Heco Drive', 'Conveyor Hydraulic Motor', 'Chain/Rollers']
    brushIds = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

    df = pd.DataFrame(columns=['id', 'side', 'setNum', 'brushStyle', 'siteCode'])
    z = []
    for brush in brushIds:
        temp = getSpecificBrushDataById(brush)
        z.append(temp)

    df = pd.concat(z)
    
    df2 = pd.DataFrame(columns=['id', 'brushID', 'motor', 'shaft', 'bearings', 'upperBearings', 'cloth', 'shocks', 'siteCode'])
    z2 = []
    for id in brushIds:
        temp = getSpecificComponentData(id)
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
            cursor.execute("SELECT brushID, motor, shaft, bearings, upperBearings, cloth, shocks FROM app_brushComponent WHERE siteCode = " + str(siteCode))
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
    maintenanceData = []
    compName = ['Takeup Drum', 'Sprocket', 'Fork Cover', 'Fork Cylinder', 'Heco Drive', 'Conveyor Hydraulic Motor', 'Chain/Rollers']
    headers = [1, 2, 3, 4]
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM app_maintenance WHERE siteCode = " + str(siteCode))
        
        z = 0
        for i in cursor: 
            temp = {}
            kount = 0 
            headerCount = 0
            temp[headers[headerCount]] = compName[z] 
            headerCount += 1 
            for j in i:
                
                if kount == 0 or kount == 1 or kount == 5: pass 
                else:
                    if isinstance(j, datetime.date) == True:
                         j = j.strftime("%m/%d/%Y")
                    temp[headers[headerCount]] = j
                    headerCount += 1
                kount += 1
            maintenanceData.append(temp)
            z += 1
    return maintenanceData