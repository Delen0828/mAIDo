import os.path
from msilib.schema import tables
import PyQt5
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout import Ui_Form
from edit import EditUi
import sys
# import functools
import numpy as np
from datetime import date
import pandas as pd
from qt_material import apply_stylesheet
from encrypt import *
from schedule import *

#=============================================  css_content  ==========================================
addstyle='''
QPushButton {
    text-transform: none;
}
QHeaderView::section {
    text-transform: none;
}
'''
#=============================================  css_content  ==========================================
key=b'\xc2\xb5a\x87\xb4\x90\xb9\xa7\xb5\x9a\xfc\xa1\x89&\xfa\xbd\xdc\x15\x16\x87\x97\xd8\xfc\x8e\xef\xd5\xd2\x98\xc0yQ7'
iv=b'\xfd\xa2\x1d8\xe9\xc3z3\x1fs\x91$\xc0\xb1\x9a\xc4'
path=os.path.join(os.getcwd(),'data','task.csv')
pathtxt=os.path.join(os.getcwd(),'data','task.txt')
PriorityDict = {0: 'Low', 1: 'Avg', 2: 'High'}


class MainWindow(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("mAIDo-Demo")
		self.setWindowIcon(QIcon('icon.ico'))
		self.setupUi(self)
		self.setFixedSize(self.width(), self.height())
		self.TaskTable()
		self.Comboini()
		self.test()
		self.datelist=[]#内置日历列表
		self.calendarini()
		self.child=None
		self.Username=None
		self.Pass=None
		self.otherStoredTasks=None




	def test(self):
		pass
	def Comboini(self):
		date=QDate.currentDate()
		time=QTime.currentTime()
		self.comboBox_year.setCurrentText(str(date.year()))
		self.comboBox_month.setCurrentText(str(date.month()).zfill(2))
		self.comboBox_day.setCurrentText(str(date.day()).zfill(2))
		self.comboBox_hour.setCurrentText(str(time.hour()).zfill(2))
	def TaskTable_Menu(self):
		self.menu = QMenu()
		self.actionA = QAction(u'Remove', self)  # 创建菜单选项对象
		self.menu.addAction(self.actionA)
		self.actionB = QAction(u'Edit', self)  # 创建菜单选项对象
		self.menu.addAction(self.actionB)
		if len(self.tableWidget.selectedItems())==0:
			self.menu.actions()[0].setEnabled(False)
			self.menu.actions()[1].setEnabled(False)
		else:
			ind = list(set(self.returnDelList()))
			if len(ind) >1:
				self.menu.actions()[1].setEnabled(False)
		self.actionA.triggered.connect(self.Delete)
		self.actionB.triggered.connect(self.Edit)
		self.menu.popup(QCursor.pos())

	def calendarini(self):
		self.calendarWidget.setLocale(QLocale(QLocale.English))
		self.calendarWidget.setSelectedDate(QDate.currentDate())
		self.calendarWidget.setFirstDayOfWeek(Qt.Monday)
		cell_format=self.calendarWidget.weekdayTextFormat(Qt.Saturday)
		cell_format.setForeground(PyQt5.QtGui.QColor("white"))
		self.calendarWidget.setWeekdayTextFormat(Qt.Saturday,cell_format)
		self.calendarWidget.setWeekdayTextFormat(Qt.Sunday, cell_format)
		self.calendarWidget.setMinimumDate(QDate.currentDate().addDays(0))
		self.calendarWidget.setMaximumDate(QDate.currentDate().addDays(31))
	def TaskTable(self):
		self.Tasklist = pd.DataFrame(columns=['√', 'Task', 'Deadline', 'Priority','Workload'])
		self.TaskNum = 0
		self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.tableWidget.customContextMenuRequested.connect(self.TaskTable_Menu)
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(5)
		self.tableWidget.setHorizontalHeaderLabels(['√', 'Task', 'Deadline', 'Priority','Workload'])
		self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{font:13pt \"Calibri\"}")

	def sortTaskList(self):
		self.Tasklist.sort_values(by=['√', 'Priority', 'Deadline'], ascending=[True, False, True], inplace=True)

	def UpdateTable(self):
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(self.TaskNum)

		for row in range(self.TaskNum):
			for column in range(5):
				if column == 0:
					checkbox = QCheckBox()
					checkbox.setStyleSheet('QComboBox{margin:3px};')
					checkbox.clicked.connect(self.updateCheck)  # update the click signal to tasklist
					checkbox.setChecked(self.Tasklist.iloc[row][column])
					self.tableWidget.setCellWidget(row, 0, checkbox)
				elif column == 3:
					self.tableWidget.setItem(row, column, QTableWidgetItem(PriorityDict[self.Tasklist.iloc[row][column]]))
				elif column==4:
					self.tableWidget.setItem(row, column, QTableWidgetItem(str(self.Tasklist.iloc[row][column])))
				else:
					self.tableWidget.setItem(row, column, QTableWidgetItem(self.Tasklist.iloc[row][column]))
	def updateCheck(self):
		#print('a')
		tempdatelist=[]
		for i in range(self.TaskNum):
			checkItem = self.tableWidget.cellWidget(i, 0)
			self.Tasklist.iat[i, 0] = checkItem.isChecked()
			if checkItem.isChecked()==False:
				tempdatelist.append(self.Tasklist.iat[i,2].split(' ')[0])
		self.sortTaskList()
		self.UpdateTable()
		if (len(tempdatelist)>len(self.datelist)):
			self.deHighLight(tempdatelist,self.datelist,1)
		elif (len(tempdatelist)<len(self.datelist)):
			self.deHighLight(self.datelist,tempdatelist)

	def highLight(self,dateItem):
		'''更改dateitem背景 ,将dateitem加入内置日期列表'''
		self.datelist.append(dateItem.split(' ')[0])
		dt = PyQt5.QtCore.QDate.fromString('20' + dateItem.split(' ')[0], "yyyy/MM/d")
			# print(dt.toString())
		cell_format = self.calendarWidget.dateTextFormat(dt)
		cell_format.setBackground(PyQt5.QtGui.QColor("grey"))
		self.calendarWidget.setDateTextFormat(dt, cell_format)

	def deHighLight(self,date_,deldate_,add=0):
		'''date_:内置日期列表
		   deldate_:删除选择日期后的日期列表
		'''
		choose=[QBrush(QColor(0,0,0,1)),PyQt5.QtGui.QColor("grey")]
		result=[deldate_,date_]
		dellist = list(set(date_) - set(deldate_))  # 获取calendarview更改的item
		for date in dellist:
			dt = PyQt5.QtCore.QDate.fromString('20'+date.split(' ')[0], "yyyy/MM/d")
			cell_format = PyQt5.QtGui.QTextCharFormat()
			cell_format.setBackground(choose[add])#透明背景设置
			self.calendarWidget.setDateTextFormat(dt, cell_format)
		self.datelist=result[add]#更新内置日期列表

	def messageDialog(self, type):
		if type == 'invalidDate':
			msg_box = QMessageBox(QMessageBox.Critical, 'Date input', 'The input date is not valid!')
		msg_box.exec_()
	def add(self,Item=None):
		if Item==None:
			item = {'√': False, 'Task': str(self.textEdit.toPlainText())+'\t', 'Deadline': self.comboBox_year.currentText()[2:4]+"/"+self.comboBox_month.currentText()+"/"+self.comboBox_day.currentText()+" "+self.comboBox_hour.currentText()+":"+'00',
				'Priority': self.comboBox.currentIndex(),'Workload':int(self.WorkLoadCombo.currentText())}
		else:
			item=Item
			item['Task']=str(item['Task'])
		dt=PyQt5.QtCore.QDate.fromString('20'+item['Deadline'].split(' ')[0],'yyyy/MM/d')
		if dt.isValid():
			self.Tasklist = self.Tasklist.append(item, ignore_index=True)
			self.TaskNum += 1
			self.tableWidget.setRowCount(self.TaskNum)
			self.sortTaskList()
			self.UpdateTable()
			self.highLight(item['Deadline'])
		else:
			self.messageDialog('invalidDate')


	def returnDelList(self):
		ind = []
		for item in self.tableWidget.selectedItems():
			i = item.row()
			ind.append(self.Tasklist.iloc[i].name)
		return ind
	
	def Delete(self):
		ind = []
		if len(self.tableWidget.selectedItems()) != 0:
			ind = list(set(self.returnDelList()))
			self.Tasklist = self.Tasklist.drop(ind)
			self.TaskNum -= len(ind)
		self.sortTaskList()
		self.UpdateTable()
		self.updateCheck()
		#self.saveTaskList()

	def Edit(self):
		self.setEnabled(False)
		self.setFocusPolicy(Qt.NoFocus)
		self.child = EditLogic(self)
		self.child.show()
	
	def closeEvent(self,event):
		if self.child!=None:
			self.child.close()
		self.saveTaskList()

	def saveTaskList(self):
		dict={'Username':str(self.Username),'Password':self.Pass,'√': False, 'Task': ' ', 'Deadline': ' ',
					'Priority': -1,'Workload':0}
		Emptydf=pd.DataFrame([dict])
		self.Tasklist.insert(0,'Password',self.Pass)
		self.Tasklist.insert(0,'Username',str(self.Username))
		df = pd.concat([self.otherStoredTasks,Emptydf,self.Tasklist])
		#print(self.otherStoredTasks)
		df['Task'].fillna('',inplace=True)
		df['Workload'].fillna(2,inplace=True)
		df.to_csv(r'data/task.csv',index=False)
		encrypt(path,key,iv)
	def loadTaskList(self,df):
		loadTasklist=df
		for _,row in loadTasklist.iterrows():
			#print(row.tolist())
			item = {'√': row[2], 'Task': str(row[3]), 'Deadline': row[4],
					'Priority': row[5],'Workload':row[6]}
			self.add(item)
		#print(self.Tasklist)
	def generateSchedule(self):
		# print(self.Tasklist)
		tempTaskList=self.Tasklist.copy()
		getScore(tempTaskList)
		print(tempTaskList)
		self.schedule=schedule(filterTask(tempTaskList,maxWorkLoad=8))
		print(tempTaskList,self.schedule)


#==================================================================================================
#edit 窗口
class EditLogic(QWidget,EditUi):
	def __init__(self,parent):
		super().__init__()
		self.setWindowTitle("Edit a task")
		self.setWindowIcon(QIcon('icon.ico'))
		self.setupUi(self)
		self.setFixedSize(self.width(), self.height())
		self.parentWidget=parent
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.ConfirmEditButton.clicked.connect(self.edit)
		date = QDate.currentDate()
		time = QTime.currentTime()
		self.Yearcombo.setCurrentText(str(date.year()))
		self.Monthcombo.setCurrentText(str(date.month()).zfill(2))
		self.Daycombo.setCurrentText(str(date.day()).zfill(2))
		self.Hourcombo.setCurrentText(str(time.hour()).zfill(2))
	def messageDialog(self, type):
		if type == 'invalidDate':
			msg_box = QMessageBox(QMessageBox.Critical, 'Date input', 'The input date is not valid!')
			msg_box.setWindowFlags(Qt.WindowStaysOnTopHint)
		msg_box.exec_()
	def edit(self):
		item = {'√': False, 'Task': str(self.textEdit.toPlainText()), 'Deadline': self.Yearcombo.currentText()[2:4]+"/"+self.Monthcombo.currentText()+"/"+self.Daycombo.currentText()+" "+self.Hourcombo.currentText()+":"+'00',
				'Priority': self.Pricombo.currentIndex(),'Workload':int(self.Workloadcombo.currentText())}
		dt = PyQt5.QtCore.QDate.fromString('20' + item['Deadline'].split(' ')[0], 'yyyy/MM/d')
		if dt.isValid():
			self.parentWidget.Delete()
			self.parentWidget.add(item)
			self.close()
		else: self.messageDialog('invalidDate')
		#print(self.parentWidget.Tasklist)
		#print(self.parentWidget.datelist)
	def closeEvent(self,event):
		self.parentWidget.setFocusPolicy(Qt.StrongFocus)
		self.parentWidget.setEnabled(True)


if __name__ == '__main__':
	QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	apply_stylesheet(app, theme='dark_teal.xml')
	stylesheet = app.styleSheet()
	#print(stylesheet)

	app.setStyleSheet(stylesheet + addstyle)

	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

