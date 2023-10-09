#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022


import tkinter as tk


def print_keysyms(event):
    print(event.keysym)


root = tk.Tk()
root.bind('<Key>', print_keysyms)
root.mainloop()

