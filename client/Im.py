from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMenu, QLineEdit, QMainWindow, QLabel, QWidget
from PyQt5.QtCore import QCoreApplication, QTimer, QThread, pyqtSignal, Qt, QPoint
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPalette, QBrush, QMouseEvent
import sys


# 基本五大包导入

# 以下为导入功能包


# 以下为导入自定义函数
# 工具箱

class Ui_IM(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def paintEvent(self, event):  # set background_img
        painter = QPainter(self)
        painter.drawRect(self.rect())
        pixmap = QPixmap("./images/Im.jpg")  # 换成自己的图片的相对路径
        painter.drawPixmap(self.rect(), pixmap)

    def off(self):
        exit()

    def min(self):
        self.showMinimized()

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1063, 826)
        Form.setMinimumSize(QtCore.QSize(1024, 0))
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Head = QtWidgets.QPushButton(Form)
        self.Head.setMinimumSize(QtCore.QSize(50, 50))
        self.Head.setText("")
        self.Head.setObjectName("Head")
        self.horizontalLayout.addWidget(self.Head)
        self.username = QtWidgets.QLabel(Form)
        self.username.setObjectName("username")
        self.horizontalLayout.addWidget(self.username)
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setMaximumSize(QtCore.QSize(155, 16777215))
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.horizontalLayout_6.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(150, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.talkButton = QtWidgets.QPushButton(Form)
        self.talkButton.setMinimumSize(QtCore.QSize(50, 50))
        self.talkButton.setText("")
        self.talkButton.setObjectName("talkButton")
        self.horizontalLayout_2.addWidget(self.talkButton)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.toolButton = QtWidgets.QPushButton(Form)
        self.toolButton.setMinimumSize(QtCore.QSize(50, 50))
        self.toolButton.setText("")
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout_2.addWidget(self.toolButton)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.talkButton_3 = QtWidgets.QPushButton(Form)
        self.talkButton_3.setMinimumSize(QtCore.QSize(50, 50))
        self.talkButton_3.setText("")
        self.talkButton_3.setObjectName("talkButton_3")
        self.horizontalLayout_2.addWidget(self.talkButton_3)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.MinimumExpanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.minum = QtWidgets.QPushButton(Form)
        self.minum.setMinimumSize(QtCore.QSize(40, 0))
        self.minum.setText("")
        self.minum.setObjectName("minum")
        self.horizontalLayout_3.addWidget(self.minum)
        self.max = QtWidgets.QPushButton(Form)
        self.max.setMinimumSize(QtCore.QSize(40, 0))
        self.max.setText("")
        self.max.setObjectName("max")
        self.horizontalLayout_3.addWidget(self.max)
        self.offbutton = QtWidgets.QPushButton(Form)
        self.offbutton.setMinimumSize(QtCore.QSize(40, 0))
        self.offbutton.setText("")
        self.offbutton.setObjectName("off")
        self.horizontalLayout_3.addWidget(self.offbutton)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(Form)
        self.textBrowser_2.setMinimumSize(QtCore.QSize(300, 0))
        self.textBrowser_2.setMaximumSize(QtCore.QSize(300, 16777215))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_5.addWidget(self.textBrowser_2)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(650, 191))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_4.addWidget(self.lineEdit_2)
        self.send = QtWidgets.QPushButton(Form)
        self.send.setMinimumSize(QtCore.QSize(50, 25))
        self.send.setMaximumSize(QtCore.QSize(100, 50))
        self.send.setObjectName("send")
        self.horizontalLayout_4.addWidget(self.send)
        self.gridLayout.addLayout(self.horizontalLayout_4, 2, 0, 1, 1)
        self.attach1 = QtWidgets.QPushButton(Form)
        self.attach1.setMinimumSize(QtCore.QSize(50, 50))
        self.attach1.setMaximumSize(QtCore.QSize(50, 16777215))
        self.attach1.setObjectName("attach1")
        self.gridLayout.addWidget(self.attach1, 1, 0, 1, 1)
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setMinimumSize(QtCore.QSize(730, 480))
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.retranslateUi(Form)
        self.offbutton.clicked.connect(lambda: self.off())
        self.minum.clicked.connect(lambda: self.min())
        QtCore.QMetaObject.connectSlotsByName(Form)

    def mouseMoveEvent(self, e: QMouseEvent):  # 重写移动事件
        self._endPos = e.pos() - self._startPos
        self.move(self.pos() + self._endPos)

    def mousePressEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = True
            self._startPos = QPoint(e.x(), e.y())

    def mouseReleaseEvent(self, e: QMouseEvent):
        if e.button() == Qt.LeftButton:
            self._isTracking = False
            self._startPos = None
            self._endPos = None

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.username.setText(_translate("Form", "1233333"))
        self.send.setText(_translate("Form", "发送"))
        self.attach1.setText(_translate("Form", "bak"))


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    Imapp = QApplication(sys.argv)
    ex = Ui_IM()
    ex.show()
    sys.exit(Imapp.exec_())
