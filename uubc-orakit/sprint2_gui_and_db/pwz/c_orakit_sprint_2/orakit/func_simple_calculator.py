#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
import tkinter
from tkinter import *
from tkinter import ttk


def init_func_simple_calculator(menu: Menu, func_frm: ttk.LabelFrame):
    print(f'container size: width={func_frm.winfo_width()}, height={func_frm.winfo_height()}')
    # Label(func_frm, text='init_func_simple_calculator').pack(fill=BOTH, expand=1)

    def calculate(expression):
        # print(str(eval(expression)))
        try:
            result = eval(expression)
            return ' =' + str(result)
        except Exception:
            print('illegal expression')
            return ''

    def init_calculator():
        """实现简易计算器的面板以及计算逻辑 \n
        1、创建一个显示框、计算按钮 \n
        2、实现计算方法:）
        """

        # 初始化面板前，先清空面板上所有内容
        print('init calculator... start')
        print('clear panel...')
        for child in func_frm.winfo_children():
            child.destroy()
        print('clear panel... done')

        # 创建显示框及按钮
        expression_entry = ttk.Entry(func_frm, width=30)
        expression_entry.grid(row=0, column=0, columnspan=4)
        exec_btn = ttk.Button(func_frm, text='calculate',
                              command=lambda: expression_entry.insert(tkinter.END, calculate(expression_entry.get())))
        exec_btn.grid(row=0, column=5)

    menu.add_command(label='Simple Calculator', command=init_calculator)



