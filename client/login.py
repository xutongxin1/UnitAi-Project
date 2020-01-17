# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import sys,os,configparser

# 基本五大包导入


# PyQt5.QtWidgets import*
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# 以下为导入功能包
import socket
import json
import hashlib
import time
import ctypes

from config import config
# 以下为导入自定义函数

# import Im
# from Main import loginsuccess

loginmode=config("acc","loginmode")
acc=config("acc","acc")
pd=config("acc","pd")


class Ui_login(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def auto(self):
        if self.Auto.isChecked():
            self.remember.setChecked(True)

    def setupUi(self, Form):


        Form.setObjectName("登陆")
        Form.resize(1024,728)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.remember = QtWidgets.QCheckBox(Form)
        self.remember.setObjectName("remember")
        self.horizontalLayout_3.addWidget(self.remember)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.Auto = QtWidgets.QCheckBox(Form)
        self.Auto.setObjectName("Auto")
        self.horizontalLayout_3.addWidget(self.Auto)
        self.gridLayout.addLayout(self.horizontalLayout_3, 3, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(75, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 3, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setMinimumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.textaccount = QtWidgets.QLineEdit(Form)
        self.textaccount.setMinimumSize(QtCore.QSize(70, 30))
        self.textaccount.setObjectName("textaccount")
        self.horizontalLayout.addWidget(self.textaccount)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 1, 1, 3)
        self.proxyButton = QtWidgets.QPushButton(Form)
        self.proxyButton.setMaximumSize(QtCore.QSize(100, 16777215))
        self.proxyButton.setObjectName("proxyButton")
        self.gridLayout.addWidget(self.proxyButton, 4, 1, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem3, 1, 1, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setMinimumSize(QtCore.QSize(70, 30))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.textpassword = QtWidgets.QLineEdit(Form)
        self.textpassword.setMinimumSize(QtCore.QSize(0, 30))
        self.textpassword.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.textpassword)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 1, 1, 3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setMinimumSize(QtCore.QSize(0, 50))
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout.addWidget(self.loginButton)
        self.visitButton = QtWidgets.QPushButton(Form)
        self.visitButton.setMinimumSize(QtCore.QSize(0, 50))
        self.visitButton.setObjectName("visitButton")
        self.verticalLayout.addWidget(self.visitButton)
        self.gridLayout.addLayout(self.verticalLayout, 3, 3, 2, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        op1 = QtWidgets.QGraphicsOpacityEffect()
        op1.setOpacity(0.5)
        self.textaccount.setGraphicsEffect(op)
        self.textpassword.setGraphicsEffect(op1)
        # 完成界面第一初始化
        # 以下为修改界面参数

        # 设置文本框的默认浮现文本 https://blog.csdn.net/jia666666/article/details/81510502
        self.textaccount.setPlaceholderText("账号")
        self.textpassword.setPlaceholderText("密码")
        # QLineEdit.NoEcho：不显示任何输入的字符，常用于密码类型的输入，且长度保密
        self.textpassword.setEchoMode(QLineEdit.Password)

        # 无边框
        # self.setWindowFlags(Qt.Qt.FramelessWindowHint | Qt.Qt.WindowStaysOnTopHint)

        # screen = QtGui.QDesktopWidget().screenGeometry()
        # setGeometry(0, 0, screen.width(), screen.height())

        # 按钮事件绑定
        self.Auto.clicked.connect(self.auto)
        if loginmode== "2":
            self.textaccount.setText(acc)
            self.textpassword.setText('111111')
        if loginmode == "1":
            self.textaccount.setText(acc)
            self.textpassword.setText('111111')
            self.remember.setChecked(True)

    # 结束第二初始化

    # self.showMaximized()

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.remember.setText(_translate("Form", "保存密码"))
        self.Auto.setText(_translate("Form", "自动登录"))
        self.label.setText(_translate("Form", "  账号 "))
        self.proxyButton.setText(_translate("Form", "服务器设置"))
        self.label_2.setText(_translate("Form", "  密码"))
        self.loginButton.setText(_translate("Form", "登录"))
        self.visitButton.setText(_translate("Form", "普通使用"))
    # 本地化


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_login()
    sys.exit(loginapp.exec_())
