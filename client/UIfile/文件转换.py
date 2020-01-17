# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '文件转换.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(800, 571)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(0, 0, 101, 51))
        self.pushButton.setObjectName("pushButton")
        self.mode = QtWidgets.QComboBox(Dialog)
        self.mode.setGeometry(QtCore.QRect(700, 0, 101, 51))
        self.mode.setObjectName("mode")
        self.mode.addItem("")
        self.mode.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Dialog)
        self.tableWidget.setGeometry(QtCore.QRect(0, 50, 801, 431))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.file = QtWidgets.QPushButton(Dialog)
        self.file.setGeometry(QtCore.QRect(620, 480, 91, 41))
        self.file.setObjectName("file")
        self.document = QtWidgets.QPushButton(Dialog)
        self.document.setGeometry(QtCore.QRect(710, 480, 91, 41))
        self.document.setObjectName("document")
        self.begin = QtWidgets.QPushButton(Dialog)
        self.begin.setGeometry(QtCore.QRect(690, 520, 111, 51))
        self.begin.setObjectName("begin")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(480, 480, 141, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.mode_2 = QtWidgets.QComboBox(Dialog)
        self.mode_2.setGeometry(QtCore.QRect(530, 0, 171, 51))
        self.mode_2.setObjectName("mode_2")
        self.mode_2.addItem("")
        self.mode_2.addItem("")
        self.mode_2.addItem("")
        self.mode_2.addItem("")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "返回"))
        self.mode.setItemText(0, _translate("Dialog", "本地转换"))
        self.mode.setItemText(1, _translate("Dialog", "云转换"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "新建列"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "文件路径"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "目标格式"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "文件转换进度"))
        self.file.setText(_translate("Dialog", "选择文件"))
        self.document.setText(_translate("Dialog", "选择文件夹"))
        self.begin.setText(_translate("Dialog", "开始"))
        self.mode_2.setItemText(0, _translate("Dialog", "全类型文件"))
        self.mode_2.setItemText(1, _translate("Dialog", "文档类"))
        self.mode_2.setItemText(2, _translate("Dialog", "音频类"))
        self.mode_2.setItemText(3, _translate("Dialog", "图片类"))

