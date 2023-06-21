from PyQt5 import QtWidgets, QtCore, QtGui
import os
from PyQt5.Qt import *
from sqlalchemy import create_engine
from sqlalchemy import text
from sqlalchemy.types import DATE,CHAR,VARCHAR,TEXT,DATETIME
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
import pandas as pd
import pymysql
path = os.path.abspath(__file__)
filePath = os.path.dirname(path)
db=pymysql.connect(user='root',password='dls123',host='127.0.0.1',port=3306,charset = 'utf8')
cur = db.cursor()
class TrayIcon(QtWidgets.QSystemTrayIcon):
    def __init__(self, MainWindow):
        super().__init__()
        self.ui = MainWindow
        self.createMenu()
    def hidelistwindow(self):
        if self.ui.listwindow.isVisible()==1:
            self.ui.listwindow.hide()
        else:
            self.ui.listwindow.show()
    def createMenu(self):
        self.menu = QtWidgets.QMenu()
        #self.showAction1 = QtWidgets.QAction("启动", self, triggered=self.show_window)
        #self.showAction2 = QtWidgets.QAction("显示通知", self, triggered=self.showMsg)
        self.quitAction = QtWidgets.QAction("退出", self, triggered=self.quit)

        #self.menu.addAction(self.showAction1)
        #self.menu.addAction(self.showAction2)
        self.menu.addAction(self.quitAction)
        self.setContextMenu(self.menu)

        # 设置图标
        self.setIcon(QtGui.QIcon('icon.ico'))
        self.icon = self.MessageIcon()

        # 把鼠标点击图标的信号和槽连接
        self.activated.connect(self.onIconClicked)

    def showMsg(self):
        self.showMessage("喝水提醒小工具", "点击退出", self.icon)

    def show_window(self):
        # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
        self.ui.showNormal()
        self.ui.activateWindow()

    def quit(self):
        if self.ui.child != None:
            self.ui.child.close()
        self.ui.saveTaskList()
        # 保存listwindow
        count = self.ui.listwindow.listWidget.count()
        sql = "DELETE FROM maido.listwindow WHERE user='%s'" % self.ui.Username
        # print(sql)
        try:
            cur.execute(sql)
            db.commit()
        except:
            # 如果发生错误则回滚
            db.rollback()
            print("删除失败")
        newdf = pd.DataFrame(columns=["taskname", "color", "deadline", "user"])
        for i in range(count):
            curitem = self.ui.listwindow.listWidget.item(i)
            data = {'taskname': curitem.data(Qt.UserRole), 'color': curitem.data(Qt.UserRole + 1),
                    'deadline': curitem.data(Qt.UserRole + 2), 'user': self.ui.Username}
            newdf.loc[len(newdf), :] = data
        #print(newdf)
        DTYPES = {"taskname": TEXT, "color": CHAR(20), "deadline": DATETIME, "user": VARCHAR(45)}
        engine = create_engine('mysql+pymysql://root:dls123@127.0.0.1:3306/maido?charset=utf8', echo=True)
        try:
            newdf.to_sql('listwindow', con=engine, if_exists='append', index=False, dtype=DTYPES, chunksize=50)
            print(">>> All good.")
        except Exception as e:
            print(">>> Something went wrong!")
        QtWidgets.qApp.quit()

    def closeEvent(self, event):
        pass
    # 鼠标点击icon传递的信号会带有一个整形的值，1是表示单击右键，2是双击，3是单击左键，4是用鼠标中键点击
    def onIconClicked(self, reason):
        if reason == 2 or reason == 3:
            if self.ui.isMinimized() or not self.ui.isVisible():
                # 若是最小化，则先正常显示窗口，再变为活动窗口（暂时显示在最前面）
                #self.ui.showNormal()
                #self.ui.activateWindow()
                #self.ui.setWindowFlags(QtCore.Qt.Window)
                self.ui.show()
                self.hide()

