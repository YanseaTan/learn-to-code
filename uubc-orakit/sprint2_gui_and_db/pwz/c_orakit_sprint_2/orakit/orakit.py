#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as msg
from tkinter import scrolledtext as st
import author_util as aut
from author_util import Role
import func_file_compressor as ffc
import func_simple_calculator as fsc
import func_std_calculator as fdc

MAIN_WIN_WIDTH = 800
MAIN_WIN_HEIGHT = 400


def help_callback():
    msg.showinfo('OraKit Help', 'no help')


def init_func(root, menu_bar, account):
    """根据用户角色初始化功能菜单"""

    # ------------------------------------------------------------------------------
    # 处理权限问题
    # ------------------------------------------------------------------------------

    # 首先将Function菜单下内容清空
    menu_func = menu_bar.winfo_children()[1]
    menu_func.delete(0, 9999)

    # 查询用户角色
    role = aut.select_role_by_account(account)

    # print(role)

    # 根据角色处理菜单项(测试权限系统用)
    def available_for_this_role(_role):
        if str(_role) == role:
            return tk.NORMAL
        return tk.DISABLED

    menu_func.add_command(label='[TEST] Available for Role.Admin', state=available_for_this_role(Role.Admin))
    menu_func.add_command(label='[TEST] Available for Role.Visitor', state=available_for_this_role(Role.Visitor))
    menu_func.add_command(label='[TEST] Available for Role.Developer', state=available_for_this_role(Role.Developer))

    # ------------------------------------------------------------------------------
    # 处理本次迭代的实际可用功能项
    # ------------------------------------------------------------------------------

    # 首先，获取主窗口左右两部分LabelFrame布局控件
    children = root.winfo_children()
    chat_frame = None
    func_frame = None

    for child in children:
        # 通过组件属性获取子组件
        try:
            if child.cget('text') == 'chat-area':
                print('got the chat-area frame')
                chat_frame = child
            elif child.cget('text') == 'func-area':
                print('got the func-area frame')
                func_frame = child
        except Exception as e:
            print(e)

    # 其次，初始化右侧对话系统（本次不再具体实现后台功能，仅展示）
    stext = st.ScrolledText(chat_frame)
    stext.pack(padx='2p', fill=BOTH, expand=1)
    stext.insert(INSERT, """now you can use the chat system\n---\n\nme: hello\nor: hi""")

    def send_msg(event=None):
        default_resp = """\nor: chat system offline now."""
        stext.insert('end', f'\nme: {entry_input.get()}' + default_resp)

    frm_input = Frame(chat_frame)
    entry_input = StringVar()
    ent = Entry(frm_input, textvariable=entry_input)
    ent.pack(side=LEFT)
    ent.bind('<Key-Return>', send_msg)
    Button(frm_input, text='Enter to send the chat', command=send_msg).pack(side=RIGHT)
    frm_input.pack(padx='2p', fill=BOTH, expand=1)

    # 最后，初始化功能菜单并绑定
    fsc.init_func_simple_calculator(menu_func, func_frame)
    fdc.init_func_std_calculator(menu_func, func_frame)
    ffc.init_func_file_compressor(menu_func, func_frame)


def hidden_func_for_admin(root):
    hidden_win = tk.Toplevel(root)
    hidden_win.title('Hidden Func for Admin')
    hidden_win.geometry(f'400x300+{(root.winfo_screenwidth() - 400) // 2}+{(root.winfo_screenheight() - 300) // 2}')

    # 新增用户
    lfrm = ttk.Labelframe(hidden_win, text='Account Insert', padding='5p')
    lfrm.pack(pady='5p')
    account = tk.StringVar()
    password = tk.StringVar()
    roles = tk.StringVar()
    ttk.Label(lfrm, text='Account:').grid(column=0, row=0, sticky=tk.W)
    ttk.Label(lfrm, text='Password:').grid(column=0, row=1, sticky=tk.W)
    ttk.Label(lfrm, text='Role:').grid(column=0, row=2, sticky=tk.W)
    ttk.Entry(lfrm, textvariable=account).grid(column=1, row=0)
    ttk.Entry(lfrm, textvariable=password).grid(column=1, row=1)
    role_input = ttk.Combobox(lfrm, textvariable=roles)
    role_input.grid(column=1, row=2)
    role_input['values'] = [role for role in Role]
    ttk.Button(lfrm, text='Submit', command=lambda: aut.create_account(account.get(), password.get(), roles.get())).grid(column=1, row=4, sticky=tk.E)

    # 查询用户
    lfrm2 = ttk.Labelframe(hidden_win, text='Search Account', padding='5p')
    lfrm2.pack(pady='10p')
    ttk.Label(lfrm2, text='Account:').grid(column=0, row=0, sticky=tk.W)
    ttk.Entry(lfrm2).grid(column=1, row=0)
    ttk.Button(lfrm2, text='Search').grid(column=1, row=1, sticky=tk.E)
    ttk.Label(lfrm2, text='(not impled)').grid(column=1, row=2, sticky=tk.E)


def login(root, menu_bar):
    def login_successful():
        """登录成功后显示功能项"""
        # print('login successful')
        root.title(f'OraKit 0.2, login with {account.get()}')
        msg.showinfo('login successful', 'login successful')
        if account.get() == aut.DEFAULT_ADMIN_ACCOUNT:
            menu_bar.add_command(label='[*hidden-func-for-admin]', command=lambda: hidden_func_for_admin(root))
        login_win.destroy()
        init_func(root, menu_bar, account.get())

    def login_fail():
        login_win.destroy()
        msg.showwarning('login fail', 'account or password error')

    login_win = tk.Toplevel(root)
    login_win.title('Login')
    login_win.geometry(f'300x100+{(root.winfo_screenwidth() - 300) // 2}+{(root.winfo_screenheight() - 200) // 2}')

    frm = ttk.Frame(login_win)
    frm.pack(pady='10p')

    account = tk.StringVar()
    password = tk.StringVar()
    ttk.Label(frm, text='Account:').grid(column=0, row=0)
    ttk.Label(frm, text='Password:').grid(column=0, row=1)
    ttk.Entry(frm, textvariable=account).grid(column=1, row=0)
    ttk.Entry(frm, textvariable=password).grid(column=1, row=1)

    ttk.Separator(login_win, orient=tk.HORIZONTAL).pack(fill='x', pady='3p')
    ttk.Label(login_win, text='Enter to login').pack()

    login_win.bind('<Key-Return>', lambda event: login_successful() if aut.login_sys(account.get(), password.get()) else login_fail())

    # for test
    # login_win.bind('<Key-Return>', lambda event: login_successful())


def init_menu(root):
    root.option_add('*tearOff', tk.FALSE)

    menu_bar = tk.Menu(root)
    root.config(menu=menu_bar)

    # 系统
    menu_sys = tk.Menu(menu_bar)
    menu_bar.add_cascade(label='System', underline=3, menu=menu_sys)
    menu_sys.add_command(label='Login', underline=0, command=lambda: login(root, menu_bar))
    menu_sys.add_command(label='Exit', underline=0, command=lambda: root.destroy())

    # 功能
    menu_func = tk.Menu(menu_bar)
    menu_bar.add_cascade(label="Function", menu=menu_func, underline=0)
    menu_func.add_command(label='Login First Please')

    # init_func(root, menu_bar, 'Role.Admin')

    # 关于
    menu_bar.add_cascade(label='About',
                         underline=0,
                         command=lambda: msg.showinfo('About', 'OraKit 0.2 Gui and Database Version\n'
                                                               'Read more in my blog ~ pwz.wiki\n'
                                                               'That\'s all ...'))


def show_main_window():
    win = tk.Tk()
    win.title('OraKit 0.2')
    # 窗口居中
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    # win.minsize(MAIN_WIN_WIDTH, MAIN_WIN_HEIGHT)
    size = f'{MAIN_WIN_WIDTH}x{MAIN_WIN_HEIGHT}+{(screen_width - MAIN_WIN_WIDTH) // 2}+{(screen_height - MAIN_WIN_HEIGHT) // 2}'
    win.geometry(size)
    # win.resizable(False, False)

    aut.init_db()
    init_menu(win)
    # win.resizable(False, False)

    # 尝试将窗口分为左右两部分，中间用分割线表示
    frm_l = ttk.Labelframe(win, text='func-area', height=round(MAIN_WIN_HEIGHT * 0.95), width=round(MAIN_WIN_WIDTH * 0.6))
    frm_r = ttk.Labelframe(win, text='chat-area', height=round(MAIN_WIN_HEIGHT * 0.95), width=round(MAIN_WIN_WIDTH * 0.4))
    # frm_l = tk.Frame(win, height=MAIN_WIN_HEIGHT, width=MAIN_WIN_WIDTH*0.7)
    # frm_r = tk.Frame(win, height=MAIN_WIN_HEIGHT, width=MAIN_WIN_WIDTH*0.2)
    # win.grid_columnconfigure(0, weight=7)
    # win.grid_columnconfigure(1, weight=1)
    # win.grid_columnconfigure(2, weight=2)
    # win.grid_rowconfigure(0, weight=3)
    # frm_l = ttk.Labelframe(win, text='func-area', padding='10p')
    # frm_r = ttk.Labelframe(win, text='chat-area', padding='10p')

    # sep = ttk.Separator(win, orient='vertical')
    # sep.grid(column=1, row=0, pady='6p', sticky=tk.NS)
    # frm_l.grid(column=0, row=0, pady='6p', padx='6p', sticky=N + E + S + W)
    # frm_r.grid(column=2, row=0, pady='6p', padx='6p', sticky=N + E + S + W)
    frm_l.pack(side=LEFT, padx='10p')
    frm_r.pack(side=RIGHT, padx='10p')
    # frm_l.grid_propagate(False)
    # frm_r.grid_propagate(False)
    win.update()

    # 如下加入子控件会导致上层frame的高度、宽度设置失效
    # ttk.Label(frm_l, text='test').pack()
    # ttk.Label(frm_r, text='test').pack()
    # ttk.Label(frm_l, text='test').grid(column=0, row=0)
    # ttk.Label(frm_r, text='test').grid(column=1, row=0)
    # ttk.Label(frm_l, text='test').grid(column=0, row=0, sticky=N+E+S+W)
    # ttk.Label(frm_r, text='test').grid(column=1, row=0, sticky=N+E+S+W)
    print(round(MAIN_WIN_WIDTH * 0.6))
    print(frm_l.winfo_width())
    print(frm_l.winfo_height())

    # ll = Label(frm_l, text='init_func_file_compress', width=frm_l.winfo_width())
    # ll.pack(fill=BOTH, expand=1)
    # win.update()
    # print(ll.winfo_width())

    # 将左右两个布局Frame的大小固定住，不根据子控件变换大小
    frm_l.pack_propagate(False)
    frm_l.grid_propagate(False)
    frm_r.pack_propagate(False)
    frm_r.grid_propagate(False)

    win.update()
    win.mainloop()


if __name__ == '__main__':
    show_main_window()
