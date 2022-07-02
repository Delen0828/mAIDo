import numpy as np
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
import hashlib
from encrypt import *
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
key=b'\xc2\xb5a\x87\xb4\x90\xb9\xa7\xb5\x9a\xfc\xa1\x89&\xfa\xbd\xdc\x15\x16\x87\x97\xd8\xfc\x8e\xef\xd5\xd2\x98\xc0yQ7'
iv=b'\xfd\xa2\x1d8\xe9\xc3z3\x1fs\x91$\xc0\xb1\x9a\xc4'
path=os.path.join(os.getcwd(),'data','task.csv')
pathtxt=os.path.join(os.getcwd(),'data','task.txt')
class LoginWindowLogic(QWidget, Login_Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("mAIDo-Demo-login")
        self.setWindowIcon(QIcon('icon.ico'))
        self.setupUi(self)
        self.LoginButton.clicked.connect(self.login)
        self.Mainwindow = MainWindow()

    def messageDialog(self,type):
        if type=='inform':
            msg_box = QMessageBox(QMessageBox.Information, 'Log in', 'Log in successfully!')
        if type=='error':
            msg_box = QMessageBox(QMessageBox.Critical, 'Log in', 'Wrong Password!')
        if type=='reg':
            msg_box = QMessageBox(QMessageBox.Information, 'Register', 'Register successfully!')
        if type=='EmptyUser':
            msg_box = QMessageBox(QMessageBox.Warning, 'Register', 'The username can not be empty!')
        if type == 'EmptyPass':
            msg_box = QMessageBox(QMessageBox.Warning, 'Register', 'The password can not be empty!')

        msg_box.exec_()


    def load(self,username,passWord,list):
        loadTasklist = list
        otherTasks = loadTasklist[loadTasklist['Username'] != str(username)]
        loadTasklist=loadTasklist[loadTasklist['Username']==str(username)]
        #print(loadTasklist)
        loadTasklist.drop(loadTasklist.index[0],inplace=True)
        if len(loadTasklist)>0:
            loadTasklist['Task']=loadTasklist['Task'].astype(np.str)
            loadTasklist['√']=loadTasklist['√'].astype('bool')
            loadTasklist['Priority']=loadTasklist['Priority'].astype('int')
            self.Mainwindow.loadTaskList(loadTasklist)
        self.Mainwindow.otherStoredTasks=otherTasks.copy()
        self.Mainwindow.Username=username
        self.Mainwindow.Pass=passWord
    def login(self):
        #os.rename(path,pathtxt)
        decrypt(path,key,iv)
        #os.rename(pathtxt,path)
        username=str(self.UserNameTextEdit.toPlainText())
        plainPass=str(self.passWordTextEdit.toPlainText())
        loadTasklist = pd.read_csv(r'data/task.csv')

        userlist=loadTasklist['Username'].astype('str').tolist()
        shal1 = hashlib.sha1()
        data = plainPass
        shal1.update(data.encode('utf-8'))
        shalPass = shal1.hexdigest()
        if username=='':
            self.messageDialog('EmptyUser')
        elif username in userlist:
            loadTasklist['Username'] = loadTasklist['Username'].astype('str')
            loadTasklist['Password'] = loadTasklist['Password'].astype('str')
            loadPass=loadTasklist[loadTasklist['Username']==username]['Password'].unique()
            if shalPass==loadPass :
                self.messageDialog('inform')
                self.load(username,shalPass,loadTasklist)
                self.Mainwindow.show()
                encrypt(path,key,iv)
                self.close()
            else:
                self.messageDialog('error')
        else:
            if plainPass=='':
                self.messageDialog('EmptyPass')
            else:
                newItem={'Username':str(username),'Password':str(shalPass),'√':None,'Task':None,'Deadline':None,'Priority':None}
                loadTasklist=loadTasklist.append(newItem,ignore_index=True)
                loadTasklist.to_csv(r'data/task.csv', index=False)
                self.messageDialog('reg')
                self.load(username, shalPass,loadTasklist)
                self.Mainwindow.show()
                encrypt(path,key,iv)
                self.close()
        encrypt(path, key, iv)

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