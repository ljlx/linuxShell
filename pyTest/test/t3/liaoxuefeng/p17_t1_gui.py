#!/usr/bin/python3
# -- coding: utf-8 --
# --------------------------------------------------
# File Name: p17-t1-gui.py
# Author: hanxu
# AuthorSite: https://www.thesunboy.com/
# Created Time: 2018-10-29-下午10:14
# ---------------------说明--------------------------
# Gui编程,只是了解, gui还是要用qt来做,网上推荐的
# 我推荐直接用 web 技术， react 尤其适合，效率比 tk 和 qt 高，且界面 UI 更灵活美观。
# 不过我也觉得还是web更好写,技术通用更强,减少学习成本,而且应用场景好,还灵活些.
# tk 本身動態 py 本身也是動態 二者組合起來程式一大 就慢上加慢
# Qt + py 能有 C++的速度， py 的優雅語法方便性，二者結合很搭。
# Qt 本身的庫大了點..
# 但我試過用 c#、 java 、 pyqt 都寫個小程式 來試 啟動速度
# 原本我以為 C#和 java 應該會較快，但結果出乎我預料之外，三者的啟動速度差不多，我沒實測時間
# c#和 java 跑 GUI 應該也是要載入蠻大的庫，所以沒辦法像 Notepad++ 那種啟動速度那麼快
# 用 Qt 我覺得有一個很大優點，也是不用 拖拉方式，直接手寫也很好寫，現在再寫都不用拖拉視窗介面的方式來寫了
# 推薦 Qt
# ---------------------------------------------------
# Python支持多种图形界面的第三方库，包括：
#
# Tk
#
# wxWidgets
#
# Qt
#
# GTK

import tkinter.messagebox as tmessagebox
from tkinter import *


def test():
    btn1.quit()
    print("test,hello")


# 在GUI中，每个Button、Label、输入框等，都是一个Widget。Frame则是可以容纳其他Widget的Widget，所有的Widget组合起来就是一棵树

class demoApplication(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master=None)
        self.setvar('width', 100)
        self.pack()

    # pack()方法把Widget加入到父容器中，并实现布局。pack()是最简单的布局，grid()可以实现更复杂的布局。
    def createWidgets(self):
        self.hellolable1 = Label(self, text='hello,world')
        self.hellolable1.pack()
        testkw = {"text": 'quit', 'command': self.quit}
        testkw['height'] = 5
        testkw['width'] = 5
        self.quitbutton = Button(self, testkw)
        self.quitbutton['text'] = 'clickme.'
        self.quitbutton.pack()

    def inputText(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertBtn1 = Button(self, text='hello,input', command=self.helloAlertinput)
        self.alertBtn1.pack()

    def caculateInp(self):
        self.caculateInput = Entry(self)
        self.caculateInput.pack()
        self.execaculbtn = Button(self, text='计算', command=self.execacul)
        self.execaculbtn.pack()

    def execacul(self):
        cainput = self.caculateInput.get() or '0'
        tmessagebox.showinfo('resault', eval(cainput))

    def helloAlertinput(self):
        name = self.nameInput.get() or "none input text"
        tmessagebox.showinfo('infoMsg', 'hello,%s' % name)
        tmessagebox.showerror('info-error', 'hello,%s' % name)


app = demoApplication()
app.inputText()
app.caculateInp()
app.master.title('hello,gui,py')
for item in range(0, 2):
    app.createWidgets()

app.mainloop()
app.destroy()
app.quit()
app.pack_forget()

win = Tk()
win.title('title')
win.geometry('200x200')

Label(win, text='hello').place(x=10, y=10)
Button(win, text='1', command=test).place(x=10, y=30)
Button(win, text='2', command=test).place(x=25, y=30)
Button(win, text='3', command=test).place(x=45, y=30)


def test1():
    btn1.quit()


btn1 = Button(win, text='quit', command=test)
btn1.pack()

win.mainloop()
