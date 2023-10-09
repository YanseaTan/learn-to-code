#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
# refer ~ Python GUI Programming Cookbook Third Edition

"""Tkinter乃至更多的GUI库如何学习、应用"""

import tkinter as tk
# The ttk module has some advanced widgets such as a notebook,
# progress bar, labels, and buttons that look different.
# The name ttk stands for themed tk. The tk-themed widget set
# was introduced in Tk 8.5.
from tkinter import ttk


# 1. 窗口如何创建
def min_win():
    # 创建主窗口（顶层容器）
    win = tk.Tk()
    win.title("My Tkinter Window")
    # 添加另一个组件到主窗口，组件构造器第一个参数为父容器
    lab = ttk.Label(win, text="My Label")
    lab.pack()
    win.mainloop()


# 2. 布局如何处理
def about_layout():
    win = tk.Tk()
    win.title('布局尝试')

    # Preventing the GUI from being resized
    # 是否允许resize（X、Y两个方向）
    # win.resizable(False, True)
    win.resizable(True, True)

    # Arranging several labels within a label frame widget
    lab_frame = ttk.LabelFrame(win, text='My Label Frame')
    lab_frame.grid(column=0, row=0)
    tk.Label(lab_frame, text='test label 1').grid(column=0, row=0)
    tk.Label(lab_frame, text='test label 2').grid(column=0, row=1)
    tk.Label(lab_frame, text='test label 3').grid(column=0, row=2)
    # 同样的也可以在frame中放别的组件
    tk.Button(lab_frame, text='test button 1').grid(column=0, row=3)

    # Using padding to add space around widgets
    # padx pady 是针对容器左上角的像素距离
    lab_frame.grid(column=0, row=1, padx=20, pady=80)
    # 遍历容器中所有组件，并添加padding
    for child in lab_frame.winfo_children():
        # The grid_configure() function allows us to modify
        # the UI elements before the mainloop displays them
        child.grid_configure(padx=5, pady=6)

    # 三种布局管理器
    """
    pack 按添加顺序排列组件
    grid 按网格坐标排列组件
    place 指定组件大小及位置
    """

    # ttk.Label(win, text="一个标签").grid(column=0, row=0)
    def _pack():
        _win = tk.Tk()
        ttk.Label(_win, text='pack layout').pack(side=tk.BOTTOM)
        _win.mainloop()

    def _place():
        _win = tk.Tk()
        ttk.Label(_win, text='place layout').place(x=50, y=50, anchor=tk.NW)
        _win.mainloop()

    # _pack()
    # _place()
    win.mainloop()

    # 更详细的布局手段，参考具体接口参数


# 3. 组件支持哪些
def about_component():
    win = tk.Tk()

    # 菜单组件
    # create a menu bar
    menu_bar = tk.Menu(win)
    win.config(menu=menu_bar)
    # create menu and add menu items
    file_menu = tk.Menu(menu_bar)
    file_menu.add_command(label='New File')
    # add the menu to the menu bar
    menu_bar.add_cascade(label="File", menu=file_menu)
    # 以上添加菜单的逻辑有点...
    # If this tkinter menu bar syntax seems a little bit confusing, don't worry.
    # This is just the syntax of tkinter for creating a menu bar. It isn't very Pythonic.

    # 更多组件参考文档
    # 一篇总结： https://blog.csdn.net/explorer9607/article/details/82783470

    win.mainloop()


# 4. 参数透传与事件处理
def about_args_and_callback():
    """
    tkinter定义了几种数据类型用于处理数据：
        strVar = StringVar()
        intVar = IntVar()
        dbVar = DoubleVar()
        blVar = BooleanVar()
    通用事件绑定的方法：
        widget.bind("<event>",func)
            <event>：字符串参数，表示事件类型，需使用“尖括号”包裹
            func：回调函数，触发事件时，Tk会携带事件对象（Event）调用func
        具体事件类型参考相关文档
    """
    win = tk.Tk()
    input_ = tk.StringVar()
    input_box = ttk.Entry(win, width=20, textvariable=input_)
    input_box.pack(side=tk.LEFT)

    def button_func(event):
        print("发生事件的组件为：" + str(event.widget))
        print("事件类型为：" + str(event.type))
        in_str = input_box.get()
        print('[input] ' + in_str) if in_str != '' else print('[debug] !empty input')

    btn = ttk.Button(win, text='Aha!')
    btn.bind('<Button-1>', button_func)
    btn.pack(side=tk.RIGHT)

    win.mainloop()


# 5. 样式如何调整
def about_look():
    pass


if __name__ == '__main__':
    # min_win()
    # about_layout()
    # about_component()
    about_args_and_callback()
