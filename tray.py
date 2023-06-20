from PyQt5 import QtWidgets, QtCore, QtGui
import os
from PyQt5.QtWidgets import QShortcut
from PyQt5.QtGui import QKeySequence
path = os.path.abspath(__file__)
filePath = os.path.dirname(path)

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

