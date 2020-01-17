# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chooseserver.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QMessageBox
import sys,os,configparser
from send import login
from config import config


ipset=config("server","add")
portset=config("server","port")

class Ui_chooseserver(QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def testserver(self):
        try:
            serverversion=login('ConnectTest',123)
            print(serverversion)
            reply = QMessageBox.information(self,
                                    "测试结果",
                                    "服务器版本："+serverversion,
                                    QMessageBox.Yes)
        except:
            reply = QMessageBox.information(self,
                                    "测试结果",
                                    "无法连接至服务器",
                                    QMessageBox.Yes)
        return 0

    def save1(self):
        portset=self.port.text()
        ipset=self.ip.text()
        curpath = os.path.dirname(os.path.realpath(__file__))
        cfgpath = os.path.join(curpath, "config/user.ini")
        conf = configparser.ConfigParser()
        conf.read(cfgpath, encoding="utf-8")
        conf.set("server","port",portset)
        #conf.set("server","add",ip)
        try:
            conf.write(sys.stdout)
            reply = QMessageBox.information(self,
                                    '提示',
                                    "保存成功",
                                    QMessageBox.Yes)
        except:
            reply = QMessageBox.information(self,
                                    "提示",
                                    "保存失败",
                                    QMessageBox.Yes)
        sys.exit()
    def cancel1(self):
        sys.exit()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(720, 576)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 30))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.ip = QtWidgets.QLineEdit(Form)
        self.ip.setMinimumSize(QtCore.QSize(0, 31))
        self.ip.setObjectName("ip")
        self.horizontalLayout_2.addWidget(self.ip)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(22, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.port = QtWidgets.QLineEdit(Form)
        self.port.setMinimumSize(QtCore.QSize(0, 31))
        self.port.setObjectName("port")
        self.horizontalLayout.addWidget(self.port)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)
        self.cancel = QtWidgets.QPushButton(Form)
        self.cancel.setObjectName("cancel")
        self.gridLayout.addWidget(self.cancel, 3, 1, 1, 1)
        self.test = QtWidgets.QPushButton(Form)
        self.test.setObjectName("test")
        self.gridLayout.addWidget(self.test, 4, 1, 1, 1)
        self.save = QtWidgets.QPushButton(Form)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 5, 1, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)



        #第二初始化
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.ip.setGraphicsEffect(op)
        op = QtWidgets.QGraphicsOpacityEffect()
        op.setOpacity(0.5)
        self.port.setGraphicsEffect(op)
        self.port.setText(portset)
        self.ip.setText(ipset)

        #按键绑定
        self.test.clicked.connect(self.testserver)
        self.save.clicked.connect(self.save1)
        self.cancel.clicked.connect(self.cancel1)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.comboBox.setItemText(0, _translate("Form", "共享工作站"))
        self.comboBox.setItemText(1, _translate("Form", "私有工作站"))
        self.label.setText(_translate("Form", "服务器地址"))
        self.label_2.setText(_translate("Form", "  端口"))
        self.cancel.setText(_translate("Form", "取消"))
        self.test.setText(_translate("Form", "测试"))
        self.save.setText(_translate("Form", "保存"))


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    loginapp = QApplication(sys.argv)
    ex = Ui_chooseserver()
    ex.show()
    sys.exit(loginapp.exec_())
