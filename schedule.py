from asyncio import Task
from numpy import empty
import pandas as pd
Tasklist=pd.read_csv(r'data/task.csv')
# print(Tasklist['Deadline'].str.split(' ')[0][0])
def isToday(Tasklist):
	flagList=[]
	for item in Tasklist:
		flagList.append(item.split(' ')[0]=='22/07/02')
	return flagList
def getHour(time):
	return time.split(' ')[1].split(':')[0]

def helper(scList,sc,item,Namelist,DueDict,count=0):
	if count >=9:
		# if sc not in scList:
		scList.append(sc.copy()) ##bug:duplicate problem
		return sc
	else:
		if count==0:
			count+=1
			for name in Namelist:
				helper(scList,sc.copy(),name,Namelist,DueDict,count)
		elif count+7>=DueDict[item]: ##bug?
			return sc
		else:
			sc.append(item)
			count+=1
			for name in Namelist:
				helper(scList,sc.copy(),name,Namelist,DueDict,count)

# def getScore(schedule):
## 所有task长度的variance越小越好

Tasklist=Tasklist[isToday(Tasklist['Deadline'])]
Namelist=Tasklist['Task'].to_list()
DueDict={}
for name in Namelist:
	DueDict[name]=int(getHour(Tasklist[Tasklist['Task']==name]['Deadline'].values[0]))
# print(DueDict)
scTime=range(8,18)
scList=[]
sc=[]
helper(scList,sc,Namelist[0],Namelist,DueDict)
print(len(scList))
print(Tasklist)