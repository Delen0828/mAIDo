import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QWidget,QDialog
from Ui_untitled import Ui_Dialog  #导入你写的界面类
 
 
class MyMainWindow(QDialog,Ui_Dialog): #这里也要记得改
    def __init__(self,parent =None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)
 
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())