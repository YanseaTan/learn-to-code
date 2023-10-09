#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022

import sqlite3


def create_database():
    # 首先连接数据库
    conn = sqlite3.connect('library.db')

    # 准备建表语句
    create_db = """
    create table book (
    id int primary key  not null,
    name text not null,
    price int not null)
    """

    # 通过游标执行sql
    cur = conn.cursor()
    cur.execute(create_db)

    # 提交变更
    conn.commit()
    conn.close()


def insert_data():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    cur.execute("""insert into book (id, name, price) values(1, 'silent hill', 100)""")
    cur.execute("""insert into book (id, name, price) values(2, 'mocking bird', 299)""")
    cur.execute("""insert into book (id, name, price) values(3, 'hello world', 100)""")
    conn.commit()
    conn.close()


def select_all():
    conn = sqlite3.connect('library.db')
    cur = conn.cursor()
    result = cur.execute("""select * from book""")
    for row in result:
        print(row)

    conn.close()


if __name__ == '__main__':
    # create_database()
    # insert_data()
    select_all()


