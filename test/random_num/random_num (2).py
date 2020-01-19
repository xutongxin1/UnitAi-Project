# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Jay\test\random.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys, random, time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QThread, pyqtSignal



i = 20
class MyThread(QThread):
    signal = pyqtSignal(str)
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        global i
        while i >= 0:
            num = random.randint(1, 50)
            text = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">" + str(num) + "</span></p></body></html>"
            i -= 1
            time.sleep(0.05)
            self.signal.emit(text)
        i = 20



class Ui_Random(QWidget):
    def __init__(self):
        super(Ui_Random, self).__init__()
        self.setupUi(self)

    def _update(self):
        #global thread
        self.MyThreado = MyThread()# 实例化自己建立的任务线程类
        self.MyThreado.signal.connect(self.callback)# 设置任务线程发射信号触发的函数
        self.MyThreado.start()
        #self.MyThreado.wait()
        #self.quit()


    def callback(self, signal):  # 这里的 i 就是任务线程传回的数据
        self.label.setText(signal)
        #print(signal)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(148, 220)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(40, 130, 71, 71))
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 10, 111, 101))
        self.label.setObjectName("label")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form._update)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setToolTip(_translate("Form", "<html><head/><body><p><span style=\" font-size:11pt;\">Start</span></p></body></html>"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">1</span></p></body></html>"))




if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Random()
    w.show()
    sys.exit(app.exec_())