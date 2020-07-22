#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     views
   Description :
   Author :        Mr.Zhang
   date：          2019/7/24 0024
-------------------------------------------------
   Change Activity:
                   2019/7/24 0024:
-------------------------------------------------
"""
from MyDButils import *
from tkinter import *
from tkinter.messagebox import *
import operator
__author__ = 'Mr.Zhang'
# 个人信息界面
class Per_details(Frame):
    # 初始化
    def __init__(self, main=None, stuNo=None):
        Frame.__init__(self,main) #Fram初始化
        self._root = main
        # self.stuNo.set("sdfsdf")
        # 定义展示数据
        self.stuNo = StringVar()
        self.name = StringVar()
        self.password = StringVar()
        self.idCard = StringVar()
        self.sex = StringVar()
        self.education = StringVar()
        self.professional = StringVar()
        self.acceptanceDate = StringVar()
        self.birthday = StringVar()
        self.tel = StringVar()
        self.email = StringVar()
        self.address = StringVar()
        self.classId = StringVar()
        self.Assignment(stuNo)
        self.creatPage()

    # 充填数据
    def Assignment(self, stuNo=None):
        # sql语句
        sql = "select * from shazam.tb_student where stuNo = %s"
        # 执行
        result = utils_db(pymysql.cursors.DictCursor).getOne(sql, stuNo)
        print(result)
        self.stuNo.set(result['stuNo'])
        self.password.set(result['password'])
        self.name.set(result['name'])
        self.idCard.set(result['idCard'])
        self.sex.set(result['sex'])
        self.education.set(result['education'])
        self.professional.set(result['professional'])
        self.acceptanceDate.set(result['acceptanceDate'])
        self.birthday.set(result['birthday'])
        self.tel.set(result['tel'])
        self.address.set(result['address'])
        self.classId.set(result['classId'])
        self.email.set(result['email'])
    # 创建页面
    def creatPage(self):
        self.old_values = []
        # 定义保存方法
        def save():
            print(self.old_values)
            if button['text'] == '修改信息':
                button['text'] = '保存信息'
                for state in entry:
                    state['state'] = 'normal'
                    self.old_values.append(state.get())
            else:
                button['text'] = '修改信息'
                new_values = []
                for state in entry:
                    state['state'] = 'readonly'
                    new_values.append(state.get())
                print(new_values)
                if operator.eq(self.old_values,new_values):
                    showinfo(title='waring', message='您未做任何修改！')
                else:
                    new_values.append(self.stuNo.get())
                    sql = "UPDATE `shazam`.`tb_student` SET `stuNo`=%s, `name`=%s, `password`=%s, `idCard`=%s, `sex`=%s, `education`=%s, `professional`=%s, `acceptanceDate`=%s, `birthday`=%s, `tel`=%s, `email`=%s, `address`=%s, `classId`=%s WHERE `stuNo`=%s"
                    result = utils_db(pymysql.cursors.DictCursor).update(sql, new_values)
                    if result:
                        showinfo(title='成功', message='保存成功！')
                    else:
                        showinfo(title='失败', message='服务器繁忙，请稍后重试！')
                self.old_values = []
        # 创建控件
        # label
        label1 = Label(self, text='学号：')
        label2 = Label(self, text='姓名：')
        label3 = Label(self, text='密码：')
        label4 = Label(self, text='身份证：')
        label5 = Label(self, text='性别：')
        label6 = Label(self, text='学历：')
        label7 = Label(self, text='专业：')
        label8 = Label(self, text='入学日期：')
        label9 = Label(self, text='出生日期：')
        label10 = Label(self, text='联系电话：')
        label11 = Label(self, text='电子邮箱：')
        label12 = Label(self, text='家庭住址：')
        label13 = Label(self, text='班级：')
        label = (label1, label2, label3, label4, label5, label6, label7, label8, label9, label10, label11, label12, label13)
        # entry(textvariable='内容',state='状态只读')
        self.__state__ = 'readonly'
        entry1 = Entry(self, textvariable=self.stuNo, state=self.__state__)
        entry2 = Entry(self, textvariable=self.name, state=self.__state__)
        entry3 = Entry(self, textvariable=self.password, state=self.__state__,show='*')
        entry4 = Entry(self, textvariable=self.idCard, state=self.__state__)
        entry5 = Entry(self, textvariable=self.sex, state=self.__state__)
        entry6 = Entry(self, textvariable=self.education, state=self.__state__)
        entry7 = Entry(self, textvariable=self.professional, state=self.__state__)
        entry8 = Entry(self, textvariable=self.acceptanceDate, state=self.__state__)
        entry9 = Entry(self, textvariable=self.birthday, state=self.__state__)
        entry10 = Entry(self, textvariable=self.tel, state=self.__state__)
        entry11 = Entry(self, textvariable=self.email, state=self.__state__)
        entry12 = Entry(self, textvariable=self.address, state=self.__state__)
        entry13 = Entry(self, textvariable=self.classId, state=self.__state__)
        entry = [entry1, entry2, entry3, entry4, entry5, entry6, entry7, entry8, entry9, entry10, entry11, entry12, entry13]
        # button
        button = Button(self, text='修改信息', command=save)
        # 对控件进行布局
        Label(self, text='个人信息').grid(column=3)
        # 第一行
        label1.grid(row=1, stick=W, column=1, pady=10)
        entry1.grid(row=1, stick=E, column=2)
        label2.grid(row=1, stick=W, column=3, pady=10)
        entry2.grid(row=1, stick=E, column=4)
        # 第二行
        label3.grid(row=2, stick=W, column=1, pady=10)
        entry3.grid(row=2, stick=E, column=2)
        label4.grid(row=2, stick=W, column=3, pady=10)
        entry4.grid(row=2, stick=E, column=4)
        # 第三行
        label5.grid(row=3, stick=W, column=1, pady=10)
        entry5.grid(row=3, stick=E, column=2)
        label6.grid(row=3, stick=W, column=3, pady=10)
        entry6.grid(row=3, stick=E, column=4)
        # 第四行
        label7.grid(row=4, stick=W, column=1, pady=10)
        entry7.grid(row=4, stick=E, column=2)
        label8.grid(row=4, stick=W, column=3, pady=10)
        entry8.grid(row=4, stick=E, column=4)
        # 第五行
        label9.grid(row=5, stick=W, column=1, pady=10)
        entry9.grid(row=5, stick=E, column=2)
        label10.grid(row=5, stick=W, column=3, pady=10)
        entry10.grid(row=5, stick=E, column=4)
        # 第六行
        label11.grid(row=6, stick=W, column=1, pady=10)
        entry11.grid(row=6, stick=E, column=2)
        label12.grid(row=6, stick=W, column=3, pady=10)
        entry12.grid(row=6, stick=E, column=4)
        # 第七行
        label13.grid(row=7, stick=W, column=1, pady=10)
        entry13.grid(row=7, stick=E, column=2)
        button.grid(row=7, column=4, stick=E, pady=10)

# 成绩查询页面
class Query_results(Frame):
    def __init__(self, main=None, stuNo=None):
        Frame.__init__(self, main)
        self.root = main
        self.stuNo = stuNo
        # 获取数据
        self.Assignment()
        # 填充页面
        self.CreatePage()

    # 获取数据
    def Assignment(self):
        sql = 'select coutseName,result,semester from tb_course,tb_results where tb_course.courseId = tb_results.courseId and tb_results.stuNo=%s'
        self.result = utils_db().getAll(sql, self.stuNo)
        print(self.result)
    # 填充页面
    def CreatePage(self):
        Label(self, text='科目名称').grid(row=0, column=1, padx=5, pady=5, ipadx=5, ipady=5)
        Label(self, text='分数').grid(row=0, column=2, padx=5, pady=5, ipadx=5, ipady=5)
        Label(self, text='学期').grid(row=0, column=3, padx=5, pady=5, ipadx=5, ipady=5)
        if self.result:
            for i in range(len(self.result)):
                for j in range(len(self.result[0])):
                    Label(self, text=self.result[i][j]).grid(row=i + 1, column=j + 1, padx=10, pady=10, ipadx=10, ipady=10)




if __name__ == '__main__':
    from HomePage import *
    root = Tk()
    root.title('学生管理系统')
    HomePage(root)
    root.mainloop()