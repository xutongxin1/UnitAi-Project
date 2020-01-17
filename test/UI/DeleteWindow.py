# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Jay\test\UI\DeleteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class Ui_DeleteWindow(object):

    def respond_yes(self):
        exit()

    def respond_no(self):
        exit()

    def setupUi(self, DeleteWindow):
        DeleteWindow.setObjectName("DeleteWindow")
        DeleteWindow.setEnabled(True)
        DeleteWindow.resize(260, 120)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(False)
        font.setWeight(50)
        DeleteWindow.setFont(font)
        DeleteWindow.setFocusPolicy(QtCore.Qt.ClickFocus)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../../PyCharm/PyCharm Community Edition 2019.1.1/bin/pycharm.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        DeleteWindow.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(DeleteWindow)
        self.buttonBox.setGeometry(QtCore.QRect(50, 70, 156, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(DeleteWindow)
        self.label.setGeometry(QtCore.QRect(70, 30, 131, 16))
        self.label.setObjectName("label")

        self.retranslateUi(DeleteWindow)
        self.buttonBox.accepted.connect(DeleteWindow.respond_yes)
        self.buttonBox.accepted.connect(DeleteWindow.respond_no)
        QtCore.QMetaObject.connectSlotsByName(DeleteWindow)

    def retranslateUi(self, DeleteWindow):
        _translate = QtCore.QCoreApplication.translate
        DeleteWindow.setWindowTitle(_translate("DeleteWindow", "Delete"))
        self.label.setText(_translate("DeleteWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:11pt;\">Sure to delete?</span></p></body></html>"))


class mwindow(QWidget, Ui_DeleteWindow):
    def __init__(self):
        super(mwindow, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = mwindow()
    w.show()
    sys.exit(app.exec_())