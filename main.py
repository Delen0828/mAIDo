from msilib.schema import tables
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout import Ui_Form
import sys
import functools
import pandas as pd
PriorityDict={0:'None',1:'1',2:'2'}


class Window(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("mAIDo-Demo")
		#self.resize(1,1)
		self.setupUi(self)
		self.TaskTable()

	def TaskTable(self):
			# 数据源 模型
			self.Tasklist = pd.DataFrame(columns=['Tick', 'Task Name', 'Deadline', 'Priority'])
			self.TaskNum=0
			# self.model.setVerticalHeaderLabels(['1', '3', '4'])
			# 关联QTableView控件和Model
			#self.tableView.setModel(self.model)
			# 添加数据
			self.tableWidget.setRowCount(0)
			self.tableWidget.setColumnCount(4)
			self.tableWidget.setHorizontalHeaderLabels(['Tick', 'Task Name', 'Deadline', 'Priority'])

	def sortTaskList(self):
		# Dict={True:1,False:0}
		self.Tasklist.sort_values(by='Tick',ascending=True,inplace=True)
		print(self.Tasklist)
		# undone_list= for item in self.Tasklist
		# print(self.Tasklist[0]==False)
	def UpdateTable(self):
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(self.TaskNum)

		for row in range(self.TaskNum):
			# print(list(self.Tasklist.loc[0]))
			for column in range(4):
				if column==0:
					checkbox= QCheckBox()
					checkbox.setStyleSheet('QComboBox{margin:3px};')
					checkbox.clicked.connect(self.updateCheck) #检测check点击，更新list
					checkbox.setChecked(self.Tasklist.iloc[row][column])
					self.tableWidget.setCellWidget(row, 0, checkbox)
				elif column==3:
					self.tableWidget.setItem(row, column, QTableWidgetItem(PriorityDict[self.Tasklist.iloc[row][column]]))
				else:
					self.tableWidget.setItem(row,column,QTableWidgetItem(self.Tasklist.iloc[row][column]))
	def updateCheck(self):
		for i in range(self.TaskNum):
			checkItem=self.tableWidget.cellWidget(i,0)
			self.Tasklist.iloc[i][0] = checkItem.isChecked()
		self.sortTaskList()
		self.UpdateTable()

	def add(self):
		item=[False,self.textEdit.toPlainText(),self.TaskDue.text(),self.comboBox.currentIndex()]
		self.Tasklist.loc[len(self.Tasklist)]=item
		# print(self.Tasklist.iloc[0][0])
		self.TaskNum+=1
		self.tableWidget.setRowCount(self.TaskNum)
		self.sortTaskList()
		self.UpdateTable()


	def Delete(self):
		# if len(self.tableWidget.selectedItems())!=0:
		# 	for item in self.tableWidget.selectedItems():
		# 		row=item.row()
		# 		self.Tasklist[row]=[None,None,None,None]
		# 	count=self.Tasklist.count((None,None,None,None))
		# 	self.TaskNum-=count
		# 	Newlist=[]
		# 	for i in range(len(self.Tasklist)):
		# 		if self.Tasklist[i]!=(None,None,None,None): Newlist.append(self.Tasklist[i])
		# 	self.Tasklist=Newlist
		self.sortTaskList()
		self.UpdateTable()

if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())