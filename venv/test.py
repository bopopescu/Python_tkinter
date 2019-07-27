'''5.验证输入的内容是否符合要求。
Entry 组件是支持验证输入内容的合法性的，比如要求输入数字，你输入了字母那就是非法。
实现该功能，需要通过设置 validate、validatecommand 和 invalidcommand 选项。
首先启用验证的“开关”是 validate 选项，该选项可以设置的值有：
focus:当 Entry 组件获得或失去焦点的时候验证
focusin: 当 Entry 组件获得焦点的时候验证
focusout: 当 Entry 组件失去焦点的时候验证
key:当输入框被编辑的时候验证
all: 当出现上边任何一种情况的时候验证
其次是为 validatecommand 选项指定一个验证函数，该函数只能返回 True 或 False 表示验证的结果。
一般情况下验证函数只需要知道输入框的内容即可，可以通过 Entry 组件的 get() 方法获得该字符串。
然后，invalidcommand 选项指定的函数只有在 validatecommand 的返回值为 False 的时候才被调用。
'''
from tkinter import *

root = Tk()
e = StringVar()


def validateText():
    val = entry.get()
    if val == '654321':
        print("正确!")
        return True
    else:
        '''
        删除内容,-- 删除参数 first 到 last 范围内（包含 first 和 last）的所有内容
        -- 如果忽略 last 参数，表示删除 first 参数指定的选项
        -- 使用 delete(0, END) 实现删除输入框的所有内容
       '''
        entry.delete(0, END)
        return False


def test():
    print('invalidcommand:我被调用了')
    return True


entry = Entry(root, textvariable=e, validate='focusout', validatecommand=validateText, invalidcommand=test)
entry.pack()
Entry(root, text='sure').pack()
root.mainloop()
# 还有其他的属性fg/bg/relief/width/height/justify/state使用方法与Button相同，不再举例。