# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Im1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1024, 657)
        Dialog.setStyleSheet("")
        self.head = QtWidgets.QLabel(Dialog)
        self.head.setGeometry(QtCore.QRect(0, 0, 111, 61))
        self.head.setText("")
        self.head.setObjectName("head")
        self.account = QtWidgets.QLabel(Dialog)
        self.account.setGeometry(QtCore.QRect(123, 21, 101, 41))
        self.account.setStyleSheet("font: 12pt \"萝莉体 第二版\";\n"
"color: rgb(102, 204, 255);")
        self.account.setText("")
        self.account.setObjectName("account")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(130, 60, 891, 551))
        self.label_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(212, 610, 731, 48))
        self.lineEdit.setObjectName("lineEdit")
        self.send = QtWidgets.QPushButton(Dialog)
        self.send.setGeometry(QtCore.QRect(943, 610, 82, 51))
        self.send.setObjectName("send")
        self.voice = QtWidgets.QPushButton(Dialog)
        self.voice.setGeometry(QtCore.QRect(130, 610, 82, 51))
        self.voice.setText("")
        self.voice.setObjectName("voice")
        self.workmode = QtWidgets.QPushButton(Dialog)
        self.workmode.setGeometry(QtCore.QRect(0, 60, 131, 51))
        self.workmode.setObjectName("workmode")
        self.livemode = QtWidgets.QPushButton(Dialog)
        self.livemode.setGeometry(QtCore.QRect(0, 110, 131, 51))
        self.livemode.setObjectName("livemode")
        self.setting = QtWidgets.QPushButton(Dialog)
        self.setting.setGeometry(QtCore.QRect(0, 735, 131, 34))
        self.setting.setObjectName("setting")
        self.function1 = QtWidgets.QPushButton(Dialog)
        self.function1.setGeometry(QtCore.QRect(340, 0, 112, 61))
        self.function1.setObjectName("function1")
        self.function2 = QtWidgets.QPushButton(Dialog)
        self.function2.setGeometry(QtCore.QRect(450, 0, 112, 61))
        self.function2.setObjectName("function2")
        self.function3 = QtWidgets.QPushButton(Dialog)
        self.function3.setGeometry(QtCore.QRect(560, 0, 112, 61))
        self.function3.setObjectName("function3")
        self.function4 = QtWidgets.QPushButton(Dialog)
        self.function4.setGeometry(QtCore.QRect(670, 0, 112, 61))
        self.function4.setObjectName("function4")
        self.more = QtWidgets.QPushButton(Dialog)
        self.more.setGeometry(QtCore.QRect(780, 0, 112, 61))
        self.more.setObjectName("more")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.send.setText(_translate("Dialog", "发送"))
        self.workmode.setText(_translate("Dialog", "工作模式"))
        self.livemode.setText(_translate("Dialog", "实例模式"))
        self.setting.setText(_translate("Dialog", "PushButton"))
        self.function1.setText(_translate("Dialog", "PushButton"))
        self.function2.setText(_translate("Dialog", "PushButton"))
        self.function3.setText(_translate("Dialog", "PushButton"))
        self.function4.setText(_translate("Dialog", "PushButton"))
        self.more.setText(_translate("Dialog", "PushButton"))

import 123_rc
