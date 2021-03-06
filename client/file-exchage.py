# code:utf-8
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMenu, QLineEdit, QMainWindow, QDialog, QFileDialog, \
    QTableWidgetItem
from PyQt5.QtCore import QCoreApplication, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPalette, QBrush
import sys, os, socket, json, time, hashlib

# 基本五大包导入
from send import sendfile,download

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
        if len(files) == 0:
            return
        global num
        for path in files:
            print(path)
            self.tableWidget.setItem(num, 0, QTableWidgetItem(num))
            self.tableWidget.setItem(num, 1, QTableWidgetItem(path))
            filepath, fullflname = os.path.split(path)
            fname, ext = os.path.splitext(fullflname)
            print(ext)

            if (ext == ".doc" or ext == ".docx" or ext == ".ppt" or ext == ".pptx" or ext == ".xlsx" or ext == ".ppts"):
                self.tableWidget.setItem(num, 2, QTableWidgetItem("pdf"))
            self.tableWidget.setItem(num, 3, QTableWidgetItem("就绪"))

    def choose_document(self):
        dir_choose = QFileDialog.getExistingDirectory(self,
                                                      "选取文件夹",
                                                      'C:/')  # 起始路径
        if len(dir_choose) == 0:
            return
        global num
        list = os.listdir(dir_choose)  # 列出文件夹下所有的目录与文件
        for i in range(0, len(list)):
            path = os.path.join(dir_choose, list[i])
            if os.path.isfile(path):
                print(path)

                self.tableWidget.setItem(num, 0, QTableWidgetItem(num))
                self.tableWidget.setItem(num, 1, QTableWidgetItem(path))
                filepath, fullflname = os.path.split(path)
                print(fullflname)
                fname, ext = os.path.splitext(fullflname)

                # if(ext=="doc"or ext=="docx" or ext=="ppt" or ext=="pptx" or ext=="xlsx" or ext=="ppts"):
                # self.tableWidget.setItem(num, 2, QTableWidgetItem("pdf"))
                # ext = self.tableWidget.item(num, 2).text()
                # print(ext)
                self.tableWidget.setItem(num, 3, QTableWidgetItem("就绪"))
                num += 1

    def begin1(self):
        num1 = 0
        while num1 <= num:
            path = self.tableWidget.item(num1, 1).text()
            formatto = self.tableWidget.item(num1, 2).text()
            print(path)
            filepath, fullflname = os.path.split(path)
            print(fullflname)
            key = "123321"
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
            # md5 = str(hash_code).lower()

            data = {
                "order": True,
                "apikey": key,
                "filename": fullflname,
                "md5": md5,
                "formatto": formatto
            }
            print(data)
            # data=json.dumps(data)
            # back=0
            url = "http://127.0.0.1:19150/upload/exchange"
            back = int(sendfile(url, data, path, "ex"))
            if (back == 0):
                print("ok")
                self.tableWidget.setItem(num1, 3, QTableWidgetItem("上传完成"))
            elif (back == 1):
                self.tableWidget.setItem(num1, 3, QTableWidgetItem("未授权"))
                return
            elif (back == 2):
                print("Error")
                self.tableWidget.setItem(num1, 3, QTableWidgetItem("上传错误"))
                return
            elif (back == 3):
                self.tableWidget.setItem(num1, 3, QTableWidgetItem("无法连接到服务器"))
                return
            elif (back == 4):
                self.tableWidget.setItem(num1, 3, QTableWidgetItem("服务器错误"))
                return
            num1 += 1
        time.sleep(1)


        num1=0
        while num1 <= num:
            path = self.tableWidget.item(num1, 1).text()
            formatto = self.tableWidget.item(num1, 2).text()
            filepath, fullflname = os.path.split(path)
            (filename, extension) = os.path.splitext(fullflname)
            #name = filename + "." + formatto # TODO(xtx): 后缀修改为了测试
            name=fullflname
            data = {
                "apikey": "123321",
                "filename": name,
            }
            n=1
            while n<10:
                result = download("http://127.0.0.1:19150/download/exchange", data)
                if result == 404:
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("无法连接到服务器"))
                    break
                elif result == 501:
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("请稍后,第" + n + "次尝试"))
                    time.sleep(2)
                    n+=1
                    pass
                else:
                    name = filename + "." + formatto
                    name = filepath + "/" + name
                    with open(name, 'wb') as f:
                        f.write(result)
                    self.tableWidget.setItem(num1, 3, QTableWidgetItem("完成转换"))
                    break
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
        titles = ['编号', '文件路径', '目标格式', '状态']
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
        # 第一初始化
        self.document.clicked.connect(self.choose_document)
        self.file.clicked.connect(self.choose_file)
        self.begin.clicked.connect(self.begin1)
        # 绑定槽
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


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    file_exchange = QApplication(sys.argv)
    ex = Ui_file_exchange()
    sys.exit(file_exchange.exec_())
