import sys
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QThread, pyqtSignal

class MainWindow(QMainWindow):
    def __init__(self, ):
        super(QMainWindow, self).__init__()
        self.number = 0


        w = QWidget()
        self.setCentralWidget(w)

        self.topFiller = QWidget()
        self.topFiller.setMinimumSize(200, 1000)  #######设置滚动区域的尺寸
        for filename in range(20):
            self.MapButton = QPushButton(self.topFiller)
            self.MapButton.setText(str(filename))
            self.MapButton.move(10, filename * 40)

        # self.MapButton = QPushButton(self.topFiller)
        # self.MapButton.setText("My Button")
        # self.MapButton.move(50, 50)

                ##创建一个滚动条
        self.scroll = QScrollArea()
        self.scroll.setWidget(self.topFiller)

        self.vbox = QVBoxLayout()
        self.vbox.addWidget(self.scroll)
        w.setLayout(self.vbox)

        # self.statusBar().showMessage("底部信息栏")
        # self.resize(300, 500)

        self.setupUi(self)

    def setupUi(self, Form):
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
        self.spinBoxMinimum.setValue(10)
        # min = self.spinBoxMinimum.value()

        self.spinBoxMaximum = QtWidgets.QSpinBox(Form)
        self.spinBoxMaximum.setGeometry(QtCore.QRect(80, 200, 42, 22))
        self.spinBoxMaximum.setObjectName("spinBoxMaximum")
        self.spinBoxMaximum.setValue(10)
        # max = self.spinBoxMaximum.value()
        # print(self.spinBoxMaximum.value())

        self.spinBoxPY = QtWidgets.QSpinBox(Form)
        self.spinBoxPY.setGeometry(QtCore.QRect(200, 70, 51, 21))
        self.spinBoxPY.setObjectName("spinBoxPY")
        self.spinBoxPY.setValue(10)
        # py = self.spinBoxPY.value()

        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(200, 30, 61, 21))
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        #self.pushButton.clicked.connect(Form.UpdateText)
        #self.spinBoxMinimum.editingFinished.connect(Form.Min)
        #self.spinBoxMaximum.editingFinished.connect(Form.Max)
        #self.spinBoxPY.editingFinished.connect(Form.pychanged)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Random"))
        self.pushButton.setText(_translate("Form", "Start"))
        self.label.setText(_translate("Form", "<html><head/><body><p align=\"center\">1</p></body></html>"))
        self.label_2.setText(_translate("Form", "PY交易"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec_())