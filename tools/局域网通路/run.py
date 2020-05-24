# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QLineEdit, QMainWindow, QWidget,QSystemTrayIcon,QAction,QMenu
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush
import sys, os, configparser,time

# 基本五大包导入


# PyQt5.QtWidgets import*
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# 以下为导入功能包
import socket
import json
import hashlib
import time
import ctypes
filename="./1.txt"
filemt=""
state=0
class Ui_New(QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi()
    def about(self):
        sys.exit()

    def see(self):
        path=os.path.abspath(filename)
        os.startfile(path)
        self.tp.setIcon(QIcon('./nothing_logo.jpg'))
        tpMenu = QMenu()
        a1 = QAction(QtGui.QIcon('exit.png'), u'退出', self)  # 添加一级菜单动作选项(关于程序)
        a1.triggered.connect(self.about)
        tpMenu.addAction(a1)
        self.tp.setContextMenu(tpMenu)
        self.work()
    def work(self):
        global filemt
        while 1:
            time.sleep(10)
            if time.localtime(os.stat(filename).st_mtime)!=filemt:
                filemt = time.localtime(os.stat(filename).st_mtime)
                print(filemt)
                self.tp.setIcon(QIcon('./Yes_logo.jpg'))
                tpMenu = QMenu()
                a1 = QAction(QtGui.QIcon('exit.png'), u'查看', self)  # 添加一级菜单动作选项(关于程序)
                a1.triggered.connect(self.see)
                tpMenu.addAction(a1)
                self.tp.setContextMenu(tpMenu)
                break

    def setupUi(self):
        global filemt
        self.resize(250, 250)
        # move()方法移动了窗口到屏幕坐标x=300, y=300的位置.
        self.move(300, 300)
        # 在这里我们设置了窗口的标题.标题会被显示在标题栏上.
        self.setWindowTitle('Simple')
        # show()方法将窗口显示在屏幕上.一个窗口是先在内存中被创建,然后显示在屏幕上的.
        #self.show()
        print(1)
        self.tp = QSystemTrayIcon(self)
        self.tp.setIcon(QIcon('./nothing_logo.jpg'))
        self.tp.setToolTip(u'智乃酱真棒(*^▽^*)！')
        self.tp.showMessage('tp', 'tpContent')
        tpMenu = QMenu()
        a1 = QAction(QtGui.QIcon('exit.png'), u'退出', self)  # 添加一级菜单动作选项(关于程序)
        a1.triggered.connect(self.about)
        tpMenu.addAction(a1)
        self.tp.setContextMenu(tpMenu)
        self.tp.show()
        filemt = time.localtime(os.stat(filename).st_mtime)
        print(filemt)
        #self.tp.messageClicked.connect(self.message)
        self.work()


if __name__ == '__main__':  # 调试用启动器
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    Newapp = QApplication(sys.argv)
    ex = Ui_New()
    #ex.show()
    sys.exit(Newapp.exec_())