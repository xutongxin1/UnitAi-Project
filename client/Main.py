# code:utf-8
Version="0.0.1b"
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMenu, QLineEdit, QMainWindow, QDialog, QWidget
from PyQt5.QtCore import QCoreApplication, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPalette, QBrush
import sys, os, configparser,ctypes

# 基本五大包导入

# 以下为导入功能包
import hashlib
import socket
import json
import time

# 以下为导入自定义函数
# 窗口
from login import Ui_login
from Im import Ui_IM
from Chooseserver import Ui_chooseserver
from config import config
# 发送数据程序

from send import login

# 全局变量
imgpath = "./images/login.jpg"

loginmode = config("acc", "loginmode")
acc = config("acc", "acc")
pd = config("acc", "pd")

op = QtWidgets.QGraphicsOpacityEffect()
op.setOpacity(0.5)


class LoginWindow(QWidget):
    def __init__(self):
        QMainWindow.__init__(self)
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID("myappid")  # 系统图标
        self.setWindowIcon(QIcon('.\images\Iron.png'))

        self.main_ui = Ui_login()
        self.main_ui.setupUi(self)

    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap(imgpath)  # 换成自己的图片的相对路径
        painter.drawPixmap(self.rect(), pixmap)


class ImWindow(QWidget):
    def __init__(self):
        QDialog.__init__(self)

        self.Im = Ui_IM()
        self.Im.setupUi(self)


class chooseserverWindow(QWidget):
    def __init__(self):
        QDialog.__init__(self)

        self.ser = Ui_chooseserver()
        self.ser.setupUi(self)

    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap('.\images\serverchoose.png')  # 换成自己的图片的相对路径
        painter.drawPixmap(self.rect(), pixmap)


def Im_reload(acc):
    print(1)
    Im_account = Imapp.Im.account
    Im_account.setText(acc)

    if acc == "xutongxin":
        Im_account.setStyleSheet("font: 12pt \"萝莉体 第二版\";\n"
                                 "color: rgb(102, 204, 255);")


class logindef():
    def login_action(self):
        # loginButton = loginapp.main_ui.loginButton
        loginButton.clicked.connect(self.login1)

        proxyButton.clicked.connect(self.chooseserver)
        lo_textaccount.editingFinished.connect(self.root)
        if loginmode == "2":
            login(acc, pd)
        # login事件绑定

    def chooseserver(self):

        chooseserverapp.show()

    # Im事件回调

    def root(self):
        global imgpath
        if (lo_textaccount.text() == "xutongxin"):
            loginapp.close()
            imgpath = "./images/xlogin.jpg"
            loginapp.show()

    def login1(self):
        loginButton.setEnabled(False)
        acc = lo_textaccount.text()
        pd = lo_textpassword.text()
        # 获取密码和账号
        re = int(login(acc, pd))
        if (re == 0):
            loginButton.setText("登录成功")
            loginapp.close()
            Imapp.show()
            Im_reload("xutongxin")
        elif (re == 2):
            loginButton.setEnabled(True)
            loginButton.setText("用户不存在")
        elif (re == -1):
            loginButton.setEnabled(True)
            loginButton.setText("服务器异常")
        else:
            loginButton.setEnabled(True)
            loginButton.setText("密码错误")


# 特殊界面回调


# 登陆事件函数
if __name__ == '__main__':
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QApplication(sys.argv)
    loginapp = LoginWindow()  # 初始化login界面
    Imapp = ImWindow()  # 初始化Im界面
    logindef = logindef()
    loginapp.setWindowTitle("登录")
    chooseserverapp = chooseserverWindow()
    lo_textpassword = loginapp.main_ui.textpassword
    lo_remember = loginapp.main_ui.remember
    lo_Auto = loginapp.main_ui.Auto
    lo_textaccount = loginapp.main_ui.textaccount
    loginButton = loginapp.main_ui.loginButton
    proxyButton = loginapp.main_ui.proxyButton
    # login类继承

    logindef.login_action()  # login事件总线

    loginapp.show()

    sys.exit(app.exec_())
