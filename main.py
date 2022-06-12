from msilib.schema import tables
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout import Ui_Form
import sys
import functools
PriorityDict={0:'None',1:'1',2:'2'}


class Window(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("添加到list")
		#self.resize(1,1)
		self.setupUi(self)
		self.TaskTable()

	def TaskTable(self):
			# 数据源 模型
			self.Tasklist = []
			self.TaskNum=0
			# self.model.setVerticalHeaderLabels(['1', '3', '4'])
			# 关联QTableView控件和Model
			#self.tableView.setModel(self.model)

			# 添加数据
			self.tableWidget.setRowCount(0)
			self.tableWidget.setColumnCount(4)
			self.tableWidget.setHorizontalHeaderLabels(['Checked', 'Task', 'Time','Priority'])

	def sortTaskList(self):
		Dict={True:1,False:0}
		def Mycmp(a,b):
			a=Dict[a[0]]
			b=Dict[b[0]]
			return a-b
		self.Tasklist.sort(key=functools.cmp_to_key(Mycmp),reverse=False)
	def UpdateTable(self):
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(self.TaskNum)
		for row in range(self.TaskNum):
			for column in range(4):
				if column==0:
					checkbox= QCheckBox()
					checkbox.setStyleSheet('QComboBox{margin:3px};')
					checkbox.clicked.connect(self.updateCheck)#检测check点击，更新list
					checkbox.setChecked(self.Tasklist[row][column])
					self.tableWidget.setCellWidget(row, 0, checkbox)
				elif column==3:
					self.tableWidget.setItem(row, column, QTableWidgetItem(PriorityDict[self.Tasklist[row][column]]))
				else:
					self.tableWidget.setItem(row,column,QTableWidgetItem(self.Tasklist[row][column]))
	def updateCheck(self):
		for i in range(self.TaskNum):
			checkItem=self.tableWidget.cellWidget(i,0)
			temp = list(self.Tasklist[i])
			temp[0] =checkItem.isChecked()
			self.Tasklist[i] = tuple(temp)
		self.sortTaskList()
		self.UpdateTable()
	def add(self):        #
		#
		item=(False,self.textEdit.toPlainText(),self.TaskDue.text(),self.comboBox.currentIndex())
		self.Tasklist.append(item)
		self.TaskNum+=1
		self.tableWidget.setRowCount(self.TaskNum)
		self.sortTaskList()
		self.UpdateTable()


	def Delete(self):

		if len(self.tableWidget.selectedItems())!=0:
			for item in self.tableWidget.selectedItems():
				row=item.row()
				self.Tasklist[row]=(None,None,None,None)
			count=self.Tasklist.count((None,None,None,None))
			self.TaskNum-=count
			Newlist=[]
			for i in range(len(self.Tasklist)):
				if self.Tasklist[i]!=(None,None,None,None): Newlist.append(self.Tasklist[i])
			self.Tasklist=Newlist
		self.sortTaskList()
		self.UpdateTable()
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())