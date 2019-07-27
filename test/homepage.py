# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '主界面.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sys

class Ui_MainWindow1(object):
    def __init__(self, value=None):
        print(value)
    def setupUi(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow1")
        MainWindow1.resize(436, 300)
        self.dialog = MainWindow1
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(70, 80, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 80, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        # MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 436, 26))
        self.menubar.setObjectName("menubar")
        # MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        # MainWindow1.setStatusBar(self.statusbar)
        #绑定成绩界面
        self.pushButton_2.clicked.connect(self.jump_to_UI_grpy)
        self.retranslateUi(MainWindow1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow1)


    def retranslateUi(self, MainWindow1):
        _translate = QtCore.QCoreApplication.translate
        MainWindow1.setWindowTitle(_translate("MainWindow1", "MainWindow1"))
        self.pushButton.setText(_translate("MainWindow1", "个人信息 "))
        self.pushButton_2.setText(_translate("MainWindow1", "成绩查询"))
    #跳转到成绩页面
    def jump_to_UI_grpy(self):
        self.dialog.close()
    #     app = QApplication(sys.argv)
        #全局设置QPushButton的背景样式
        # dlg = myDialog()
        # dlg.show()
        # dlg.exec_()

if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = Ui_MainWindow1()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())