
from msilib.schema import tables
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from layout import Ui_Form
import sys
# import functools
# import numpy as np
import pandas as pd

PriorityDict = {0: 'NaN', 1: '1', 2: '2'}


class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mAIDo-Demo")
        self.setupUi(self)
        self.TaskTable()

    def TaskTable(self):
        self.Tasklist = pd.DataFrame(columns=['Tick', 'TaskName', 'Deadline', 'Priority'])
        self.TaskNum = 0
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setHorizontalHeaderLabels(['Tick', 'TaskName', 'Deadline', 'Priority'])

    def sortTaskList(self):
        self.Tasklist.sort_values(by=['Tick','Priority','Deadline'],ascending=[True,False,True],inplace=True)

    def UpdateTable(self):
        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(self.TaskNum)

        for row in range(self.TaskNum):
            for column in range(4):
                if column == 0:
                    checkbox = QCheckBox()
                    checkbox.setStyleSheet('QComboBox{margin:3px};')
                    checkbox.clicked.connect(self.updateCheck)	#update the click signal to tasklist 
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
            self.Tasklist.iat[i,0] = checkItem.isChecked()
        self.sortTaskList()
        self.UpdateTable()

    def add(self):
        item = {'Tick':False, 'TaskName':self.textEdit.toPlainText(), 'Deadline':self.TaskDue.text(), 'Priority':self.comboBox.currentIndex()}
        self.Tasklist=self.Tasklist.append( item,ignore_index = True)
        self.TaskNum += 1
        self.tableWidget.setRowCount(self.TaskNum)
        self.sortTaskList()
        self.UpdateTable()

    def Delete(self):
        ind=[]
        if len(self.tableWidget.selectedItems())!=0:
            for item in self.tableWidget.selectedItems():
                i=item.row()
                ind.append(self.Tasklist.iloc[i].name)
            ind=list(set(ind))
            self.Tasklist=self.Tasklist.drop(ind)
            self.TaskNum-=len(ind)
        self.sortTaskList()
        self.UpdateTable()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
