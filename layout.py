# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(500, 500)
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(50, 20, 201, 31))
        self.textEdit.setObjectName("textEdit")
        self.AddButton = QtWidgets.QPushButton(Form)
        self.AddButton.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.AddButton.setObjectName("AddButton")
        self.AddButton.clicked.connect(Form.add)
        self.DeleteButton = QtWidgets.QPushButton(Form)
        self.DeleteButton.setGeometry(QtCore.QRect(300, 50, 75, 23))
        self.DeleteButton.setObjectName("DeleteButton")
        self.DeleteButton.clicked.connect(Form.Delete)
        self.TaskDue = QtWidgets.QDateTimeEdit(Form)
        self.TaskDue.setGeometry(QtCore.QRect(50, 60, 194, 22))
        self.TaskDue.setObjectName("dateTimeEdit")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(50, 90, 69, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.tableWidget=QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(50, 130, 420, 350))
        self.tableWidget.setObjectName("tableWidget")
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "mAIDo-demo"))
        self.AddButton.setText(_translate("Form", "Add"))
        self.DeleteButton.setText(_translate("Form", "Remove"))
        self.comboBox.setItemText(1, _translate("Form", "1"))
        self.comboBox.setItemText(2, _translate("Form", "2"))
        self.comboBox.setItemText(0, _translate("Form", "None"))
