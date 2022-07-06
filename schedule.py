from asyncio import Task
import numpy as np
import pandas as pd
import time
from datetime import date
# Tasklist=pd.read_csv(r'data/test.csv')
maxWorkLoad=8
# print(Tasklist['Deadline'].str.split(' ')[0][0])
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

def getScore(Tasklist):
	# print(Tasklist['Deadline'].apply(getTimeDiff(Tasklist['Deadline'])))
	# Tasklist['Score']=Tasklist['Priority']*Tasklist['Workload']*(getTimeDiff(Tasklist['Deadline'].str))
	timeDiffList=[]
	for ddl in Tasklist['Deadline']:
		timeDiffList.append(getTimeDiff(ddl))
	Tasklist['Score']=np.exp(Tasklist['Priority'])*Tasklist['Workload']*(1/pd.Series(timeDiffList))
	
def filterTask(Tasklist, maxWorkLoad):
	dueToday=Tasklist[isToday(Tasklist['Deadline'])]
	wkldToday=dueToday["Workload"].sum()
	outTask=dueToday
	# print(wkldToday)
	if wkldToday<maxWorkLoad:
		timediff=maxWorkLoad-wkldToday
		today=time.strftime('%y/%m/%d',time.localtime())
		datelist=np.array(Tasklist['Deadline'].str.split(' ').to_list())[:,0]
		notTodayList=pd.Series(list(datelist!=[today]*len(datelist)))
		otherWork=Tasklist[Tasklist['Workload']<=timediff * notTodayList].sort_values('Score',ascending=False)
		while timediff>0 and len(otherWork)>0:
			# print(otherWork)
			best,bestIndex=otherWork.iloc[0],otherWork.index.to_list()[0]
			# print(bestIndex)
			outTask=outTask.append(best,ignore_index=True)
			# print(otherWork)
			timediff-=best['Workload']
			otherWork.drop([bestIndex],inplace=True)
			otherWork=otherWork[otherWork['Workload']<timediff]
	return outTask
	
def schedule(Tasklist):
	Tasklist.sort_values(by=['Deadline','Priority'], ascending=[True, True], inplace=True)
	daily=[]
	for _,task in Tasklist.iterrows():
		# print(task)
		daily=daily+[task.Task]*task.Workload
	return daily

# Namelist=Tasklist['Task'].to_list()
# DueDict={}
# for name in Namelist:
# 	DueDict[name]=int(getHour(Tasklist[Tasklist['Task']==name]['Deadline'].values[0]))
# scTime=range(8,18)

# getScore(Tasklist)
# # print(Tasklist)
# mySchedule=schedule(filterTask(Tasklist,maxWorkLoad))
# print(mySchedule)

# self.Tasklist.sort_values(by=['√', 'Priority', 'Deadline'], ascending=[True, False, True], inplace=True)


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