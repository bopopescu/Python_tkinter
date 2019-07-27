#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     main
   Description :
   Author :        Mr.Zhang
   date：          2019/7/24 0024
-------------------------------------------------
   Change Activity:
                   2019/7/24 0024:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'

from LoginPage import *
from HomePage import *


def on_closing():
    if askokcancel("退出", "您确定要退出吗？"):
        root.destroy()

root = Tk()
root.title('学生管理系统')
root.protocol("WM_DELETE_WINDOW", on_closing)
LoginPage(root)
root.mainloop()