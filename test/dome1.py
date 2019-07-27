import tkinter as tk
import pymysql
import tkinter.messagebox

window = tk.Tk()
window.title('Welcome to My System')
window.geometry('450x300')

# 背景图片
canvas = tk.Canvas(window, height=300, width=700)
image_file = tk.PhotoImage(file='fdf.gif')
image = canvas.create_image(0, 0, anchor='nw', image=image_file)
canvas.pack(side='top')

# 窗口信息
tk.Label(window, text='User name:').place(x=50,y=150)
tk.Label(window, text='Password:').place(x=50,y=190)

var_usr_name = tk.StringVar()
entry_use_name = tk.Entry(window, textvariable=var_usr_name)
entry_use_name.place(x=160,y=150)
var_usr_pwd = tk.StringVar()
entry_use_pwd = tk.Entry(window, textvariable=var_usr_pwd, show='*')
entry_use_pwd.place(x=160,y=190)

# 设计登录按钮事件
def usr_login(a, b, c):
    print(a, b, c)
    # 获取文本框的账户信息
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    # 连接数据库
    db = pymysql.connect("localhost", "awesome", "awesome123", "awesome")
    # 创建游标，并设定返回值类型为字典“cursor=pymysql.cursors.DictCursor”
    cursor = db.cursor(cursor=pymysql.cursors.DictCursor)# 返回字典格式数据
    # sql语句
    sql = 'select * from user where username = "%s"' % (usr_name)
    print(sql)
    # 执行sql语句
    cursor.execute(sql)
    # 关闭连接
    cursor.close()
    db.close()
    # 结果集
    data = cursor.fetchall()
    # print(data[0]['passwd'])
    print(data)
    # 判断用户名是否存在
    if data:
        # 存在时，判断密码是否正确
        if data[0]['password'] == usr_pwd:
            tk.messagebox.showinfo(title='Hi', message='Hello:'+usr_name)
        else:
            tk.messagebox.showerror(message="Error, your password is wrong, try again! ")
    # 不存在时
    else:
        # 告知用户是否注册
        is_sign_up = tk.messagebox.askyesno('Welcome','You have not sign up yet. Sign uo now? ')
        if is_sign_up:
            # 调用注册按钮事件
            usr_sign_up()

# 设计注册按钮事件
def usr_sign_up():
    def sign_to_sava():
        # 获取密码
        np = new_pwd.get()
        # 确认密码
        npf = new_pwd_confirm.get()
        # 获取用户名
        nn = new_name.get()
        # 连接数据库
        db = pymysql.connect("localhost", "awesome", "awesome123", "awesome")
        # 创建游标，并设定返回值类型为字典“cursor=pymysql.cursors.DictCursor”
        cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  # 返回字典格式数据
        # sql语句
        sql = 'select * from user where username = "%s"' % (nn)
        print(sql)
        # 执行sql语句
        cursor.execute(sql)
        # 结果集
        data = cursor.fetchone()
        print(data)
        # 判断用户名是否存在
        if data:
            tk.messagebox.showerror('Error', 'The user has already signed up! ')
        else:
            # 判断两次密码是否一样
            if np != npf:
                tk.messagebox.showerror('Error', 'Password and confirm password must be the same! ')
            else:
                try:
                    sql = "INSERT INTO `awesome`.`user` (`password`, `username`) VALUES ('%s', '%s');" % (np, nn)
                    print(sql)
                    cursor.execute(sql)
                    db.commit()
                    count = cursor.rowcount
                    print(count)
                    # if count:
                    tk.messagebox.showinfo(title='Hi', message='Sign up successful:'+nn)
                # else:
                except:
                    tk.messagebox.showerror('Error', 'Server busy, please try again later!! ')
                cursor.close()
                db.close()

    window_sign_up = tk.Toplevel(window)
    window_sign_up.geometry('350x200')
    window_sign_up.title('Sign up window')

    new_name = tk.StringVar()
    tk.Label(window_sign_up, text='User name:').place(x=10,y=10)
    entry_new_name = tk.Entry(window_sign_up,textvariable=new_name)
    entry_new_name.place(x=150,y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=50)
    entry_usr_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_usr_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text='Password:').place(x=10, y=90)
    entry_usr_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_usr_pwd_confirm.place(x=150, y=90)

    btn_comfirm_sign_up = tk.Button(window_sign_up, text='Sign up',command=sign_to_sava)
    btn_comfirm_sign_up.place(x=150,y=130)

# 登录按钮
btn_login = tk.Button(window, text='Login', command=lambda :usr_login(a=122, b=233, c=344))
btn_login.place(x=170, y=230)
# 注册按钮
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270, y=230)

# 实例化窗口
window.mainloop()