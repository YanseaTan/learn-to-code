#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
# refer ~ Beginning Python From Novice to Professional Third Edition

import tkinter as tk
from tkinter.scrolledtext import ScrolledText


def main_windows():
    top = tk.Tk()  # top-level component, or widget

    # pack是布局管理器
    # 对控件调用方法pack时，将把控件放在其父控件（主控件 ）中
    #   要指定主控件，可使用构造函数的第一个可选参数
    #   如果没有指定，将把顶级主窗口用作主控件
    btn = tk.Button(top)  # If there is no Tk instance, creating a widget will also instantiate Tk
    btn.pack()

    def button_action():
        # 按钮的动作函数
        print('hello there')

    # btn['text'] = 'A Button!'
    # btn['command'] = button_action
    btn.config(text='a button', command=button_action)  # 使用config方法为控件进行参数配置
    # 也可以通过构造函数直接传入参数
    btn2 = tk.Button(top, text='another button', command=button_action)
    btn2.pack()

    # 没有提供任何参数时，pack从窗口顶部开始将控件堆叠成一列，并让它们在窗口中水平居中
    for i in range(5):
        tk.Label(top, text=f'label {i}').pack()

    # 处理pack外，还有grid及place两种布局管理器
    # 一个容器中最好只使用一众布局管理器，避免混乱

    # 事件处理！！！
    # 上面实践了通过command参数给按钮控件绑定事件函数，这是种特殊的事件绑定方式
    # Tkinter提供的更通用的事件处理机制是：bind方法
    # You call this on the widget you want to handle a given kind of event,
    # specifying the name of the event and a function to use
    def callback_of_mouse_click(event):
        print(event.x, event.y)
    label = tk.Label(top, text='try click here')
    label.pack()
    label.bind('<Button-1>', callback_of_mouse_click)

    top.mainloop()
    # btn.mainloop()


def text_editor():
    def load():
        with open(filename.get()) as file:
            contents.delete('1.0', tk.END)
            contents.insert(tk.INSERT, file.read())

    def save():
        with open(filename.get(), 'w') as file:
            file.write(contents.get('1.0', tk.END))

    top = tk.Tk()
    top.title("Simple Editor")

    contents = tk.scrolledtext.ScrolledText()
    contents.pack(side=tk.BOTTOM, expand=True, fill=tk.BOTH)

    filename = tk.Entry()
    filename.pack(side=tk.LEFT, expand=True, fill=tk.X)

    tk.Button(text='Open', command=load).pack(side=tk.LEFT)
    tk.Button(text='Save', command=save).pack(side=tk.LEFT)

    top.mainloop()


if __name__ == '__main__':
    # main_windows()
    text_editor()
