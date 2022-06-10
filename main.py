from msilib.schema import tables
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Ui_layout import Ui_Form
import sys
class Window(QWidget, Ui_Form):
	def __init__(self):
		super().__init__()
		self.setWindowTitle("添加到list")
		self.resize(1000, 2000)
		self.setupUi(self)
		self.TaskTable()

	def TaskTable(self):
		self.tableView=QTableView()
		self.model = QStandardItemModel(self.tableView)

		#设置数据层次结构，4行4列
		self.model=QStandardItemModel(4,4)
		self.check_box = QCheckBox(self)
		#设置水平方向四个头标签文本内容
		self.model.setHorizontalHeaderLabels(['状态','姓名','身份证','地址'])

		for row in range(4):
			for column in range(4):
				item_checked = QStandardItem()
				item_checked.setCheckState(Qt.Checked)
				item_checked.setCheckable(True)
				self.model.setItem(column,0, item_checked)
				item=QStandardItem('row %s,column %s'%(row,column))
				#设置每个位置的文本值
				self.model.setItem(row,column,item)

		self.tableView.setModel(self.model)
		#设置布局
		layout=QVBoxLayout()
		layout.addWidget(self.check_box)
		layout.addWidget(self.tableView)
		self.setLayout(layout)

	def add(self):        #
		#print(self.textEdit.toPlainText())
		self.list.append(self.textEdit.toPlainText())
		self.model.setStringList(self.list)
		self.listView.setModel(self.model)
		#print(self.list)

	def DelListItem(self):
		selected = self.listView.selectedIndexes()

		for i in selected:
			#print (i.row())
			del self.list[i.row()]
		self.model.setStringList(self.list)
		self.listView.setModel(self.model)
if __name__ == '__main__':
	app = QApplication(sys.argv)
	window = Window()
	window.show()
	sys.exit(app.exec_())