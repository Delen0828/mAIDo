from msilib.schema import tables
import PyQt5
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout import Ui_Form
import sys
# import functools
# import numpy as np
import pandas as pd
from qt_material import apply_stylesheet

PriorityDict = {0: 'NaN', 1: '1', 2: '2'}


class Window(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("mAIDo-Demo")
		self.setWindowIcon(QIcon('icon.ico'))
		self.setupUi(self)
		self.TaskTable()
		self.datelist=[]#内置日历列表

	def TaskTable(self):
		self.Tasklist = pd.DataFrame(columns=['√', 'Task', 'Deadline', 'Priority'])
		self.TaskNum = 0
		self.tableWidget.setRowCount(0)
		self.tableWidget.setColumnCount(4)
		self.tableWidget.setHorizontalHeaderLabels(['√', 'Task', 'Deadline', 'Priority'])
		self.tableWidget.horizontalHeader().setStyleSheet("QHeaderView::section{font:10pt \"Calibri\"}")

	def sortTaskList(self):
		self.Tasklist.sort_values(by=['√', 'Priority', 'Deadline'], ascending=[True, False, True], inplace=True)

	def UpdateTable(self):
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(self.TaskNum)

		for row in range(self.TaskNum):
			for column in range(4):
				if column == 0:
					checkbox = QCheckBox()
					checkbox.setStyleSheet('QComboBox{margin:3px};')
					checkbox.clicked.connect(self.updateCheck)  # update the click signal to tasklist
					checkbox.setChecked(self.Tasklist.iloc[row][column])
					self.tableWidget.setCellWidget(row, 0, checkbox)
				elif column == 3:
					self.tableWidget.setItem(row, column,
											 QTableWidgetItem(PriorityDict[self.Tasklist.iloc[row][column]]))
				else:
					self.tableWidget.setItem(row, column, QTableWidgetItem(self.Tasklist.iloc[row][column]))

	def updateCheck(self):
		for i in range(self.TaskNum):
			checkItem = self.tableWidget.cellWidget(i, 0)
			self.Tasklist.iat[i, 0] = checkItem.isChecked()
		self.sortTaskList()
		self.UpdateTable()

	def highLight(self,dateItem):
		'''更改dateitem背景 ，将dateitem加入内置日期列表'''
		self.datelist.append(dateItem)
		dt = PyQt5.QtCore.QDate.fromString('20' + dateItem.split(' ')[0], "yyyy/MM/d")
			# print(dt.toString())
		cell_format = self.calendarWidget.dateTextFormat(dt)
		cell_format.setBackground(PyQt5.QtGui.QColor("grey"))
		self.calendarWidget.setDateTextFormat(dt, cell_format)


	def deHighLight(self,date_,deldate_):
		'''date_:内置日期列表
		   deldate_:删除选择日期后的日期列表
		'''
		dellist=list(set(date_)-set(deldate_)) #获取calendarview更改的item
		for date in dellist:
			dt = PyQt5.QtCore.QDate.fromString('20'+date.split(' ')[0], "yyyy/MM/d")
			cell_format = PyQt5.QtGui.QTextCharFormat()
			cell_format.setBackground(QBrush(QColor(0,0,0,1)))#透明背景设置
			self.calendarWidget.setDateTextFormat(dt, cell_format)
		self.datelist=deldate_#更新内置日期列表

	def add(self):
		item = {'√': False, 'Task': self.textEdit.toPlainText(), 'Deadline': self.TaskDue.text(),
				'Priority': self.comboBox.currentIndex()}
		self.Tasklist = self.Tasklist.append(item, ignore_index=True)
		self.TaskNum += 1
		self.tableWidget.setRowCount(self.TaskNum)
		self.sortTaskList()
		self.UpdateTable()
		self.highLight(self.TaskDue.text())


	def Delete(self):
		ind = []
		delDateList=[]
		if len(self.tableWidget.selectedItems()) != 0:
			for item in self.tableWidget.selectedItems():
				i = item.row()
				ind.append(self.Tasklist.iloc[i].name)
			ind = list(set(ind))
			self.Tasklist = self.Tasklist.drop(ind)
			self.TaskNum -= len(ind)
		self.sortTaskList()
		self.UpdateTable()
		delDateList=self.Tasklist['Deadline'].to_list()#获取删除后的日期列表
		self.deHighLight(self.datelist,delDateList)


if __name__ == '__main__':
	QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
	app = QApplication(sys.argv)
	apply_stylesheet(app, theme='dark_teal.xml')
	stylesheet = app.styleSheet()
	with open('custom.css') as file:
		app.setStyleSheet(stylesheet + file.read())
	window = Window()
	window.show()
	sys.exit(app.exec_())
