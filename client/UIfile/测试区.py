from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QPushButton, QMenu, QLineEdit, QMainWindow, QLabel
from PyQt5.QtCore import QCoreApplication, QTimer, QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPainter, QPixmap, QPalette, QBrush
import sys

# 基本五大包导入

# 以下为导入功能包


# 以下为导入自定义函数
# 工具箱


class Ui_Dialog(object):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "PushButton"))


if __name__ == '__main__':  # 调试用启动器
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    Imapp = QApplication(sys.argv)
    ex = Ui_Dialog()
    ex.show()
    sys.exit(Imapp.exec_())
