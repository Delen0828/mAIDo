# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Login_Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(360, 282)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(130, 30, 141, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(30, 110, 81, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 71, 31))
        self.label_3.setObjectName("label_3")
        self.UserNameTextEdit = QtWidgets.QTextEdit(Form)
        self.UserNameTextEdit.setGeometry(QtCore.QRect(110, 110, 191, 31))
        self.UserNameTextEdit.setObjectName("UserNameTextEdit")
        self.passWordTextEdit = QtWidgets.QTextEdit(Form)
        self.passWordTextEdit.setGeometry(QtCore.QRect(110, 170, 191, 31))
        self.passWordTextEdit.setObjectName("passWordTextEdit")
        self.LoginButton = QtWidgets.QPushButton(Form)
        self.LoginButton.setGeometry(QtCore.QRect(130, 220, 101, 31))
        self.LoginButton.setObjectName("LoginButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "mAIdo     "))
        self.label_2.setText(_translate("Form", "UserName"))
        self.label_3.setText(_translate("Form", "Password"))
        self.LoginButton.setText(_translate("Form", "Log in"))
