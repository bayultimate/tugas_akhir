'''

@author: root
'''
#!/usr/bin/python
#open file
from __future__ import division
import glob
import datetime
import os
from fileinput import filename
from epsilon.extime import Time

counter = 0
listSize = 0
capPath = ""
logPath = ""
fileLocation = ""
sensitivity = 0
listFile = list()
#variable for get data from log#
processYear = list()
processMonth = list()
processDate = list()
processHour = list()
processMinute = list()
processSecond = list()
processNumber = list()
processIpSrc = list()
processIpDest = list()
processProtocol = list()
processPortSrc = list()
processPortDest = list()
processPayload = list()
#variable for limit time cleaning from process list#
cleanYear = list()
cleanMonth = list()
cleanDate = list()
cleanHour = list()
cleanMinute = list()
cleanSecond = list()
cleanNumber = list()
cleanIpSrc = list()
cleanIpDest = list()
cleanProtocol = list()
cleanPortSrc = list()
cleanPortDest = list()
cleanPayload = list()
#variable for list of traffic#
noteYear = list()
noteMonth = list()
noteDate = list()
noteHour = list()
noteMinute = list()
noteSecond = list()
noteNumber = list()
noteIpSrc = list()
noteIpDest = list()
noteProtocol = list()
notePortSrc = list()
notePortDest = list()
notePayload = list()
noteCount = list()
notePeriode = list()
noteFlowId = list()
noteCounter = 0
#flow with filter
#flowStartTime = list()
#flowYear = list()
#flowMonth = list()
#flowDate = list()
#flowHour = list()
#flowMinute = list()
#flowSecond = list()
#flowPortDest = list()
flowTotalPacket = list()
flowPercentage = list()
#flowPayload = list()
#flowPeriode = list()
#flowCounter = 0
#limit time#
limitYear = 0
limitMonth = 0
limitDate = 0
limitHour = 0
limitMinute = 0
limitSecond = 0


######function######

###get user configuration###
def Initialization():
    global capPath
    global logPath
    global sensitivity
    f = open ("/home/bayu/config_ta/config.txt","r")
    conf = f.readline()
    
    while conf:
        #print("masuk")
        splitData = conf.split(':')
        if (splitData[0] == "captured data path"):
            capPath = splitData[1]
        elif (splitData[0] == "log path"):
            logPath = splitData[1]
        elif (splitData[0] == "sensitivity"):
            sensitivity = splitData[1]
        conf = f.readline()
    
    f.close()
    capPath = capPath.lstrip()
    logPath =  logPath.strip()    
    sensitivity = sensitivity.strip()
    #print (capPath)
    #print (logPath)
    #print (sensitivity)
    return

def Filecheck():
    global capPath
    global listFile
    capPath = capPath.strip()
    #print ("------")
    #print (capPath)
   
    globFile = ''
    globFile += capPath+"*.txt"
    #print globFile
    listFile = glob.glob(globFile)
    for i in range(0,len(listFile)):
        print (listFile[i])
    return

def Cleanvariable():
    
    del processYear[0:len(processYear)]
    del processMonth[0:len(processMonth)]
    del processDate[0:len(processDate)]
    del processHour[0:len(processHour)]
    del processMinute[0:len(processMinute)]
    del processSecond[0:len(processSecond)]
    del processNumber[0:len(processNumber)]
    del processIpSrc[0:len(processIpSrc)]
    del processIpDest[0:len(processIpDest)]
    del processProtocol[0:len(processProtocol)]
    del processPortSrc[0:len(processPortSrc)]
    del processPortDest[0:len(processPortDest)]
    del processPayload[0:len(processPayload)]
    #variable for limit time cleaning from process list#
    del cleanYear[0:len(cleanYear)]
    del cleanMonth[0:len(cleanMonth)]
    del cleanDate[0:len(cleanDate)]
    del cleanHour[0:len(cleanHour)]
    del cleanMinute[0:len(cleanMinute)]
    del cleanSecond[0:len(cleanSecond)]
    del cleanNumber[0:len(cleanNumber)]
    del cleanIpSrc[0:len(cleanIpSrc)]
    del cleanIpDest[0:len(cleanIpDest)]
    del cleanProtocol[0:len(cleanProtocol)]
    del cleanPortSrc[0:len(cleanPortSrc)]
    del cleanPortDest[0:len(cleanPortDest)]
    del cleanPayload[0:len(cleanPayload)]
    #variable for list of traffic#
    del noteYear[0:len(noteYear)]
    del noteMonth[0:len(noteMonth)]
    del noteDate[0:len(noteDate)]
    del noteHour[0:len(noteHour)]
    del noteMinute[0:len(noteMinute)]
    del noteSecond[0:len(noteSecond)]
    del noteNumber[0:len(noteNumber)]
    del noteIpSrc[0:len(noteIpSrc)]
    del noteIpDest[0:len(noteIpDest)]
    del noteProtocol[0:len(noteProtocol)]
    del notePortSrc[0:len(notePortSrc)]
    del notePortDest[0:len(notePortDest)]
    del notePayload[0:len(notePayload)]
    del noteCount[0:len(noteCount)]
    del notePeriode[0:len(notePeriode)]
    del noteFlowId[0:len(noteFlowId)]
    global noteCounter
    noteCounter = 0
    #flow with filter
    #flowStartTime = list()
    #flowYear = list()
    #flowMonth = list()
    #flowDate = list()
    #flowHour = list()
    #flowMinute = list()
    #flowSecond = list()
    #flowPortDest = list()
    del flowTotalPacket[0:len(flowTotalPacket)]
    del flowPercentage[0:len(flowPercentage)]
    #flowPayload = list()
    #flowPeriode = list()
    #flowCounter = 0
    #limit time#
    global limitYear
    limitYear = 0
    global limitMonth
    limitMonth = 0
    global limitDate
    limitDate = 0
    global limitHour
    limitHour = 0
    global limitMinute
    limitMinute = 0
    global limitSecond
    limitSecond = 0
    return
    
###get data###
def Processdata(fileLocation):
    #print(fileLocation)
    localCounter = 0
    f = open (fileLocation,"r")
    data = f.readline()
        
    while data:        
        #print data
        splitData = data.split(':')
        if (len(splitData) < 13):
            break
        dataYear = splitData[0]
        dataMonth = splitData[1]
        dataDate = splitData[2]
        dataHour = splitData[3]
        dataMinute = splitData[4]
        dataSecond = splitData[5]
        dataNumber = splitData[6]
        dataIpSrc = splitData[7]
        dataIpDest = splitData[8]
        dataProtocol = splitData[9]
        dataPortSrc = splitData[10]
        dataPortDest = splitData[11]
        dataPayload = splitData[12]
        
        #print (dataNumber)
        
        processYear.insert(localCounter, dataYear)
        processMonth.insert(localCounter, dataMonth)
        processDate.insert(localCounter, dataDate)
        processHour.insert(localCounter, dataHour)
        processMinute.insert(localCounter, dataMinute)
        processSecond.insert(localCounter, dataSecond)
        processNumber.insert(localCounter, dataNumber)
        processIpSrc.insert(localCounter, dataIpSrc)
        processIpDest.insert(localCounter, dataIpDest)
        processProtocol.insert(localCounter, dataProtocol)
        processPortSrc.insert(localCounter, dataPortSrc)
        processPortDest.insert(localCounter, dataPortDest)
        processPayload.insert(localCounter, dataPayload)

        localCounter += 1
        data = f.readline()
    f.close()
    global counter
    counter = localCounter
    global listSize
    listSize = len(processNumber)
    #print (listSize)
    #print (counter)
    return

def waktu():
    global listSize
    global limitYear
    global limitMonth
    global limitDate
    global limitHour
    global limitMinute
    global limitSecond
    
    startYear = processYear[0]
    startMonth = processMonth[0]
    startDate = processDate[0]
    startHour = processHour[0]
    startMinute = processMinute[0]
    startSecond = processSecond[0]
    
    endYear = processYear[listSize - 1]
    endMonth = processMonth[listSize - 1]
    endDate = processDate[listSize - 1]
    endHour = processHour[listSize - 1]
    endMinute = processMinute[listSize - 1]
    endSecond = processSecond[listSize - 1]

    #print (startYear)
    #print (startMonth)
    #print (startDate)
    #print (startHour)
    #print (startMinute)
    #print (startSecond)
    #print ("--------------------------")
    #print (endYear)
    #print (endMonth)
    #print (endDate)
    #print (endHour)
    #print (endMinute)
    #print (endSecond)
    #print ("---------------------------")
    
    delay = 5
    
    tempSecond = int(endSecond) - delay
    tempMinute = int(endMinute) - 1
    tempHour = int(endHour) - 1
    tempDate = int(endDate) - 1
    tempMonth = int(endMonth) - 1
    
    if (tempDate <= 0 ):
        useDate = startDate
    else:
        useDate = tempDate
   
    if (tempMonth <= 0):
        useMonth = 12
    else:
        useMonth = tempMonth
   
     
    if (tempSecond >= 0 ):
        #print ("masuk a")
        limitYear = endYear
        limitMonth = endMonth
        limitDate = endDate
        limitHour = endHour
        limitMinute = endMinute
        limitSecond = tempSecond
    elif(tempSecond < 0 and tempMinute >= 1):
        #print ("masuk b")
        limitYear = endYear
        limitMonth = endMonth
        limitDate = endDate
        limitHour = endHour
        limitMinute = tempMinute
        limitSecond = 59  + tempSecond
    elif(tempSecond < 0 and tempMinute < 0 and tempHour >= 0):
        #print ("masuk d")
        limitYear = endYear
        limitMonth = endMonth
        limitDate = endDate
        limitHour = tempHour
        limitMinute = 59
        limitSecond = 59 + tempSecond
    elif(tempSecond < 0 and tempMinute < 0 and tempHour < 0 and tempDate > 0):
        #print ("masuk e")
        limitYear = endYear
        limitMonth = endMonth
        limitDate = tempDate
        limitHour = 23
        limitMinute = 59
        limitSecond = 59 + tempSecond
    elif(tempSecond < 0 and tempMinute < 0 and tempHour < 0 and tempDate <= 0 and tempMonth > 0):
        #print ("masuk f")
        limitYear = endYear
        limitMonth = tempMonth
        limitDate = useDate
        limitHour = 23
        limitMinute = 59
        limitSecond = 59 + tempSecond
    elif(tempSecond < 0 and tempMinute < 0 and tempHour < 0 and tempDate <= 0 and tempMonth <= 0 ):
        #print ("print g")
        limitYear = endYear - 1
        limitMonth = 12
        limitDate = useDate
        limitHour = 23
        limitMinute = 59
        limitSecond = 59 + tempSecond
                
    #print (limitYear)
    #print (limitMonth)
    #print (limitDate)
    #print (limitHour)
    #print (limitMinute)
    #print (limitSecond)
    #print ("-------------------------------")
    
    if (limitSecond < 10):
        limitSecond = "0" + str(limitSecond)
        
    #print (limitYear)
    #print (limitMonth)
    #print (limitDate)
    #print (limitHour)
    #print (limitMinute)
    #print (limitSecond)
    #print ("-------------------------------")
    
    return

def Cleandata():
    limit = str(limitYear) + str(limitMonth) + str(limitDate) + str(limitHour) + str(limitMinute) + str(limitSecond)
    #print (limit)
    for i in range(0,listSize):
        temp = processYear[i] + processMonth[i] + processDate[i] + processHour[i] + processMinute[i] + processSecond[i]
        if (temp <= limit):
            cleanYear.append(processYear[i])
            cleanMonth.append(processMonth[i])
            cleanDate.append(processDate[i])
            cleanHour.append(processHour[i])
            cleanMinute.append(processMinute[i])
            cleanSecond.append(processSecond[i])
            cleanNumber.append(processNumber[i])
            cleanIpSrc.append(processIpSrc[i])
            cleanIpDest.append(processIpDest[i])
            cleanProtocol.append(processProtocol[i])
            cleanPortSrc.append(processPortSrc[i])
            cleanPortDest.append(processPortDest[i])
            cleanPayload.append(processPayload[i])
    return


    
def Printdata():
    global counter
    global noteCounter
    localCounter = counter
    #print (localCounter)        
    return
    
def Selectdata():
    cleanLen = len(cleanNumber)
    localCounter = counter
    global noteCounter
    noteYear.insert(0,cleanYear[0])
    noteMonth.insert(0,cleanMonth[0])
    noteDate.insert(0,cleanDate[0])
    noteHour.insert(0,cleanHour[0])
    noteMinute.insert(0,cleanMinute[0])
    noteSecond.insert(0,cleanSecond[0])
    noteNumber.insert(0,cleanNumber[0])
    noteIpSrc.insert(0,cleanIpSrc[0])
    noteIpDest.insert(0,cleanIpDest[0])
    noteProtocol.insert(0,cleanProtocol[0])
    notePortSrc.insert(0,cleanPortSrc[0])
    notePortDest.insert(0,cleanPortDest[0])
    notePayload.insert(0,cleanPayload[0])
    noteCount.insert(0,1)
    noteCounter += 1

    flag = 0
    for i in range(1,cleanLen):

        flag = 0
        for j in range(0,noteCounter):
            if (cleanIpSrc[i] == noteIpSrc[j] and cleanIpDest[i] == noteIpDest[j] and cleanPortDest[i] == notePortDest[j] and cleanPayload[i] == notePayload[j]):          
                temp = noteCount[j]
                temp += 1
                noteCount[j] = temp
                flag = 1
     
        if (flag == 0):
            noteYear.append(cleanYear[i])
            noteMonth.append(cleanMonth[i])
            noteDate.append(cleanDate[i])
            noteHour.append(cleanHour[i])
            noteMinute.append(cleanMinute[i])
            noteSecond.append(cleanSecond[i])
            noteNumber.append(cleanNumber[i])
            noteIpSrc.append(cleanIpSrc[i])
            noteIpDest.append(cleanIpDest[i])
            noteProtocol.append(cleanProtocol[i])
            notePortSrc.append(cleanPortSrc[i])
            notePortDest.append(cleanPortDest[i])
            notePayload.append(cleanPayload[i])
            noteCount.append(1)
            noteCounter += 1
            flag = 0
    return

def Detectflow():
    global flowCounter
    global noteCounter
    cleanLen = len(cleanNumber)
    differenceTime = list()
    for i in range(0,noteCounter):
        totalDifference = 0
        periodeDifference = 0
        differenceLen = 0
        tempNoteTime = noteYear[i] + noteMonth[i] + noteDate[i] + noteHour[i] + noteMinute[i] + noteSecond[i]
        del differenceTime[0:len(differenceTime)]
        #print ("--------------------------------------------")
        for j in range(0,cleanLen):
            if(cleanIpSrc[j] == noteIpSrc[i] and cleanIpDest[j] == noteIpDest[i] and cleanPortDest[j] == notePortDest[i] and cleanPayload[j] == notePayload[i]):
                tempCleanTime = cleanYear[j] + cleanMonth[j] + cleanDate[j] + cleanHour[j] + cleanMinute[j] + cleanSecond[j]
                #print("tempnotetime: " + str(tempNoteTime))
                #print("tempcleantime: " + str(tempCleanTime)) 
                if (tempNoteTime != tempCleanTime ):
                    tempDifference = int(tempCleanTime) - int(tempNoteTime)
                    differenceTime.append(tempDifference)
                    differenceLen = len(differenceTime)
                    tempNoteTime = tempCleanTime
                    
        if(differenceLen > 0):            
            for k in range(0,differenceLen):
                totalDifference = totalDifference + differenceTime[k]
            periodeDifference = totalDifference / differenceLen
        else:
            totalDifference = 0 
            periodeDifference = 0
            
        #print ("total difference = " + str(totalDifference))
        #print ("difference time = " + str(differenceLen))
        #print (periodeDifference)
        #print ("periode difference = " + str(periodeDifference))
        notePeriode.insert(i, periodeDifference)
        #print ("note periode = " + str(notePeriode[i]))
        #print ("--------------------------------------------")
        
    noteFlowId.insert(0, 0)
    flowCounter = 1
    flag = 0
        
    for i in range(1,noteCounter):
        flag = 0
        noteStartTime = noteYear[i] + noteMonth[i] + noteDate[i] + noteHour[i] + noteMinute[i] + noteSecond[i]
        for j in range(0,flowCounter):
            flowStartTime = noteYear[j] + noteMonth[j] + noteDate[j] + noteHour[j] + noteMinute[j] + noteSecond[j]
            if (noteStartTime == flowStartTime and notePeriode[i] == notePeriode[j] and notePortDest[i] == notePortDest[j] and notePayload[i] == notePayload[j]):
                noteFlowId.insert(i, j)
                flag = 1
        
        if (flag == 0):
            noteFlowId.insert(i, flowCounter)
            flowCounter += 1 
    return
    
def Printnote():
    global noteCounter
    #print ("notecounter")
    #print (noteCounter)
    for i in range(0,noteCounter):
        print (i)
        print (noteNumber[i] + ":" + noteYear[i] + ":" + noteMonth[i] + ":" + noteDate[i] + ":" + noteHour[i] + ":" + noteMinute[i] + ":" + noteSecond[i] + ":" + noteNumber[i] + ":" + noteIpSrc[i] + ":" + noteIpDest[i] + ":" + notePortSrc[i] + ":" + notePortDest[i] + ":" + notePayload[i] + ":" + str(notePeriode[i]) + ":" + str(noteFlowId[i]) )
        print (noteCount[i])
        print ("-------------------------------------")
    return

def Printclean():
    cleanLen = len(cleanNumber)
    print (cleanLen)
    for i in range(0,cleanLen):
        print (cleanYear[i] + cleanMonth[i] + cleanDate[i] + cleanHour[i] + cleanMinute[i] + cleanSecond[i] + cleanNumber[i])
    return

def Printflow():
    flowLen = flowCounter

    for i in range(0,flowCounter):
            tempFlowTotalPacket = 0
            print ("-------------------------------")
            for j in range(0,noteCounter):
                if (noteFlowId[j] == i):
                   # print (noteNumber[j] + ":" + noteYear[j] + ":" + noteMonth[j] + ":" + noteDate[j] + ":" + noteHour[j] + ":" + noteMinute[j] + ":" + noteSecond[j] + ":" + noteNumber[j] + ":" + noteIpSrc[j] + ":" + noteIpDest[j] + ":" + notePortSrc[j] + ":" + notePortDest[j] + ":" + notePayload[j] + ":" + str(notePeriode[j]) + ":" + str(noteFlowId[j]))
                   # print (noteCount[j])
                    tempFlowTotalPacket = tempFlowTotalPacket + noteCount[j]
                    
            flowTotalPacket.insert(i, tempFlowTotalPacket)
            #print("total packet : " + str(flowTotalPacket[i]))
            #print ("--------------------------------")
    return

def Participationcalculation():
    cleanLen = len(cleanNumber)
    try:
        now = datetime.date.today()
        logDate =  logPath + str(now) + ".log"
        logfile = open(logDate, "a")
        try:
            logfile.write(cleanYear[0] + "-" + cleanMonth[0] + "-" + cleanDate[0] + "-" + cleanHour[0] + "-" + cleanMinute[0] + "-" + cleanSecond[0] + "\n" )
            logfile.write("~~~~~~~~~~~~~~~~~~~\n")
        finally:
            logfile.close()
    except IOError:
        pass
    
    
    for i in range(0,flowCounter):
        #flowSum = flowTotalPacket[i]
        #print ("masuk")
        #print (flowTotalPacket[i])
        #print (cleanLen)
        tempFlowPercentage = (flowTotalPacket[i] / cleanLen) * 100
        flowPercentage.insert(i, tempFlowPercentage)
        
    for i in range(0,flowCounter):
            
            try:
                now = datetime.date.today()
                logDate =  logPath + str(now) + ".log"
                print (logDate)
                logfile = open(logDate, "a")
                try:
                    #logfile.write("-------------------------------\n")
                    for j in range(0,noteCounter):
                        if (noteFlowId[j] == i):
                            logfile.write(noteNumber[j] + ":" + noteYear[j] + ":" + noteMonth[j] + ":" + noteDate[j] + ":" + noteHour[j] + ":" + noteMinute[j] + ":" + noteSecond[j] + ":" + noteNumber[j] + ":" + noteIpSrc[j] + ":" + noteIpDest[j] + ":" + notePortSrc[j] + ":" + notePortDest[j] + ":" + notePayload[j] + ":" + str(notePeriode[j]) + ":" + str(noteFlowId[j]) + "\n")
            
                    logfile.write("total packet : " + str(flowTotalPacket[i]) + "\n")
                    logfile.write("packet percentage: " + str(flowPercentage[i]) + "\n")
                    if (flowPercentage[i] > int(sensitivity)):
                      logfile.write("--LDDOS packet flow-- \n")
                      logfile.write("--------------------------------\n")
                    else:
                        logfile.write("--normal packet flow--\n")
                        logfile.write("--------------------------------\n")
                finally:
                    logfile.close()
            except IOError:
                pass
                    
    try:
        now = datetime.date.today()
        logDate =  logPath + str(now) + ".log"
        logfile = open(logDate, "a")
        try:
            logfile.write("\n\n")
        finally:
            logfile.close()
    except IOError:
        pass
                    
    return

def Deletefile(fileLocation):
    try:
        os.remove(fileLocation)
        print("masuk")
    except OSError, e:
        print ("Error: %s." % (e.strerror))
    return

Initialization()
Filecheck()
for i in range(0,len(listFile)):
    fileLocation = listFile[i]
    print (datetime.datetime.now())
    print ("step 1")
    Processdata(fileLocation)
    print ("step 2")
    waktu()
    print ("step 3")
    Cleandata()
    print ("step 4")
    #Printclean()
    Selectdata()
    print ("step 5")
    Detectflow()
    #Printnote()
    print ("step 6")
    Printflow()
    print ("step 7")
    Participationcalculation()
    print ("step 8")
    Cleanvariable()
    print ("step 9")
    Deletefile(fileLocation)
    print (datetime.datetime.now())
