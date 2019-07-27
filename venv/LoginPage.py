#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     LoginPage
   Description :
   Author :        Mr.Zhang
   date：          2019/7/24 0024
-------------------------------------------------
   Change Activity:
                   2019/7/24 0024:
-------------------------------------------------
"""
__author__ = 'Mr.Zhang'

# 引用tkinter并取名tk
import tkinter as tk
from tkinter.messagebox import *
import MyDButils
from HomePage import *
from PIL import Image, ImageTk
# 定义类
class LoginPage(object):
    # 初始化
    def __init__(self, master=None):
        # 我们需要一个 root 控件, 即根窗口, 它包括标题栏和其他一些由本地窗口系统提供的装饰. root 控件需要在创建其他控件前创建, 并且一个窗口只能有一个 root 控件.
        self.root = master
        # 窗口大小
        self.root.geometry('600x450')
        # 设置两个变量
        self.username = tk.StringVar()
        self.password = tk.StringVar()
        # 使用展示页面方法
        self.loginPage()

    # 定义createPage方法
    def loginPage(self):
        # 创建一个表单self.page
        self.page = tk.Frame(self.root)
        # 将表单self.page展示
        self.page.pack()
        # 为表单添加内容
        # 添加三个个空行：为了界面排版
        tk.Label(self.page).grid(row=0, stick=tk.W)
        tk.Label(self.page).grid(row=1, stick=tk.W)
        tk.Label(self.page,text='学生管理系统').grid(row=2, pady=10,sticky=tk.W)
        tk.Label(self.page).grid(row=3, stick=tk.W)
        # 第四行  拥有两个控件一个Label和Entry
        tk.Label(self.page, text='账户：').grid(row=4, pady=10, stick=tk.W)
        tk.Entry(self.page, textvariable=self.username).grid(row=4, column=1, stick=tk.E)
        # 第五行  拥有两个控件一个Label和Entry
        tk.Label(self.page, text='密码：').grid(row=5, pady=10, stick=tk.W)
        tk.Entry(self.page, textvariable=self.password, show='*').grid(row=5, column=1, stick=tk.E)
        tk.Label(self.page).grid(row=6, stick=tk.W)
        tk.Button(self.page, text='登陆', command=self.loginCheck).grid(row=7, stick=tk.W, pady=10)
        tk.Button(self.page, text='注册', command=self.registPage).grid(row=7, column=1, stick=tk.E)

    def loginCheck(self):
        # 获取用户输入的数据
        username = self.username.get()
        password = self.password.get()
        if username == '':
            showinfo(title='错误', message='账号不能为空！')
        elif password =='':
            showinfo(title='错误', message='密码不能为空！')
        else:
            # 将用户名密码装入list
            values = (username,password)
            # 调用连接池
            cursor = MyDButils.utils_db(param=pymysql.cursors.DictCursor)
            # sql语句
            sql = 'SELECT * FROM shazam.tb_student where stuNo = %s and password =%s'
            # 执行sql语句,并获得结果集
            result = cursor.getOne(sql, values)
            if result:
                self.page.destroy()
                HomePage(self.root,result['stuNo'])
            else:
                showinfo(title='错误', message='用户名或密码错误！')

    def registPage(self):
        def sign_to_sava():
            # 获取密码
            np = new_pwd.get()
            # 确认密码
            npf = new_pwd_confirm.get()
            # 获取用户名
            nn = new_name.get()
            # 获取学号
            ns = new_stuNo.get()
            values = (ns, np ,nn)
            # 判断用户输入是否为空
            if ''in values:
                showerror('Error', '学号、姓名和密码不能为空! ')
                return None
            # 判断两次密码是否一样
            if np != npf:
                showerror('Error', '两次密码不一致，请重试! ')
                return None
            # 调用数据库连接池
            mysql = MyDButils.utils_db()
            # sql语句
            sql = 'SELECT * FROM shazam.tb_student where stuNo = %s '
            result = mysql.getOne(sql,ns)
            # 判断用户名是否存在
            if result:
                showerror('Error', '该学号已经被注册! ')
                return None
            else:
                sql = "INSERT INTO shazam.tb_student (stuNo, password, name) values (%s, %s, %s)"
                result = mysql.insertOne(sql,values)
                if result:
                    showinfo('success', '注册成功！')
                else:
                    showinfo('Error', '服务器繁忙，请稍后重试！')


        window_sign_up = tk.Toplevel()
        window_sign_up.geometry('350x230')
        window_sign_up.title('注册')

        new_stuNo = tk.StringVar()
        tk.Label(window_sign_up, text='学号:').place(x=10, y=10)
        entry_new_stuNo = tk.Entry(window_sign_up, textvariable=new_stuNo)
        entry_new_stuNo.place(x=150, y=10)

        new_name = tk.StringVar()
        tk.Label(window_sign_up, text='姓名:').place(x=10, y=50)
        entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
        entry_new_name.place(x=150, y=50)

        new_pwd = tk.StringVar()
        tk.Label(window_sign_up, text='密码:').place(x=10, y=90)
        entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
        entry_usr_pwd.place(x=150, y=90)

        new_pwd_confirm = tk.StringVar()
        tk.Label(window_sign_up, text='确认密码:').place(x=10, y=130)
        entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
        entry_usr_pwd_confirm.place(x=150, y=130)

        btn_comfirm_sign_up = tk.Button(window_sign_up, text='注册', command=sign_to_sava)
        btn_comfirm_sign_up.place(x=150, y=170)

if __name__ == '__main__':
    root = tk.Tk()
    LoginPage(root)
    root.title("学生管理系统")
    root.mainloop()