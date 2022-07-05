# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout1.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1089, 599)
        self.TaskNameEdit = QtWidgets.QTextEdit(Form)
        self.TaskNameEdit.setGeometry(QtCore.QRect(700, 30, 291, 41))
        self.TaskNameEdit.setObjectName("TaskNameEdit")
        self.AddButton = QtWidgets.QPushButton(Form)
        self.AddButton.setGeometry(QtCore.QRect(1000, 30, 71, 41))
        self.AddButton.setStyleSheet("font: 10pt \"Calibri\" \"bold\";")
        self.AddButton.setObjectName("AddButton")
        self.MonthCombo = QtWidgets.QComboBox(Form)
        self.MonthCombo.setGeometry(QtCore.QRect(900, 80, 51, 41))
        self.MonthCombo.setStyleSheet("font: 10pt \"Calibri\";")
        self.MonthCombo.setObjectName("MonthCombo")
        self.MonthCombo.addItem("")
        self.MonthCombo.addItem("")
        self.MonthCombo.addItem("")
        self.TasktableView = QtWidgets.QTableView(Form)
        self.TasktableView.setGeometry(QtCore.QRect(14, 261, 531, 331))
        self.TasktableView.setStyleSheet("font: 10pt \"Calibri\";")
        self.TasktableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.TasktableView.setObjectName("TasktableView")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(561, 211, 511, 381))
        self.calendarWidget.setStyleSheet("font: 10pt \"Calibri\" \"bold\";")
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.NoSelection)
        self.calendarWidget.setDateEditEnabled(False)
        self.calendarWidget.setObjectName("calendarWidget")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(160, 30, 171, 71))
        self.label.setStyleSheet("font: 48pt \"Calibri\" \"bold\";")
        self.label.setObjectName("label")
        self.YearCombo = QtWidgets.QComboBox(Form)
        self.YearCombo.setGeometry(QtCore.QRect(750, 80, 81, 41))
        self.YearCombo.setObjectName("YearCombo")
        self.YearLabel = QtWidgets.QLabel(Form)
        self.YearLabel.setGeometry(QtCore.QRect(700, 89, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.YearLabel.setFont(font)
        self.YearLabel.setObjectName("YearLabel")
        self.TaskNameLabel = QtWidgets.QLabel(Form)
        self.TaskNameLabel.setGeometry(QtCore.QRect(580, 30, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.TaskNameLabel.setFont(font)
        self.TaskNameLabel.setObjectName("TaskNameLabel")
        self.DueTimeLabel = QtWidgets.QLabel(Form)
        self.DueTimeLabel.setGeometry(QtCore.QRect(581, 86, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.DueTimeLabel.setFont(font)
        self.DueTimeLabel.setObjectName("DueTimeLabel")
        self.MonthLabel = QtWidgets.QLabel(Form)
        self.MonthLabel.setGeometry(QtCore.QRect(839, 90, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.MonthLabel.setFont(font)
        self.MonthLabel.setObjectName("MonthLabel")
        self.HourLabel = QtWidgets.QLabel(Form)
        self.HourLabel.setGeometry(QtCore.QRect(960, 90, 41, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.HourLabel.setFont(font)
        self.HourLabel.setObjectName("HourLabel")
        self.HourCombo = QtWidgets.QComboBox(Form)
        self.HourCombo.setGeometry(QtCore.QRect(1010, 80, 61, 41))
        self.HourCombo.setObjectName("HourCombo")
        self.PriorityLabel = QtWidgets.QLabel(Form)
        self.PriorityLabel.setGeometry(QtCore.QRect(737, 138, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.PriorityLabel.setFont(font)
        self.PriorityLabel.setObjectName("PriorityLabel")
        self.PriorityCombo = QtWidgets.QComboBox(Form)
        self.PriorityCombo.setGeometry(QtCore.QRect(805, 130, 51, 41))
        self.PriorityCombo.setStyleSheet("font: 10pt \"Calibri\";")
        self.PriorityCombo.setObjectName("PriorityCombo")
        self.PriorityCombo.addItem("")
        self.PriorityCombo.addItem("")
        self.PriorityCombo.addItem("")
        self.WorkLoad = QtWidgets.QLabel(Form)
        self.WorkLoad.setGeometry(QtCore.QRect(885, 140, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.WorkLoad.setFont(font)
        self.WorkLoad.setObjectName("WorkLoad")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(1055, 140, 21, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.SaveTaskButton = QtWidgets.QPushButton(Form)
        self.SaveTaskButton.setGeometry(QtCore.QRect(578, 131, 111, 41))
        self.SaveTaskButton.setObjectName("SaveTaskButton")
        self.scheduleTableView = QtWidgets.QTableView(Form)
        self.scheduleTableView.setGeometry(QtCore.QRect(14, 131, 531, 121))
        self.scheduleTableView.setObjectName("scheduleTableView")
        self.WorkLoadCombo = QtWidgets.QComboBox(Form)
        self.WorkLoadCombo.setGeometry(QtCore.QRect(990, 130, 51, 41))
        self.WorkLoadCombo.setStyleSheet("font: 10pt \"Calibri\";")
        self.WorkLoadCombo.setObjectName("WorkLoadCombo")
        self.WorkLoadCombo.addItem("")
        self.WorkLoadCombo.addItem("")
        self.WorkLoadCombo.addItem("")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.AddButton.setText(_translate("Form", "Add"))
        self.MonthCombo.setItemText(0, _translate("Form", "1"))
        self.MonthCombo.setItemText(1, _translate("Form", "2"))
        self.MonthCombo.setItemText(2, _translate("Form", "None"))
        self.label.setText(_translate("Form", "mAIdo"))
        self.YearLabel.setText(_translate("Form", "Year"))
        self.TaskNameLabel.setText(_translate("Form", "Task Name"))
        self.DueTimeLabel.setText(_translate("Form", "Due Time"))
        self.MonthLabel.setText(_translate("Form", "Month"))
        self.HourLabel.setText(_translate("Form", "Hour"))
        self.PriorityLabel.setText(_translate("Form", "Priority"))
        self.PriorityCombo.setItemText(0, _translate("Form", "1"))
        self.PriorityCombo.setItemText(1, _translate("Form", "2"))
        self.PriorityCombo.setItemText(2, _translate("Form", "None"))
        self.WorkLoad.setText(_translate("Form", "Work Load"))
        self.label_11.setText(_translate("Form", "h"))
        self.SaveTaskButton.setText(_translate("Form", "Save Tasks"))
        self.WorkLoadCombo.setItemText(0, _translate("Form", "1"))
        self.WorkLoadCombo.setItemText(1, _translate("Form", "2"))
        self.WorkLoadCombo.setItemText(2, _translate("Form", "None"))
