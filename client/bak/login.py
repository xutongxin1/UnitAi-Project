# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import  QApplication, QLineEdit,QMainWindow
from PyQt5.QtGui import QIcon, QPixmap,QPalette,QBrush
import sys

#基本五大包导入



# PyQt5.QtWidgets import*
#from PyQt5.QtCore import *
#from PyQt5.QtGui import *
#from PyQt5.QtWidgets import *

#以下为导入功能包
import socket
import json
import hashlib
import time
import ctypes
#以下为导入自定义函数

#import Im
#from Main import loginsuccess

with open("./config/config.json", 'r') as load_f:
    load_dict = json.load(load_f)


class Ui_login(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)




    def auto(self):
        if self.Auto.isChecked():
            self.remember.setChecked(True)


    def setupUi(self, Dialog):
        #json加载
        with open("./config/config.json", 'r') as load_f:
            load_dict = json.load(load_f)


        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 292)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(33, 70, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(33, 150, 54, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.remember = QtWidgets.QCheckBox(Dialog)
        self.remember.setGeometry(QtCore.QRect(110, 200, 71, 16))
        self.remember.setObjectName("remember")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setGeometry(QtCore.QRect(410, 210, 91, 41))
        self.loginButton.setObjectName("loginButton")
        self.proxyButton = QtWidgets.QPushButton(Dialog)
        self.proxyButton.setGeometry(QtCore.QRect(10, 250, 111, 31))
        self.proxyButton.setObjectName("proxyButton")
        self.Auto = QtWidgets.QCheckBox(Dialog)
        self.Auto.setGeometry(QtCore.QRect(270, 200, 71, 16))
        self.Auto.setObjectName("Auto")
        self.language = QtWidgets.QComboBox(Dialog)
        self.language.setGeometry(QtCore.QRect(130, 250, 121, 31))
        self.language.setObjectName("language")
        self.language.addItem("")
        self.language.addItem("")
        self.language.addItem("")
        self.visitButton = QtWidgets.QPushButton(Dialog)
        self.visitButton.setGeometry(QtCore.QRect(410, 250, 91, 41))
        self.visitButton.setObjectName("visitButton")
        self.textaccount = QtWidgets.QLineEdit(Dialog)
        self.textaccount.setGeometry(QtCore.QRect(100, 60, 351, 31))
        self.textaccount.setObjectName("textaccount")
        self.textpassword = QtWidgets.QLineEdit(Dialog)
        self.textpassword.setGeometry(QtCore.QRect(100, 140, 351, 31))
        self.textpassword.setObjectName("textpassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        op1 = QtWidgets.QGraphicsOpacityEffect()
        op1.setOpacity(0.5)
        self.textaccount.setGraphicsEffect(op)
        self.textpassword.setGraphicsEffect(op1)
        #完成界面第一初始化
        #以下为修改界面参数

        # 设置文本框的默认浮现文本 https://blog.csdn.net/jia666666/article/details/81510502
        self.textaccount.setPlaceholderText("账号")
        self.textpassword.setPlaceholderText("密码")
        # QLineEdit.NoEcho：不显示任何输入的字符，常用于密码类型的输入，且长度保密
        self.textpassword.setEchoMode(QLineEdit.Password)


        #无边框
        #self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint)

        #screen = QtGui.QDesktopWidget().screenGeometry()
        #setGeometry(0, 0, screen.width(), screen.height())


        #按钮事件绑定
        self.Auto.clicked.connect(self.auto)

        if load_dict["loginmode"] == 2:
            self.textaccount.setText(load_dict["acc"])
            self.textpassword.setText(load_dict["pd"])
            self.login()
            return 0
        if load_dict["loginmode"]==1:
            self.textaccount.setText(load_dict["acc"])
            self.textpassword.setText(load_dict["pd"])
            self.remember.setChecked(True)
        # 结束第二初始化

        #self.showMaximized()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "  账号 "))
        self.label_2.setText(_translate("Dialog", "  密码"))
        self.remember.setText(_translate("Dialog", "保存密码"))
        self.loginButton.setText(_translate("Dialog", "登录"))
        self.proxyButton.setText(_translate("Dialog", "代理设置"))
        self.Auto.setText(_translate("Dialog", "自动登录"))
        self.language.setItemText(0, _translate("Dialog", "Language:中文"))
        self.language.setItemText(1, _translate("Dialog", "Language:English"))
        self.language.setItemText(2, _translate("Dialog", "Language:"))
        self.visitButton.setText(_translate("Dialog", "普通使用"))
        #本地化



if __name__ == '__main__':#调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_login()
    sys.exit(loginapp.exec_())