# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '登陆界w面.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
import sys
from test import homepage as home


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(511, 249)
        self.form = MainWindow
        font = QtGui.QFont()
        font.setPointSize(2)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.passwordLB = QtWidgets.QLabel(self.centralwidget)
        self.passwordLB.setGeometry(QtCore.QRect(50, 60, 72, 15))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.passwordLB.setFont(font)
        self.passwordLB.setObjectName("passwordLB")
        self.accountLB = QtWidgets.QLabel(self.centralwidget)
        self.accountLB.setGeometry(QtCore.QRect(50, 20, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.accountLB.setFont(font)
        self.accountLB.setObjectName("accountLB")
        self.landingBT = QtWidgets.QPushButton(self.centralwidget)
        self.landingBT.setGeometry(QtCore.QRect(160, 120, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.landingBT.setFont(font)
        self.landingBT.setObjectName("landingBT")
        self.accountTE = QtWidgets.QTextEdit(self.centralwidget)
        self.accountTE.setGeometry(QtCore.QRect(120, 20, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.accountTE.setFont(font)
        self.accountTE.setObjectName("accountTE")
        self.passwordTE = QtWidgets.QTextEdit(self.centralwidget)
        self.passwordTE.setGeometry(QtCore.QRect(120, 50, 221, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.passwordTE.setFont(font)
        self.passwordTE.setObjectName("passwordTE")
        self.regeditCLB = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.regeditCLB.setGeometry(QtCore.QRect(290, 90, 201, 41))
        icon = QtGui.QIcon.fromTheme("01")
        self.regeditCLB.setIcon(icon)
        self.regeditCLB.setIconSize(QtCore.QSize(0, 0))
        self.regeditCLB.setObjectName("regeditCLB")
        self.retrievepasswordCLB = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.retrievepasswordCLB.setGeometry(QtCore.QRect(290, 140, 201, 41))
        icon = QtGui.QIcon.fromTheme("01")
        self.retrievepasswordCLB.setIcon(icon)
        self.retrievepasswordCLB.setIconSize(QtCore.QSize(0, 0))
        self.retrievepasswordCLB.setObjectName("retrievepasswordCLB")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 511, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.toolBar_2 = QtWidgets.QToolBar(MainWindow)
        self.toolBar_2.setObjectName("toolBar_2")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)

        # 绑定事件
        self.landingBT.clicked.connect(self.jump_to_UI_grpy)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.passwordLB.setText(_translate("MainWindow", "密码"))
        self.accountLB.setText(_translate("MainWindow", "账户"))
        self.landingBT.setText(_translate("MainWindow", "登陆"))
        self.regeditCLB.setText(_translate("MainWindow", "注册账号>>>"))
        self.retrievepasswordCLB.setText(_translate("MainWindow", "找回密码>>>"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.toolBar_2.setWindowTitle(_translate("MainWindow", "toolBar_2"))


    def jump_to_UI_grpy(self):
        # self.landingBT.clicked.connect(self.jump_to_UI_grpy)
        print("开始")
        self.form.hide()
        form1 = QtWidgets.QDialog()
        ui = home.Ui_MainWindow1(value='123')
        ui.setupUi(form1)
        form1.show()
        form1.exec_()
        print("结束")
        self.form.show()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())
