# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'downloadobject.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QHeaderView

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        #Form.resize(720, 576)
        Form.setFixedSize(720, 576)
        #Form.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)


        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Interactive) #可调整大小
        #self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #自适应大小
        self.tableWidget.horizontalHeader().resizeSection(0, 350)
        self.tableWidget.horizontalHeader().resizeSection(1, 100)
        self.tableWidget.horizontalHeader().resizeSection(2, 75)
        self.tableWidget.horizontalHeader().resizeSection(3, 75)
        self.tableWidget.horizontalHeader().resizeSection(4, 75)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.7)
        self.tableWidget.setGraphicsEffect(op)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "名称"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "大小"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "类型"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "操作"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "权级"))
