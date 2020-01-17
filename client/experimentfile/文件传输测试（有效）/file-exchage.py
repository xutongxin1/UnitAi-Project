# code:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QApplication, QPushButton, QMenu,QLineEdit,QMainWindow,QDialog,QFileDialog,QTableWidgetItem
from PyQt5.QtCore import QCoreApplication,QTimer,QThread,pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QPixmap,QPalette,QBrush
import sys,os,socket,json,time,hashlib

#基本五大包导入
from send import sendfile1
num = 0
class Ui_file_exchange(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def choose_file(self):
            files, filetype = QFileDialog.getOpenFileNames(self,
                                                           "多文件选择",
                                                           "C:/",  # 起始路径
                                                           "All Files (*)")
            if len(files)==0:
                return
            global num
            for file in files:
                print(file)
                self.tableWidget.setItem(num, 0, QTableWidgetItem(num))
                self.tableWidget.setItem(num, 1, QTableWidgetItem(file))
                q = file.find('.', 10, -1)
                b = file[q + 1:]
                if (b == "doc" or b == "docx" or b == "ppt" or b == "pptx" or b == "md" or b == "ppts"):
                    self.tableWidget.setItem(num, 2, QTableWidgetItem("pdf"))
                self.tableWidget.setItem(num, 3, QTableWidgetItem("就绪"))

    def choose_document(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                  'C:/')  # 起始路径
        if len(dir_choose)==0:
            return
        global num
        list = os.listdir(dir_choose)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(dir_choose, list[i])
            if os.path.isfile(path):
                print(path)

                self.tableWidget.setItem(num, 0, QTableWidgetItem(num))
                self.tableWidget.setItem(num, 1, QTableWidgetItem(path))

                q=path.find('.', -5, -1)
                b=path[q+1:]
                if(b=="doc"or b=="docx" or b=="ppt" or b=="pptx" or b=="xlsx" or b=="ppts"):
                    self.tableWidget.setItem(num, 2, QTableWidgetItem("pdf"))
                    b = self.tableWidget.item(num, 2).text()
                    print(b)
                self.tableWidget.setItem(num, 3, QTableWidgetItem("就绪"))
                num+=1

    def begin1(self):
            num1=0
            while num1<=num:
                path = self.tableWidget.item(num1, 1).text()
                formatto = self.tableWidget.item(num1, 2).text()
                q = path.find('.', -5, -1)
                while path[q] != "/":
                    q -= 1
                filename = path[q + 1:]
                f = open(path, 'rb')
                file=f.read()
                size = len(file)
                key = "123321"
                f.close()
                f = open(path, 'rb')
                myHash = hashlib.md5()
                while True:
                    d = f.read(8096)
                    if not d:
                        break
                    myHash.update(d)
                md5 = myHash.hexdigest()
                f.close()
                print(md5)
                #md5 = str(hash_code).lower()

                head = {
                    "apikey": key,
                    "size": size,
                    "filename": filename,
                    "md5":md5,
                    "formatto":formatto
                }
                print(head)
                head=json.dumps(head)
                #back=0

                back=sendfile1("localhost",11170,head,path)
                if (back == 0):
                    print("ok")
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("上传完成"))
                elif(back == 1):
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("未授权"))
                    return
                elif(back == 2):
                    print("Error")
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("上传错误"))
                elif(back == 3):
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("无法连接到服务器"))
                    return
                num1+=1




    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 571)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.mode = QtWidgets.QComboBox(Dialog)
        self.mode.setGeometry(QtCore.QRect(700, 0, 101, 51))
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 801, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(1)
        titles=['编号','文件路径','目标格式','状态']
        self.tableWidget.setHorizontalHeaderLabels(titles)
        self.tableWidget.setColumnWidth(0, 50)
        self.tableWidget.setColumnWidth(1, 550)
        self.tableWidget.setColumnWidth(2, 100)
        self.tableWidget.setColumnWidth(3, 100)
        self.file = QtWidgets.QPushButton(Dialog)
        self.file.setGeometry(QtCore.QRect(620, 480, 91, 41))
        self.file.setObjectName("file")
        self.document = QtWidgets.QPushButton(Dialog)
        self.document.setGeometry(QtCore.QRect(710, 480, 91, 41))
        self.document.setObjectName("document")
        self.begin = QtWidgets.QPushButton(Dialog)
        self.begin.setGeometry(QtCore.QRect(690, 520, 111, 51))
        self.begin.setObjectName("begin")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(480, 480, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.mode2 = QtWidgets.QComboBox(Dialog)
        self.mode2.setGeometry(QtCore.QRect(530, 0, 171, 51))
        self.mode2.setObjectName("mode_2")
        self.mode2.addItem("")
        self.mode2.addItem("")
        self.mode2.addItem("")
        self.mode2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        #第一初始化
        self.document.clicked.connect(self.choose_document)
        self.file.clicked.connect(self.choose_file)
        self.begin.clicked.connect(self.begin1)
        #绑定槽
        self.show()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "返回"))
        self.mode.setItemText(0, _translate("Dialog", "本地转换"))
        self.mode.setItemText(1, _translate("Dialog", "云转换"))
        self.file.setText(_translate("Dialog", "选择文件"))
        self.document.setText(_translate("Dialog", "选择文件夹"))
        self.begin.setText(_translate("Dialog", "开始"))
        self.mode2.setItemText(0, _translate("Dialog", "全类型文件"))
        self.mode2.setItemText(1, _translate("Dialog", "文档类"))
        self.mode2.setItemText(2, _translate("Dialog", "音频类"))
        self.mode2.setItemText(3, _translate("Dialog", "图片类"))


if __name__ == '__main__':#调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    file_exchange = QApplication(sys.argv)
    ex = Ui_file_exchange()
    sys.exit(file_exchange.exec_())
