from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import sys,os

class Ui_login(QWidget):
    def __init__(self):
        super().__init__()

        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 0, 211, 71))

        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 101, 71))
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(images/Iron.png)}")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))

if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_login()
    ex.show()
    sys.exit(loginapp.exec_())