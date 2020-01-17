from PyQt5.QtWidgets import QHeaderView,QTableView
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget,QTableWidgetItem,QPushButton
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush,QPainter
import sys,os
num=0
access=0
class Ui_Downloadobject(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def download(self,id):
        print(id)
        self.tableWidget.setCellWidget(id, 3, self.downloadingbtn(id))
    def downloadstop(self,id):
        print(id)
    def fill(self,name,size,objecttype,access):
        global num
        self.tableWidget.setRowCount(num+1)
        self.tableWidget.setVerticalHeaderItem(num, QtWidgets.QTableWidgetItem())
        self.tableWidget.setItem(num, 0, QTableWidgetItem(str(name)))
        self.tableWidget.setItem(num, 1, QTableWidgetItem(size))
        self.tableWidget.setItem(num, 2, QTableWidgetItem(objecttype))
        self.tableWidget.setCellWidget(num, 3,self.downloadbtn(num))
        self.tableWidget.setItem(num, 4, QTableWidgetItem(access))
        num += 1
    def downloadingbtn(self,id):
        print(id)
        self.btn = QPushButton("下载中")
        self.btn.setDown(True)
        self.btn.clicked.connect(lambda: self.downloadstop(id))
        return self.btn
    def downloadbtn(self,id):
        self.btn = QPushButton("下载")
        self.btn.setDown(True)

        self.btn.clicked.connect(lambda:self.download(id))
        return self.btn
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(720, 576)
        Form.setFixedSize(720, 576)
        #Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)




        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive) #可调整大小
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #自适应大小
        self.tableWidget.horizontalHeader().resizeSection(0, 350)
        self.tableWidget.horizontalHeader().resizeSection(1, 100)
        self.tableWidget.horizontalHeader().resizeSection(2, 75)
        self.tableWidget.horizontalHeader().resizeSection(3, 75)
        self.tableWidget.horizontalHeader().resizeSection(4, 75)
        self.tableWidget.setEditTriggers(QTableView.NoEditTriggers)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        i=10
        while i<20:
            self.fill(i,"123",'123','123')
            i+=1

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "大小"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "操作"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "权级"))

if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_Downloadobject()
    #ex.paintEngine()
    ex.show()
    sys.exit(loginapp.exec_())
