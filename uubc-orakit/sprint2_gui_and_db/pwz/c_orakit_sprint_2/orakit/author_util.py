#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
import enum
import sqlite3
import tkinter.messagebox as msg

DEFAULT_ADMIN_ACCOUNT = 'admin'
DEFAULT_ADMIN_PWD = 'admin'


class Role(enum.Enum):
    Admin = 0
    Visitor = 1
    Developer = 2


def login_sys(account: str, pwd: str) -> bool:
    """
    登录逻辑，捞数据库进行鉴权
    :param account: 用户名
    :param pwd: 密码
    :return: 账密鉴权是否成功
    """
    if account == '' or pwd == '':
        print('account or password is empty')
        # msg.showwarning('login fail', 'account or password is empty')
        return False
    conn = sqlite3.connect('orakit.db')
    cur = conn.cursor()
    _pwd = cur.execute(f"""select password from user where account='{account}'""").fetchone()
    if _pwd is None:
        return False
    # print(f'got pwd [{_pwd[0]}] and your input is [{pwd}]')
    return True if _pwd[0] == pwd else False


def create_account(account: str, pwd: str, role: str) -> bool:
    """
    新增账户
    :param account: 用户名
    :param pwd: 密码
    :param role: 角色
    :return:
    """
    if account == '' or pwd == '' or role == '':
        print('empty input...')
        return False

    try:
        conn = sqlite3.connect('orakit.db')
        cur = conn.cursor()

        cur.execute(f"""insert into user (account, password, role) values ('{account}', '{pwd}', '{role}')""")
        conn.commit()
        conn.close()
        print(f'create account user successful, account={account}, pwd={pwd}, role={role}')
    except Exception as e:
        print(e)
        return False
    return True


def init_db():
    conn = sqlite3.connect('orakit.db')
    cur = conn.cursor()
    try:
        print('create user table and insert the default account')
        cur.execute(f"""create table user(
                                id INTEGER PRIMARY KEY AUTOINCREMENT not null ,
                                account text not null,
                                password text not null,
                                role text not null)""")
        cur.execute(f"""insert into user (account, password, role) values ('{DEFAULT_ADMIN_ACCOUNT}', '{DEFAULT_ADMIN_PWD}', '{Role.Admin}')""")
        conn.commit()
        conn.close()
        # result = cur.execute(f"""select * from user where account = '{DEFAULT_ADMIN_ACCOUNT}'""")
        # print(type(result))
        # for row in result:
        #     print(row)
    except Exception as e:
        print(e)


def select_role_by_account(account) -> str:
    conn = sqlite3.connect('orakit.db')
    cur = conn.cursor()
    result = cur.execute(f"""select role from user where account = '{account}'""").fetchone()
    conn.close()
    if result is not None:
        print('got role = ' + result[0])
        return result[0]

