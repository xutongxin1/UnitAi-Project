import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *

class Ui_Form(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        #self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowTitle("Live2D")
        Form.resize(302, 270)
        Form.setMinimumSize(QtCore.QSize(302, 270))
        Form.setMaximumSize(QtCore.QSize(302, 270))

        #self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #Form.setWindowOpacity(0.1)  # 设置窗口透明度
        #Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.browser = QWebEngineView()
        # 加载外部页面，调用
        self.browser.load(QUrl("C:/Users/Jay/Desktop/live2d/demo2.html"))
        self.setCentralWidget(self.browser)

        op = QtWidgets.QGraphicsOpacityEffect()
        # 设置透明度的值，0.0到1.0，最小值0是透明，1是不透明
        op.setOpacity(1)
        self.browser.setGraphicsEffect(op)
        #op.setOpacity(0)
        #Form.setGraphicsEffect(op)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Ui_Form()
    w.show()
    sys.exit(app.exec_())