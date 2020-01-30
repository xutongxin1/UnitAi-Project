# -*- coding: utf-8 -*-
# Created by: PyQt5 UI code generator 5.13.0



import sys, random, time, os, json
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

max = 501
min = 1
py = 0
i = 20
dic = 0

def load_json_data():
    global min, max, py, dic
    if os.path.exists("./data.json"):
        with open("./data.json", 'r', encoding='utf-8') as f:
            #print(f)
            js = f.read()
            dic = json.loads(js.replace("'", "\""))
            #dic = json.load(f)
            max = dic["max"]
            min = dic["min"]
            py = dic["py"]
            #print(dic)
    else:
        data = """{
  "min": 1,
  "max": 50,
  "py": 0
}"""
        file = open('./data.json', 'w')
        file.write(data)


class MyThread(QThread):
    signal = pyqtSignal(str)
    def __init__(self, max, min, py):
        super(MyThread, self).__init__()
        self.max = max
        self.min = min
        self.py = py

    def run(self):
        global i
        random.seed(time.time())
        while i >= 0:
            num = random.randint(self.min, self.max)
            while num == py:
                num = random.randint(self.min, self.max)
            text = "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">" + str(num) + "</span></p></body></html>"
            i -= 1
            time.sleep(0.05)
            self.signal.emit(text)
        i = 20

class Ui_Form(QWidget):
    def __init__(self):
        super(Ui_Form,self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def UpdateText(self):
        # global thread
        self.MyThreado = MyThread(max, min, py)  # 实例化自己建立的任务线程类
        self.MyThreado.signal.connect(self.callback)  # 设置任务线程发射信号触发的函数
        self.MyThreado.start()
        # self.MyThreado.wait()
        # self.quit()

    def callback(self, signal):
        self.label.setText(signal)
        # print(signal)

    def Min(self):
        global min
        min = self.spinBoxMinimum.value()
        dic["min"] = min
        with open("./data.json", mode='r+', encoding='utf-8') as f:
            f.write(" ")
            f.write(str(dic))

    def Max(self):
        global max
        max = self.spinBoxMaximum.value()
        dic["max"] = max
        with open("./data.json", mode='r+', encoding='utf-8') as f:
            f.write(" ")
            f.write(str(dic))

    def pychanged(self):
        global py
        py = self.spinBoxPY.value()
        dic["py"] = py
        with open("./data.json", mode='r+', encoding='utf-8') as f:
            f.write(" ")
            f.write(str(dic))

    def setupUi(self, Form):
        global max, min, py
        load_json_data()

        Form.setObjectName("Form")
        Form.resize(150, 230)
        Form.setMinimumSize(QtCore.QSize(150, 230))
        Form.setMaximumSize(QtCore.QSize(300, 230))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("favicon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(41, 120, 71, 71))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(50, 31, 51, 51))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(22)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.spinBoxMinimum = QtWidgets.QSpinBox(Form)
        self.spinBoxMinimum.setGeometry(QtCore.QRect(20, 200, 42, 22))
        self.spinBoxMinimum.setObjectName("spinBoxMinimum")
        self.spinBoxMinimum.setValue(min)
        #min = self.spinBoxMinimum.value()

        self.spinBoxMaximum = QtWidgets.QSpinBox(Form)
        self.spinBoxMaximum.setGeometry(QtCore.QRect(80, 200, 42, 22))
        self.spinBoxMaximum.setObjectName("spinBoxMaximum")
        self.spinBoxMaximum.setValue(max)
        #max = self.spinBoxMaximum.value()
        # print(self.spinBoxMaximum.value())

        self.spinBoxPY = QtWidgets.QSpinBox(Form)
        self.spinBoxPY.setGeometry(QtCore.QRect(200, 70, 51, 21))
        self.spinBoxPY.setObjectName("spinBoxPY")
        self.spinBoxPY.setValue(py)
        #py = self.spinBoxPY.value()

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 61, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.UpdateText)
        self.spinBoxMinimum.editingFinished.connect(Form.Min)
        self.spinBoxMaximum.editingFinished.connect(Form.Max)
        self.spinBoxPY.editingFinished.connect(Form.pychanged)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Random"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">1</p></body></html>"))
        self.label_2.setText(_translate("Form", "PY交易"))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Form()
    w.show()
    sys.exit(app.exec_())
