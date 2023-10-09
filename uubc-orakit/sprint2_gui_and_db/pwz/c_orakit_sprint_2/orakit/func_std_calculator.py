#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
from tkinter import *
from tkinter import ttk
import tkinter as tk


def init_func_std_calculator(menu: Menu, func_frm: ttk.LabelFrame):
    print(f'container size: width={func_frm.winfo_width()}, height={func_frm.winfo_height()}')

    # Label(func_frm, text='init_func_simple_calculator').pack(fill=BOTH, expand=1)
    expression_str = tk.StringVar()

    def btn_command(btn_text):
        print('press button:' + btn_text)

        def calculate(expression):
            # print(str(eval(expression)))
            try:
                result = eval(expression)
                return str(result)
            except Exception:
                print('illegal expression')
                return 'error'

        if btn_text == '=':
            result = calculate(expression_str.get())
            print('calculate result: ' + result)
            expression_str.set(expression_str.get() + ' = ' + result)
        else:
            expression_str.set(expression_str.get() + btn_text)

    def init_calculator():
        """实现标准计算器的面板以及计算逻辑 \n
        1、创建一个显示框以及对应的变量，显示、存储计算表达式(及计算结果) \n
        2、数组存好按钮文本，for循环使用grid方法将面板显示出来，同时绑定方法（向显示框追加字符、计算结果） \n
        3、实现第三步绑定的命令（输入字符字符，计算结果） \n
        """

        # 初始化面板前，先清空面板上所有内容
        print('init calculator... start')
        print('clear panel...')
        for child in func_frm.winfo_children():
            child.destroy()
        print('clear panel... done')

        # 创建显示框
        expression_entry = ttk.Entry(func_frm, textvariable=expression_str)
        expression_entry.grid(row=0, column=0, columnspan=4)

        btn_str_list = [
            ['7', '8', '9', '+'],
            ['5', '6', '7', '-'],
            ['1', '2', '3', '*'],
            ['0', '.', '=', '/']
        ]

        # 初始化按钮并绑定计算逻辑
        for row in range(0, 4):
            for col in range(0, 4):
                # print(btn_str_list[row][col])
                btn = ttk.Button(func_frm, text=btn_str_list[row][col])
                btn.grid(row=row+1, column=col)
                btn.configure(command=lambda bt=btn_str_list[row][col]: btn_command(bt))

    menu.add_command(label='Standard Calculator', command=init_calculator)

    # for test
    # init_calculator()


if __name__ == '__main__':
    """unit test"""
    menu = tk.Menu()
    frame = ttk.LabelFrame()
    init_func_std_calculator(menu, frame)
