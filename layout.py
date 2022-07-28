# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import os.path

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime
from PyQt5.Qt import  *

class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(1089, 599)
		self.textEdit = QtWidgets.QTextEdit(Form)
		self.textEdit.setGeometry(QtCore.QRect(661, 25, 299, 50))
		self.textEdit.setObjectName("textEdit")
		self.textEdit.setStyleSheet("font: 13pt \"Calibri\";")
		self.AddButton = QtWidgets.QPushButton(Form)
		self.AddButton.setGeometry(QtCore.QRect(980, 30, 81, 41))
		self.AddButton.setObjectName("AddButton")
		self.AddButton.setStyleSheet("font:12pt \"Calibri\";")
		# self.loadButton = QtWidgets.QPushButton(Form)
		# self.loadButton.setGeometry(QtCore.QRect(460, 80, 70, 41))
		# self.loadButton.setStyleSheet("font: 12pt \"Calibri\";")
		# self.loadButton.setObjectName("loadButton")
		self.generateButton = QtWidgets.QPushButton(Form)
		self.generateButton.setGeometry(QtCore.QRect(310, 116, 100, 41))
		self.generateButton.setStyleSheet("font: 12pt \"Calibri\";")
		self.generateButton.setObjectName("generateButton")
		self.saveButton = QtWidgets.QPushButton(Form)
		self.saveButton.setGeometry(QtCore.QRect(432, 116, 111, 41))
		self.saveButton.setStyleSheet("font: 12pt \"Calibri\";")
		self.saveButton.setObjectName("saveButton")
		self.settingButton=QtWidgets.QPushButton(Form)
		self.settingButton.setGeometry(QtCore.QRect(5,5,26,26))
		self.settingButton.setObjectName("settingButton")
		Icon=QIcon(os.path.join(os.getcwd(),'setting.png'))
		self.settingButton.setIcon(Icon)

		self.comboBox_year=QtWidgets.QComboBox(Form)
		self.comboBox_year.setGeometry(QtCore.QRect(661, 80, 81, 41))
		self.comboBox_year.setObjectName("Year")
		self.comboBox_year.addItem("2022")
		self.comboBox_year.addItem("2023")
		self.comboBox_year.addItem("2024")
		self.comboBox_year.addItem("2025")
		self.comboBox_year.addItem("2026")

		self.comboBox_month=QtWidgets.QComboBox(Form)
		self.comboBox_month.setGeometry(QtCore.QRect(750, 80, 51, 41))
		self.comboBox_month.setObjectName("Month")
		self.comboBox_month.addItem("01")
		self.comboBox_month.addItem("02")
		self.comboBox_month.addItem("03")
		self.comboBox_month.addItem("04")
		self.comboBox_month.addItem("05")
		self.comboBox_month.addItem("06")
		self.comboBox_month.addItem("07")
		self.comboBox_month.addItem("08")
		self.comboBox_month.addItem("09")
		self.comboBox_month.addItem("10")
		self.comboBox_month.addItem("11")
		self.comboBox_month.addItem("12")

		self.comboBox_day=QtWidgets.QComboBox(Form)
		self.comboBox_day.setGeometry(QtCore.QRect(810, 80, 61, 41))
		self.comboBox_day.setObjectName("Day")
		for i in range(1,32):
			self.comboBox_day.addItem(str(i).zfill(2))

		self.comboBox_hour=QtWidgets.QComboBox(Form)
		self.comboBox_hour.setGeometry(QtCore.QRect(880, 80, 80, 41))
		self.comboBox_hour.setObjectName("Hour")
		for i in range(0,24):
			self.comboBox_hour.addItem(str(i).zfill(2)+":00")
			self.comboBox_hour.addItem(str(i).zfill(2)+":30")
		self.comboBox = QtWidgets.QComboBox(Form)
		self.comboBox.setGeometry(QtCore.QRect(661, 130, 81, 41))
		self.comboBox.setStyleSheet("font: 13pt \"Calibri\";")
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.tableWidget = QtWidgets.QTableWidget(Form)
		self.tableWidget.setGeometry(QtCore.QRect(14, 261, 531, 331))
		self.tableWidget.setStyleSheet("font: 12pt \"Calibri\";")
		self.tableWidget.setObjectName("tableWidget")
		# self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.calendarWidget = QtWidgets.QCalendarWidget(Form)
		self.calendarWidget.setGeometry(QtCore.QRect(551, 190, 531, 401))
		self.calendarWidget.setStyleSheet("font:bold 13pt \"Calibri\";")
		self.calendarWidget.setObjectName("calendarWidget")
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(160, 20, 220, 71))
		self.label.setStyleSheet("font:bold 56pt \"Calibri\";")
		self.label.setObjectName("label")
		self.schedulelabel = QtWidgets.QLabel(Form)
		self.schedulelabel.setGeometry(QtCore.QRect(14, 116, 220, 41))
		self.schedulelabel.setStyleSheet("font:bold 20pt \"Calibri\";")
		self.schedulelabel.setObjectName("schedulelabel")
		self.scheduleTableView = QtWidgets.QTableView(Form)
		self.scheduleTableView.setGeometry(QtCore.QRect(14, 165, 531, 90))
		self.scheduleTableView.setObjectName("scheduleTableView")
		# self.scheduleTableView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
		#self.scheduleTableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.scheduleTableView.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.scheduleTableView.verticalHeader().hide()
		# self.scheduleTableView.scroll

		self.TaskNameLabel = QtWidgets.QLabel(Form)
		self.TaskNameLabel.setGeometry(QtCore.QRect(557, 33, 101, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.TaskNameLabel.setFont(font)
		self.TaskNameLabel.setObjectName("TaskNameLabel")
		self.DueTimeLabel = QtWidgets.QLabel(Form)
		self.DueTimeLabel.setGeometry(QtCore.QRect(567, 86, 101, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.DueTimeLabel.setFont(font)
		self.DueTimeLabel.setObjectName("DueTimeLabel")
		self.WorkLoad = QtWidgets.QLabel(Form)
		self.WorkLoad.setGeometry(QtCore.QRect(795, 140, 101, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		font.setBold(True)
		self.WorkLoad.setFont(font)
		self.WorkLoad.setObjectName("WorkLoad")
		self.WorkLoadCombo = QtWidgets.QComboBox(Form)
		self.WorkLoadCombo.setGeometry(QtCore.QRect(890, 130, 70, 41))
		self.WorkLoadCombo.setStyleSheet("font: 10pt \"Calibri\";")
		self.WorkLoadCombo.setObjectName("WorkLoadCombo")
		self.WorkLoadCombo.addItem('1h')
		self.WorkLoadCombo.addItem('2h')
		self.WorkLoadCombo.addItem('3h')
		self.WorkLoadCombo.addItem('4h')
		self.WorkLoadCombo.addItem('5h')
		self.WorkLoadCombo.addItem('6h')
		self.PriorityLabel = QtWidgets.QLabel(Form)
		self.PriorityLabel.setGeometry(QtCore.QRect(579, 138, 61, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		font.setBold(True)
		self.PriorityLabel.setFont(font)
		self.PriorityLabel.setObjectName("PriorityLabel")
#=============================================================================================================
		self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
		self.calendarWidget.setVerticalHeaderFormat(0)
		self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.HorizontalHeaderFormat.SingleLetterDayNames)
		#self.calendarWidget.setNavigationBarVisible(0)
		self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SelectionMode.NoSelection)
		self.calendarWidget.setDateEditEnabled(False)
		self.calendarWidget.setAutoFillBackground(False)
		# self.calendarWFidget.ShowToday()
		self.AddButton.clicked.connect(lambda: Form.add())
		self.generateButton.clicked.connect(lambda: Form.generateSchedule())
		#self.loadButton.clicked.connect(lambda: Form.loadTaskList())
		self.settingButton.clicked.connect(lambda: Form.setting())
		self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.scheduleTableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
		self.scheduleTableView.setSelectionMode(0)
		self.retranslateUi(Form)
		QtCore.QMetaObject.connectSlotsByName(Form)

	def retranslateUi(self, Form):
		_translate = QtCore.QCoreApplication.translate
		Form.setWindowTitle(_translate("Form", "mAIDo-demo"))
		self.AddButton.setText(_translate("Form", "Add"))
		self.comboBox.setItemText(1, _translate("Form", "Avg"))
		self.comboBox.setItemText(2, _translate("Form", "High"))
		self.comboBox.setItemText(0, _translate("Form", "Low"))
		self.label.setText(_translate("Form", "mAIDo"))
		self.schedulelabel.setText(_translate("Form", "Schedule Today"))
		self.saveButton.setText(_translate("Form","Save tasks"))
		self.TaskNameLabel.setText(_translate("Form", "Task Name"))
		self.DueTimeLabel.setText(_translate("Form", "Due Time"))
		self.PriorityLabel.setText(_translate("Form", "Priority"))
		self.WorkLoad.setText(_translate("Form", "Workload"))
		self.generateButton.setText(_translate("Form","Generate"))


