#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     MainPage
   Description :
   Author :        Mr.Zhang
   date：          2019/7/24 0024
-------------------------------------------------
   Change Activity:
                   2019/7/24 0024:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'
from tkinter import *
from views import *
class HomePage(object):
    def __init__(self, master=None, stuNo=None):
        self.stuNo = stuNo
        self.root = master
        self.root.geometry('600x450')
        self.createPage()

    def createPage(self):
        self.per_details = Per_details(self.root, self.stuNo)
        self.query_results = Query_results(self.root, self.stuNo)
        self.per_details.pack()
        menubar = Menu(self.root)
        menubar.add_command(label='个人信息', command=self.per_details_show)
        menubar.add_command(label='成绩查询', command=self.query_results_show)
        self.root['menu'] = menubar  # 设置菜单栏

    def per_details_show(self):
        self.per_details.pack()
        self.query_results.pack_forget()

    def query_results_show(self):
        self.per_details.pack_forget()
        self.query_results.pack()
