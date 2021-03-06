# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDateTime


class Ui_Form(object):
	def setupUi(self, Form):
		Form.setObjectName("Form")
		Form.resize(1089, 599)
		self.textEdit = QtWidgets.QTextEdit(Form)
		self.textEdit.setGeometry(QtCore.QRect(661, 30, 311, 41))
		self.textEdit.setObjectName("textEdit")
		self.textEdit.setStyleSheet("font: 13pt \"Calibri\";")
		self.AddButton = QtWidgets.QPushButton(Form)
		self.AddButton.setGeometry(QtCore.QRect(1001, 30, 81, 41))
		self.AddButton.setObjectName("AddButton")
		self.AddButton.setStyleSheet("font:12pt \"Calibri\";")
		# self.loadButton = QtWidgets.QPushButton(Form)
		# self.loadButton.setGeometry(QtCore.QRect(460, 80, 70, 41))
		# self.loadButton.setStyleSheet("font: 12pt \"Calibri\";")
		# self.loadButton.setObjectName("loadButton")
		self.generateButton = QtWidgets.QPushButton(Form)
		self.generateButton.setGeometry(QtCore.QRect(310, 216, 100, 41))
		self.generateButton.setStyleSheet("font: 12pt \"Calibri\";")
		self.generateButton.setObjectName("generateButton")
		self.saveButton = QtWidgets.QPushButton(Form)
		self.saveButton.setGeometry(QtCore.QRect(435, 216, 111, 41))
		self.saveButton.setStyleSheet("font: 12pt \"Calibri\";")
		self.saveButton.setObjectName("saveButton")

		#self.TaskDue = QtWidgets.QDateTimeEdit(QDateTime.currentDateTime(), Form)
		#self.TaskDue.setGeometry(QtCore.QRect(550, 140, 221, 41))
		#self.TaskDue.setDisplayFormat('yy/MM/dd hh:mm')
		#self.TaskDue.setObjectName("dateTimeEdit")
		#self.TaskDue.setStyleSheet("font: 13pt \"Calibri\";")

		self.comboBox_year=QtWidgets.QComboBox(Form)
		self.comboBox_year.setGeometry(QtCore.QRect(697, 80, 81, 41))
		self.comboBox_year.setObjectName("Year")
		self.comboBox_year.addItem("2022")
		self.comboBox_year.addItem("2023")
		self.comboBox_year.addItem("2024")
		self.comboBox_year.addItem("2025")
		self.comboBox_year.addItem("2026")

		self.comboBox_month=QtWidgets.QComboBox(Form)
		self.comboBox_month.setGeometry(QtCore.QRect(834, 80, 51, 41))
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
		self.comboBox_day.setGeometry(QtCore.QRect(923, 80, 61, 41))
		self.comboBox_day.setObjectName("Day")
		for i in range(1,32):
			self.comboBox_day.addItem(str(i).zfill(2))

		self.comboBox_hour=QtWidgets.QComboBox(Form)
		self.comboBox_hour.setGeometry(QtCore.QRect(1030, 80, 51, 41))
		self.comboBox_hour.setObjectName("Hour")
		for i in range(0,24):
			self.comboBox_hour.addItem(str(i).zfill(2))
		self.comboBox = QtWidgets.QComboBox(Form)
		self.comboBox.setGeometry(QtCore.QRect(804, 130, 81, 41))
		self.comboBox.setStyleSheet("font: 13pt \"Calibri\";")
		self.comboBox.setObjectName("comboBox")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.comboBox.addItem("")
		self.tableWidget = QtWidgets.QTableWidget(Form)
		self.tableWidget.setGeometry(QtCore.QRect(14, 261, 531, 331))
		self.tableWidget.setStyleSheet("font: 13pt \"Calibri\";")
		self.tableWidget.setObjectName("tableWidget")
		# self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
		self.calendarWidget = QtWidgets.QCalendarWidget(Form)
		self.calendarWidget.setGeometry(QtCore.QRect(551, 190, 531, 401))
		self.calendarWidget.setStyleSheet("font:bold 13pt \"Calibri\";")
		self.calendarWidget.setObjectName("calendarWidget")
		self.label = QtWidgets.QLabel(Form)
		self.label.setGeometry(QtCore.QRect(160, 30, 171, 71))
		self.label.setStyleSheet("font:bold 40pt \"Calibri\";")
		self.label.setObjectName("label")
		self.scheduleTableView = QtWidgets.QTableView(Form)
		self.scheduleTableView.setGeometry(QtCore.QRect(14, 91, 531, 121))
		self.scheduleTableView.setObjectName("scheduleTableView")
		self.YearLabel = QtWidgets.QLabel(Form)
		self.YearLabel.setGeometry(QtCore.QRect(657, 91, 41, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		self.YearLabel.setFont(font)
		self.YearLabel.setObjectName("YearLabel")
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
		self.DueTimeLabel.setGeometry(QtCore.QRect(559, 86, 101, 31))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		font.setBold(True)
		font.setWeight(75)
		self.DueTimeLabel.setFont(font)
		self.DueTimeLabel.setObjectName("DueTimeLabel")
		self.MonthLabel = QtWidgets.QLabel(Form)
		self.MonthLabel.setGeometry(QtCore.QRect(786, 90, 51, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		self.MonthLabel.setFont(font)
		self.MonthLabel.setObjectName("MonthLabel")
		self.DayLabel = QtWidgets.QLabel(Form)
		self.DayLabel.setGeometry(QtCore.QRect(895, 90, 41, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		self.DayLabel.setFont(font)
		self.DayLabel.setObjectName("DayLabel")
		self.WorkLoad = QtWidgets.QLabel(Form)
		self.WorkLoad.setGeometry(QtCore.QRect(894, 140, 101, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		self.WorkLoad.setFont(font)
		self.WorkLoad.setObjectName("WorkLoad")
		self.label_11 = QtWidgets.QLabel(Form)
		self.label_11.setGeometry(QtCore.QRect(1055, 140, 21, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		self.label_11.setFont(font)
		self.label_11.setObjectName("label_11")
		self.WorkLoadCombo = QtWidgets.QComboBox(Form)
		self.WorkLoadCombo.setGeometry(QtCore.QRect(990, 130, 51, 41))
		self.WorkLoadCombo.setStyleSheet("font: 10pt \"Calibri\";")
		self.WorkLoadCombo.setObjectName("WorkLoadCombo")
		self.WorkLoadCombo.addItem('1')
		self.WorkLoadCombo.addItem('2')
		self.WorkLoadCombo.addItem('3')
		self.WorkLoadCombo.addItem('4')
		self.WorkLoadCombo.addItem('5')
		self.WorkLoadCombo.addItem('6')
		self.HourLabel = QtWidgets.QLabel(Form)
		self.HourLabel.setGeometry(QtCore.QRect(991, 90, 41, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
		self.HourLabel.setFont(font)
		self.HourLabel.setObjectName("HourLabel")
		self.PriorityLabel = QtWidgets.QLabel(Form)
		self.PriorityLabel.setGeometry(QtCore.QRect(743, 138, 61, 21))
		font = QtGui.QFont()
		font.setFamily("Arial")
		font.setPointSize(18)
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
		self.saveButton.setText(_translate("Form","Save tasks"))
		self.YearLabel.setText(_translate("Form", "Year"))
		self.TaskNameLabel.setText(_translate("Form", "Task Name"))
		self.DueTimeLabel.setText(_translate("Form", "Due Time"))
		self.MonthLabel.setText(_translate("Form", "Month"))
		self.DayLabel.setText(_translate("Form", "Day"))
		self.PriorityLabel.setText(_translate("Form", "Priority"))
		self.WorkLoad.setText(_translate("Form", "Work Load"))
		self.label_11.setText(_translate("Form", "h"))
		self.HourLabel.setText(_translate("Form", "Hour"))
		self.generateButton.setText(_translate("Form","Generate"))


