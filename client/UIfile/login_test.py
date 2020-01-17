# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_test.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(509, 292)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_2 = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAutoFillBackground(False)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_6.addWidget(self.label_2)
        self.gridLayout.addLayout(self.verticalLayout_6, 1, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.textaccount = QtWidgets.QLineEdit(Dialog)
        self.textaccount.setObjectName("textaccount")
        self.verticalLayout_4.addWidget(self.textaccount)
        self.gridLayout.addLayout(self.verticalLayout_4, 0, 1, 1, 4)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_5.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_5, 1, 1, 1, 4)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setPointSize(13)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAutoFillBackground(False)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setObjectName("verticalLayout")
        self.proxyButton = QtWidgets.QPushButton(Dialog)
        self.proxyButton.setObjectName("proxyButton")
        self.verticalLayout.addWidget(self.proxyButton)
        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.loginButton = QtWidgets.QPushButton(Dialog)
        self.loginButton.setObjectName("loginButton")
        self.verticalLayout_8.addWidget(self.loginButton)
        self.visitButton = QtWidgets.QPushButton(Dialog)
        self.visitButton.setObjectName("visitButton")
        self.verticalLayout_8.addWidget(self.visitButton)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 4, 2, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.remember = QtWidgets.QCheckBox(Dialog)
        self.remember.setObjectName("remember")
        self.verticalLayout_2.addWidget(self.remember)
        self.gridLayout.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.Auto = QtWidgets.QCheckBox(Dialog)
        self.Auto.setObjectName("Auto")
        self.verticalLayout_7.addWidget(self.Auto)
        self.gridLayout.addLayout(self.verticalLayout_7, 2, 2, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label_2.setText(_translate("Dialog", "  密码"))
        self.label.setText(_translate("Dialog", "  账号 "))
        self.proxyButton.setText(_translate("Dialog", "设置"))
        self.loginButton.setText(_translate("Dialog", "登录"))
        self.visitButton.setText(_translate("Dialog", "普通使用"))
        self.remember.setText(_translate("Dialog", "保存密码"))
        self.Auto.setText(_translate("Dialog", "自动登录"))


