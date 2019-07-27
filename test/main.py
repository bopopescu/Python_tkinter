# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :        Mr.Zhang
   date：          2019/7/22 0022
-------------------------------------------------
   Change Activity:
                   2019/7/22 0022:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'

# from tkinter import *
# from LoginPage import *
#
# root = Tk()
# root.title('小程序')
# LoginPage(root)
# root.mainloop()


from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import *

from test.login import *  # 由.UI文件生成.py文件后，导入创建的GUI类

from test.homepage import *  # Main.py为 主窗口代码文件

# from class_MSSQL import MSSQL


# QtWidgets.QMainWindow：继承该类方法
class Login_window(QtWidgets.QMainWindow, Ui_MainWindow):

    # __init__: 析构函数，也就是类被创建后就会预先加载的项目。
    # 马上运行，这个方法可以用来对你的对象做一些你希望的初始化。
    def __init__(self):
        # 这里需要重载一下Login_window，同时也包含了QtWidgets.QMainWindow的预加载项。
        super(Login_window, self).__init__()
        self.setupUi(self)

        # 将点击事件与槽函数进行连接
        self.landingBT.clicked.connect(self.btn_login_fuc)

        # 登录按钮 函数

    def btn_login_fuc(self):
        # 1 获取输入的账户和密码
        # account = self.txt_1.text()  # 记得text要打括号（）！
        # password = self.txt_2.text()
        # if account == "" or password == "":
        #     reply = QMessageBox.warning(self, "警告", "账号密码不能为空，请输入！")
        #     return

        # 2 查询数据库，判定是否有匹配
        # ms = MSSQL()
        # result = ms.Login_result(account, password)
        # if (len(result) > 0):
            # 1打开新窗口
            print('3123')
            Ui_MainWindow1.show()
            # 2关闭本窗口
        #     self.close()
        # else:
            reply = QMessageBox.warning(self, "警告", "账户或密码错误，请重新输入！")


if __name__ == '__main__':  # 如果这个文件是主程序。
    app = QtWidgets.QApplication(sys.argv)  # QApplication相当于main函数，也就是整个程序（很多文件）的主入口函数。对于GUI程序必须至少有一个这样的实例来让程序运行。
    window = Login_window()  # 生成一个实例（对象）
    Ui_Main = Ui_MainWindow()  # 生成主窗口的实例
    window.show()  # 有了实例，就得让它显示。这里的show()是QWidget的方法，用来显示窗口。
    sys.exit(app.exec_())  # 调用sys库的exit退出方法，条件是app.exec_()也就是整个窗口关闭。
