# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
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
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(100, 140, 351, 31))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

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

