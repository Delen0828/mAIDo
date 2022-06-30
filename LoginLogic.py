import os.path
from msilib.schema import tables
import PyQt5
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from login import Login_Ui_Form
from main import MainWindow
import sys
# import functools
# import numpy as np
import pandas as pd
from qt_material import apply_stylesheet

#=============================================  css_content  ==========================================
addstyle='''QPushButton {
    text-transform: none;
}
QHeaderView::section {
    text-transform: none;
}'''
#=============================================  css_content  ==========================================

class LoginWindowLogic(QWidget, Login_Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mAIDo-Demo-login")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.login)
        self.Mainwindow = MainWindow()

    def login(self):
        self.Mainwindow.show()
        self.close()


if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_teal.xml')
    stylesheet = app.styleSheet()
    #print(stylesheet)

    app.setStyleSheet(stylesheet + addstyle)

    window = LoginWindowLogic()
    window.show()
    sys.exit(app.exec_())