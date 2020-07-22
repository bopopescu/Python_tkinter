# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     view
   Description :
   Author :        Mr.Zhang
   date：          2019/7/22 0022
-------------------------------------------------
   Change Activity:
                   2019/7/22 0022:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'

from tkinter import *
from tkinter.messagebox import *


class InputFrame(Frame):  # 继承Frame类
    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.root = main  # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):
        Label(self).grid(row=0, stick=W, pady=10)
        Label(self, text='药品名称: ').grid(row=1, stick=W, pady=10)
        Entry(self, textvariable=self.itemName).grid(row=1, column=1, stick=E)
        Label(self, text='进价 /元: ').grid(row=2, stick=W, pady=10)
        Entry(self, textvariable=self.importPrice).grid(row=2, column=1, stick=E)
        Label(self, text='售价 /元: ').grid(row=3, stick=W, pady=10)
        Entry(self, textvariable=self.sellPrice).grid(row=3, column=1, stick=E)
        Label(self, text='优惠 /元: ').grid(row=4, stick=W, pady=10)
        Entry(self, textvariable=self.deductPrice).grid(row=4, column=1, stick=E)
        Button(self, text='录入').grid(row=6, column=1, stick=E, pady=10)


class QueryFrame(Frame):  # 继承Frame类
    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.root = main  # 定义内部变量root
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text='查询界面').pack()


class CountFrame(Frame):  # 继承Frame类
    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.root = main  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='统计界面').pack()


class AboutFrame(Frame):  # 继承Frame类
    def __init__(self, main=None):
        Frame.__init__(self, main)
        self.root = main  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='关于界面').pack()