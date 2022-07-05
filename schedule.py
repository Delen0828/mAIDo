from asyncio import Task
import numpy as np
import pandas as pd
import time
from datetime import date
Tasklist=pd.read_csv(r'data/test.csv')
maxWorkLoad=8
# print(Tasklist['Deadline'].str.split(' ')[0][0])
def isToday(Tasklist):
	flagList=[]
	for item in Tasklist:
		flagList.append(item.split(' ')[0]=="22/07/05")
	return flagList

def getHour(time):
	return time.split(' ')[1].split(':')[0]

def getTimeDiff(timeString):
	temptime=time.mktime(time.strptime(timeString,'%y/%m/%d %H:%M'))-time.time()
	return(temptime/3600) #transfer to hour

def getScore(Tasklist):
	# print(Tasklist['Deadline'].apply(getTimeDiff(Tasklist['Deadline'])))
	# Tasklist['Score']=Tasklist['Priority']*Tasklist['Workload']*(getTimeDiff(Tasklist['Deadline'].str))
	timeDiffList=[]
	for ddl in Tasklist['Deadline']:
		timeDiffList.append(getTimeDiff(ddl))
	Tasklist['Score']=np.exp(Tasklist['Priority'])*Tasklist['Workload']*(1/pd.Series(timeDiffList))

	
def schedule(Tasklist, maxWorkLoad):
	dueToday=Tasklist[isToday(Tasklist['Deadline'])]
	wkldToday=dueToday["Workload"].sum()
	if wkldToday>=maxWorkLoad:
		return dueToday
	# else:
		# otherWork=Tasklist[(not isToday(Tasklist['Deadline'])) and (Tasklist['Workload'].apply(lambda x:int(x))<(maxWorkLoad-wkldToday))] #should repeat many times
		# print(otherWork)
	print(wkldToday)

Namelist=Tasklist['Task'].to_list()
DueDict={}
for name in Namelist:
	DueDict[name]=int(getHour(Tasklist[Tasklist['Task']==name]['Deadline'].values[0]))
scTime=range(8,18)

getScore(Tasklist)
# print(Tasklist)
schedule(Tasklist,maxWorkLoad)

# def helper(scList,sc,item,Namelist,DueDict,count=0):
# 	if count >=9:
# 		# if sc not in scList:
# 		scList.append(sc.copy()) ##bug:duplicate problem
# 		return sc
# 	else:
# 		if count==0:
# 			count+=1
# 			for name in Namelist:
# 				helper(scList,sc.copy(),name,Namelist,DueDict,count)
# 		elif count+7>=DueDict[item]: ##bug?
# 			return sc
# 		else:
# 			sc.append(item)
# 			count+=1
# 			for name in Namelist:
# 				helper(scList,sc.copy(),name,Namelist,DueDict,count)

# def getTasks(date):