from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import sys,os

from downloadobject import Ui_Form
class Ui_login(QWidget):
    def __init__(self):
        super().__init__()

        self.Ui = Ui_Form()
        self.Ui.setupUi(self)

if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_login()
    ex.show()
    sys.exit(loginapp.exec_())