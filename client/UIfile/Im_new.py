# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Im_new.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1024, 768)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(300, 0, 211, 71))
        self.pushButton.setStyleSheet(".button {\n"
"  display: inline-block;\n"
"  border-radius: 4px;\n"
"  background-color: #33ccff;\n"
"  border: none;\n"
"  color: #3366ff;\n"
"  text-align: center;\n"
"  font-size: 28px;\n"
"  padding: 20px;\n"
"  width: 200px;\n"
"  transition: all 0.5s;\n"
"  cursor: pointer;\n"
"  margin: 5px;\n"
"}\n"
"\n"
".button span {\n"
"  cursor: pointer;\n"
"  display: inline-block;\n"
"  position: relative;\n"
"  transition: 0.5s;\n"
"}\n"
"\n"
".button span:after {\n"
"  content: \'»\';\n"
"  position: absolute;\n"
"  opacity: 0;\n"
"  top: 0;\n"
"  right: -20px;\n"
"  transition: 0.5s;\n"
"}\n"
"\n"
".button:hover span {\n"
"  padding-right: 25px;\n"
"}\n"
"\n"
".button:hover span:after {\n"
"  opacity: 1;\n"
"  right: 0;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 0, 101, 71))
        self.pushButton_2.setStyleSheet("\n"
"\n"
"border-radius:5px;\n"
"\n"
"background-color: rgb(85, 170,0);\n"
"\n"
"")
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton.setText(_translate("Form", "PushButton"))
        self.pushButton_2.setText(_translate("Form", "PushButton"))
