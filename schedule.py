from asyncio import Task
import numpy as np
import pandas as pd
import time
from datetime import date

def isToday(Tasklist):
	flagList=[]
	for item in Tasklist:
		flagList.append(item.split(' ')[0]==time.strftime('%y/%m/%d',time.localtime()))
	# print(flagList)
	return flagList

def getHour(time):
	return time.split(' ')[1].split(':')[0]

def getTimeDiff(timeString):
	temptime=time.mktime(time.strptime(timeString,'%y/%m/%d %H:%M'))-time.time()
	return(temptime/3600) #transfer to hour
	
def filterTask(tasklist, maxWorkLoad, sortByWorkload):
	# print(Tasklist)
	Tasklist=tasklist.copy()
	dueToday=Tasklist[isToday(Tasklist['Deadline'])]
	wkldToday=dueToday["Workload"].sum()
	outTask=dueToday
	timediff=maxWorkLoad-wkldToday
	if wkldToday<maxWorkLoad:
		today=time.strftime('%y/%m/%d',time.localtime())
		Tasklist['Date']=np.array(Tasklist['Deadline'].str.split(' ').to_list())[:,0]
		# Tasklist['IsToday']= (Tasklist['Date']==[today]*len(Tasklist['Date']))
		# print(sortByWorkload)
		if not sortByWorkload: #high priority first
			otherWork=Tasklist[Tasklist['Workload']<=timediff][Tasklist['Date']>today].sort_values('Priority',ascending=False)
		else:#low workload first
			otherWork=Tasklist[Tasklist['Workload']<=timediff][Tasklist['Date']>today].sort_values('Workload',ascending=False)
		# print(otherWork)
		while timediff>0 and len(otherWork)>0:
			best,bestIndex=otherWork.iloc[0],otherWork.index.to_list()[0]
			outTask=outTask.append(best,ignore_index=True)
			timediff-=best['Workload']
			otherWork.drop([bestIndex],inplace=True)
			otherWork=otherWork[otherWork['Workload']<timediff]
	if wkldToday>maxWorkLoad:
		# print('*****OVERLOAD*****')
		overflow=-timediff
		outTask=outTask.sort_values('Priority',ascending=True)
		while overflow>0 and len(outTask)>0:
			best,bestIndex=outTask.iloc[0],outTask.index.to_list()[0]
			overflow-=best['Workload']
			outTask.drop([bestIndex],inplace=True)
	return outTask
	
def schedule(Tasklist,lenHours):
	# Tasklist.sort_values(by=['Deadline','Priority'], ascending=[True, True], inplace=True)
	daily=[]
	for _,task in Tasklist.iterrows():
		# print(task)
		daily=daily+[task.Task]*int(task.Workload*2)
	if len(daily)<lenHours:
		for _ in range(lenHours-len(daily)):
			daily.append('')
	return daily