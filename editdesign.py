# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editdesign.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(520, 212)
        self.Pricombo = QtWidgets.QComboBox(Form)
        self.Pricombo.setGeometry(QtCore.QRect(430, 89, 81, 41))
        self.Pricombo.setObjectName("Pricombo")
        self.Pricombo.addItem("")
        self.Pricombo.addItem("")
        self.Pricombo.addItem("")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(90, 30, 241, 41))
        self.textEdit.setObjectName("textEdit")
        self.ConfirmEditButton = QtWidgets.QPushButton(Form)
        self.ConfirmEditButton.setGeometry(QtCore.QRect(190, 150, 131, 51))
        self.ConfirmEditButton.setObjectName("ConfirmEditButton")
        self.TaskNameLabel = QtWidgets.QLabel(Form)
        self.TaskNameLabel.setGeometry(QtCore.QRect(10, 40, 111, 21))
        self.TaskNameLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.TaskNameLabel.setObjectName("TaskNameLabel")
        self.WorkloadLabel = QtWidgets.QLabel(Form)
        self.WorkloadLabel.setGeometry(QtCore.QRect(339, 42, 111, 21))
        self.WorkloadLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.WorkloadLabel.setObjectName("WorkloadLabel")
        self.Workloadcombo = QtWidgets.QComboBox(Form)
        self.Workloadcombo.setGeometry(QtCore.QRect(420, 31, 71, 41))
        self.Workloadcombo.setObjectName("Workloadcombo")
        self.TaskNameLabel_3 = QtWidgets.QLabel(Form)
        self.TaskNameLabel_3.setGeometry(QtCore.QRect(500, 40, 16, 21))
        self.TaskNameLabel_3.setTextFormat(QtCore.Qt.MarkdownText)
        self.TaskNameLabel_3.setObjectName("TaskNameLabel_3")
        self.Yearcombo = QtWidgets.QComboBox(Form)
        self.Yearcombo.setGeometry(QtCore.QRect(11, 89, 101, 41))
        self.Yearcombo.setObjectName("Yearcombo")
        self.Slash1 = QtWidgets.QLabel(Form)
        self.Slash1.setGeometry(QtCore.QRect(117, 100, 16, 21))
        self.Slash1.setTextFormat(QtCore.Qt.MarkdownText)
        self.Slash1.setObjectName("Slash1")
        self.Monthcombo = QtWidgets.QComboBox(Form)
        self.Monthcombo.setGeometry(QtCore.QRect(133, 90, 61, 41))
        self.Monthcombo.setObjectName("Monthcombo")
        self.Daycombo = QtWidgets.QComboBox(Form)
        self.Daycombo.setGeometry(QtCore.QRect(218, 90, 61, 41))
        self.Daycombo.setObjectName("Daycombo")
        self.Slash2 = QtWidgets.QLabel(Form)
        self.Slash2.setGeometry(QtCore.QRect(202, 101, 20, 21))
        self.Slash2.setTextFormat(QtCore.Qt.MarkdownText)
        self.Slash2.setObjectName("Slash2")
        self.Hourcombo = QtWidgets.QComboBox(Form)
        self.Hourcombo.setGeometry(QtCore.QRect(326, 90, 61, 41))
        self.Hourcombo.setObjectName("Hourcombo")
        self.TimeLabel = QtWidgets.QLabel(Form)
        self.TimeLabel.setGeometry(QtCore.QRect(283, 100, 41, 21))
        self.TimeLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.TimeLabel.setObjectName("TimeLabel")
        self.MinuLabel = QtWidgets.QLabel(Form)
        self.MinuLabel.setGeometry(QtCore.QRect(387, 101, 41, 21))
        self.MinuLabel.setTextFormat(QtCore.Qt.MarkdownText)
        self.MinuLabel.setObjectName("MinuLabel")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Pricombo.setItemText(0, _translate("Form", "Low"))
        self.Pricombo.setItemText(1, _translate("Form", "Avg"))
        self.Pricombo.setItemText(2, _translate("Form", "High"))
        self.ConfirmEditButton.setText(_translate("Form", "Confirm"))
        self.TaskNameLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Task Name</span></p></body></html>"))
        self.WorkloadLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">Work Load</span></p></body></html>"))
        self.TaskNameLabel_3.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:12pt;\">h</span></p></body></html>"))
        self.Slash1.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">/</span></p></body></html>"))
        self.Slash2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">/</span></p></body></html>"))
        self.TimeLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">Time</span></p></body></html>"))
        self.MinuLabel.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:14pt;\">:00</span></p></body></html>"))