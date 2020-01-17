# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseserver.no.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.ip = QtWidgets.QLineEdit(Dialog)
        self.ip.setGeometry(QtCore.QRect(100, 50, 201, 31))
        self.ip.setObjectName("ip")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 60, 81, 20))
        self.label.setObjectName("label")
        self.port = QtWidgets.QLineEdit(Dialog)
        self.port.setGeometry(QtCore.QRect(100, 110, 201, 31))
        self.port.setObjectName("port")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(40, 120, 54, 12))
        self.label_2.setObjectName("label_2")
        self.save = QtWidgets.QPushButton(Dialog)
        self.save.setGeometry(QtCore.QRect(320, 250, 75, 23))
        self.save.setObjectName("save")
        self.comboBox = QtWidgets.QComboBox(Dialog)
        self.comboBox.setGeometry(QtCore.QRect(40, 10, 141, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "服务器地址"))
        self.label_2.setText(_translate("Dialog", "端口"))
        self.save.setText(_translate("Dialog", "保存"))
        self.comboBox.setItemText(0, _translate("Dialog", "共享工作站"))
        self.comboBox.setItemText(1, _translate("Dialog", "私有工作站"))
