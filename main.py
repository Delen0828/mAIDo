import os.path
from msilib.schema import tables
import PyQt5
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout import Ui_Form
from edit import EditUi
from Setting import SettingUi
from listui import  listUi
import sys
# import functools
import numpy as np
from datetime import date
import pandas as pd
from qt_material import apply_stylesheet
from encrypt import *
from schedule import *
from tray import TrayIcon
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
from system_hotkey import SystemHotkey
from PyQt5.QtCore import QObject,pyqtSignal
from listwindowAdd import listwindowAddUi
from style import addstyle
#=============================================  css_content  ==========================================
addstyle2='''
QPushButton {
	text-transform: none;
}
QHeaderView::section {
	text-transform: none;
}

QListView::item {
  
  color: #000000;
  padding: 3px;
  min-height: 5px;
  
}
QListView{
  background-color:#ffffff;
}
'''
#=============================================  css_content  ==========================================
key=b'\xc2\xb5a\x87\xb4\x90\xb9\xa7\xb5\x9a\xfc\xa1\x89&\xfa\xbd\xdc\x15\x16\x87\x97\xd8\xfc\x8e\xef\xd5\xd2\x98\xc0yQ7'
iv=b'\xfd\xa2\x1d8\xe9\xc3z3\x1fs\x91$\xc0\xb1\x9a\xc4'
path=os.path.join(os.getcwd(),'data','task.csv')
pathtxt=os.path.join(os.getcwd(),'data','task.txt')
PriorityDict = {0: 'Low', 1: 'Avg', 2: 'High'}


class MainWindow(QWidget, Ui_Form,QObject):
	sig_keyhot = pyqtSignal(str)

	def __init__(self):
		super().__init__()
		##setting
		self.weekDayformat = 0
		self.rankPri = 0
		self.scheduleTimeBegin = 8.0
		self.scheduleTimeEnd = 17.0
		##
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
		self.listwindow=None
		self.windowlist=[]
		self.Tlist=[]
		self.listshow()
		self.tray = TrayIcon(self)
		#self.windowlist.append(self)
		#QShortcut(QKeySequence(self.tr("Insert")), self, self.hidelistwindow)
		self.sig_keyhot.connect(self.MKey_pressEvent)
		self.hk_start = SystemHotkey()
		self.hk_start.register(('control','1'), callback=lambda x: self.send_key_event("hide"))

	def MKey_pressEvent(self, i_str):
		self.hidelistwindow()
	def send_key_event(self, i_str):
		self.sig_keyhot.emit(i_str)
	def hidelistwindow(self):
		if self.listwindow.isVisible()==0:
			self.listwindow.show()
		else:
			self.listwindow.hide()
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
			item = {'√': False, 'Task': str(self.textEdit.toPlainText())+'\t', 'Deadline': self.comboBox_year.currentText()[2:4]+"/"+self.comboBox_month.currentText()+"/"+self.comboBox_day.currentText()+" "+self.comboBox_hour.currentText(),
				'Priority': self.comboBox.currentIndex(),'Workload':int(self.WorkLoadCombo.currentText()[0])}
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
			#self.Updatelistwindow()
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
		self.Updatelistwindow()
		#self.saveTaskList()

	def Edit(self):
		self.setEnabled(False)
		self.setFocusPolicy(Qt.NoFocus)
		record=self.Tasklist.iloc[[self.tableWidget.selectedItems()[0].row()]]
		#print(ind)
		#print(record)
		self.child = EditLogic(self,record)
		self.child.show()
		#self.windowlist.append(self.child)

	def closeEvent(self,event):
		popout=QMessageBox.question(self,'最小化','是否最小化', QMessageBox.Yes|QMessageBox.No,QMessageBox.No)
		if popout==QMessageBox.No:
			if self.child!=None:
				self.child.close()
			self.saveTaskList()
		else:
			event.ignore()
			self.hide()
			self.tray.show()


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
		# startTime is the starting time of a day
		# maxWorkLoad is what amount of time user work everyday
		# maxWorklaod+starTime should not exceed 23
		if not self.Tasklist.empty:
			self.maxWorkLoad=self.scheduleTimeEnd-self.scheduleTimeBegin
			tempTaskList=self.Tasklist.copy()
			# print(tempTaskList)
			self.hours=range(int(2*self.scheduleTimeBegin),int(2*self.scheduleTimeEnd))
			self.schedule=schedule(filterTask(tempTaskList,self.maxWorkLoad,self.rankPri),len(self.hours))
			self.scheduleTable=pd.DataFrame(index=self.hours,data=self.schedule,columns=['Task'])
			self.scheduleTable=pd.DataFrame(self.scheduleTable.values.T,index=['Task'],columns=self.hours)
			self.UpdateSchedule()
		# print(self.scheduleTable)


	def UpdateSchedule(self):
		self.model = QStandardItemModel(1, len(self.hours))
		labellist=[]
		for i in self.hours:
			if i%2==0:
				labellist.append(str(int(i/2))+':00')
			else:
				labellist.append(str(int((i-1)/2))+':30')
		self.model.setHorizontalHeaderLabels(labellist)
		# self.scheduleTableView.horizontalHeader().setStyleSheet("QHeaderView::section{font:13pt \"Calibri\"}"
		# print('test',self.scheduleTable[8])
		for num in range(len(self.hours)):
			self.model.setItem(0, num, QStandardItem(str(self.scheduleTable[self.hours[num]]['Task'])))
		self.scheduleTableView.setModel(self.model)

	def setting(self):
		self.setEnabled(False)
		self.setFocusPolicy(Qt.NoFocus)
		self.child = SettingLogic(self)
		self.child.show()

	def listshow(self):
		if self.listwindow==None:
			self.listwindow=listWindow(self)
		else:
			if self.listwindow.isVisible()==1:
				self.listwindow.close()
			else:
				self.listwindow.show()
	def Updatelistwindow(self):
		curenttask=np.array(self.Tasklist['Task'])
		self.Tlist=[]
		for item in curenttask:
			item=item.replace('\t','')
			self.Tlist.append(item)
		self.listwindow.updatelist()
		print (self.Tlist)

#==================================================================================================
#edit 窗口
class EditLogic(QWidget,EditUi):
	def __init__(self,parent,record):
		super().__init__()
		name=record['Task'].tolist()[0]
		dtime=str(record['Deadline'].tolist()[0])
		workload=str(record['Workload'].tolist()[0])
		pri=PriorityDict[record['Priority'].tolist()[0]]
		self.setWindowTitle("Edit a task")
		self.setWindowIcon(QIcon('icon.ico'))
		self.setupUi(self)
		self.setFixedSize(self.width(), self.height())
		self.parentWidget=parent
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		self.ConfirmEditButton.clicked.connect(self.edit)
		self.Pricombo.setCurrentText(str(pri))
		self.Workloadcombo.setCurrentText(str(workload))
		self.textEdit.setText(name)
		self.textEdit.setTabChangesFocus(True)
		dt=dtime.split(' ')[0]
		time=dtime.split(' ')[1]
		#print(dtime)
		#print(dt)
		self.Yearcombo.setCurrentText('20'+dt.split('/')[0])
		self.Monthcombo.setCurrentText(dt.split('/')[1])
		self.Daycombo.setCurrentText(dt.split('/')[2])
		self.Hourcombo.setCurrentText(time)
	def messageDialog(self, type):
		if type == 'invalidDate':
			msg_box = QMessageBox(QMessageBox.Critical, 'Date input', 'The input date is not valid!')
			msg_box.setWindowFlags(Qt.WindowStaysOnTopHint)
		msg_box.exec_()
	def edit(self):
		item = {'√': False, 'Task': str(self.textEdit.toPlainText()), 'Deadline': self.Yearcombo.currentText()[2:4]+"/"+self.Monthcombo.currentText()+"/"+self.Daycombo.currentText()+" "+self.Hourcombo.currentText(),
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
#==================================================================================================
#setting 窗口
class SettingLogic(QWidget,SettingUi):
	def __init__(self,parent):
		super().__init__()
		self.setWindowTitle("Setting")
		self.setWindowIcon(QIcon('icon.ico'))
		self.setupUi(self)
		self.setFixedSize(self.width(), self.height())
		self.parentWidget = parent
		self.setWindowFlags(Qt.WindowStaysOnTopHint)
		if int(self.parentWidget.scheduleTimeBegin*2) %2==0:
			self.schedule1.setCurrentText(str(int(self.parentWidget.scheduleTimeBegin)).zfill(2)+':00')
		else:
			self.schedule1.setCurrentText(str(int(self.parentWidget.scheduleTimeBegin-0.5)).zfill(2) + ':30')
		if int(self.parentWidget.scheduleTimeEnd*2) % 2 == 0:
			self.schedule2.setCurrentText(str(int(self.parentWidget.scheduleTimeEnd)).zfill(2) + ':00')
		else:
			self.schedule2.setCurrentText(str(int(self.parentWidget.scheduleTimeEnd - 0.5)).zfill(2) + ':30')
		if self.parentWidget.weekDayformat==0:
			self.mondayfirst.setChecked(True)
		else:
			self.sundayfirst.setChecked(True)
		if self.parentWidget.rankPri==0:
			self.Rank1.setChecked(True)
		else:
			self.Rank1_2.setChecked(True)
	def SaveSetting(self):
		t1=int(self.schedule1.currentText()[0:2])
		t2 = int(self.schedule2.currentText()[0:2])
		if self.schedule1.currentText()[3]=='0':
			self.parentWidget.scheduleTimeBegin=t1
		else:
			self.parentWidget.scheduleTimeBegin = t1+0.5
		if self.schedule2.currentText()[3] == '0':
			self.parentWidget.scheduleTimeEnd = t2
		else:
			self.parentWidget.scheduleTimeEnd = t2 + 0.5

		#print(self.parentWidget.scheduleTimeBegin)
		#print(self.parentWidget.scheduleTimeEnd)
		if self.group1.checkedButton() == self.mondayfirst:
			self.parentWidget.calendarWidget.setFirstDayOfWeek(Qt.Monday)
			self.parentWidget.weekDayformat=0
		elif self.group1.checkedButton() == self.sundayfirst:
			self.parentWidget.calendarWidget.setFirstDayOfWeek(Qt.Sunday)
			self.parentWidget.weekDayformat = 1
		if self.group2.checkedButton() == self.Rank1:
			self.parentWidget.rankPri=0
		elif self.group2.checkedButton() == self.Rank1_2:
			self.parentWidget.rankPri = 1

		self.close()
	def closeEvent(self,event):
		self.parentWidget.setFocusPolicy(Qt.StrongFocus)
		self.parentWidget.setEnabled(True)
#==================================================================================================
#list 窗口

class listWindow(QWidget,listUi):
	def __init__(self, parent):
		super().__init__()
		self.setupUi(self)
		self.setWindowFlags(Qt.WindowCloseButtonHint|Qt.WindowStaysOnTopHint|Qt.Tool)

		self.parentWidget=parent
		self.listWidget.setDragDropMode(QListWidget.InternalMove)
		#self.setStyleSheet("background-color: none ")
		##右键菜单事件
		self.listWidget.setContextMenuPolicy(Qt.CustomContextMenu)
		self.listWidget.customContextMenuRequested.connect(self.custom_right_menu)
		#self.listWidget.addItem("Item 3")
		#self.listWidget.addItem("Item 4")
		self.move(1550,0)
	def custom_right_menu(self,pos):
		#print("呼出菜单")
		self.menu = QMenu()
		self.opt1 = self.menu.addAction('remove')
		self.opt2 = self.menu.addMenu('color')
		self.opt3=self.opt2.addAction('red')
		self.opt4=self.opt2.addAction('yellow')
		self.opt5=self.opt2.addAction('green')
		if len(self.listWidget.selectedItems())==0:
			self.menu.actions()[0].setEnabled(False)
			self.menu.actions()[1].setEnabled(False)
		self.opt1.triggered.connect(self.remove)
		self.menu.popup(QCursor.pos())
		self.opt3.triggered.connect(lambda :self.setbkg('red'))
		self.opt4.triggered.connect(lambda: self.setbkg('yellow'))
		self.opt5.triggered.connect(lambda: self.setbkg('green'))
	def remove(self):
		#print('remove')
		selected_row = self.listWidget.currentRow()
		item = self.listWidget.takeItem(selected_row)
		del item
	def setbkg(self,str):
		color=''
		if str=='red':
			#print('设置成red')
			color=QColor('red')
		elif str=='yellow':
			color = QColor('yellow')
		elif str=='green':
			color=QColor('greenyellow')
		selected_row = self.listWidget.currentRow()
		item = self.listWidget.item(selected_row)
		item.setBackground(color)
		#print(item)
	def updatelist(self):
		self.listWidget.clear()
		self.listWidget.addItems(self.parentWidget.Tlist)
	def listwindowadd(self):
		self.listaddwindow=listAdd(self)
		self.listaddwindow.show()
	def mousePressEvent(self,event):
		#print('点击')
		y=event.y()
		#print(event.pos())
		if y<self.listWidget.y():
			#print('取消选择')
			self.listWidget.clearSelection()


#==================================================================================================
#listAdd 窗口
class listAdd(QWidget,listwindowAddUi):
	def __init__(self, parent):
		super().__init__()
		self.setupUi(self)
		self.setWindowFlags( Qt.WindowStaysOnTopHint| Qt.Tool)
		self.parentWidget = parent
	def Add(self):
		text=self.lineEdit.text()
		self.parentWidget.listWidget.addItem(text)
		self.close()
if __name__ == '__main__':
	QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	QCoreApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
	app = QApplication(sys.argv)
	#stylesheet = app.styleSheet()
	apply_stylesheet(app, theme='dark_teal.xml')
	stylesheet=app.styleSheet()
	#print(stylesheet2)
	app.setStyleSheet(addstyle+addstyle2)

	window = MainWindow()
	window.show()
	sys.exit(app.exec_())

