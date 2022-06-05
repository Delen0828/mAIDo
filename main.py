from PyQt5.Qt import *
from add import Ui_Form
import sys
class Window(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("添加到list")
        self.resize(600, 500)
        self.setupUi(self)
        self.func_list()

    def func_list(self):
        self.model = QStringListModel()
        self.list = []
        self.model.setStringList(self.list)
        self.listView.setModel(self.model)

    def add(self):        #
        #print(self.textEdit.toPlainText())
        self.list.append(self.textEdit.toPlainText())
        self.model.setStringList(self.list)
        self.listView.setModel(self.model)
        #print(self.list)

    def DelListItem(self):
        selected = self.listView.selectedIndexes()

        for i in selected:
            #print (i.row())
            del self.list[i.row()]
        self.model.setStringList(self.list)
        self.listView.setModel(self.model)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())