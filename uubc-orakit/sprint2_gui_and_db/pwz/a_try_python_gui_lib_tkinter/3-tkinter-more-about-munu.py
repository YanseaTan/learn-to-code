#!/usr/bin/env python
# -*- coding: utf-8 -*-
# created by pwz.wiki 2022
# refer1 ~ https://docs.python.org/3/library/tkinter.html
# refer2 ~ http://tkdocs.com/tutorial/onepage.html
# !important~ all notes in """notes""" are quoted from refer2

from tkinter import *
from tkinter import ttk, messagebox


def mock_menu_func():
    print('boom!')


root = Tk()
root.title('')

# ---------------------------------------------------------------------------------------------------
"""Menu Widgets and Hierarchy"""
# ---------------------------------------------------------------------------------------------------

"""Menus are part of the classic Tk widgets; there is no menu widget in the themed Tk widget set."""
root.option_add('*tearOff', FALSE)

# 首先创建一个【菜单栏】
"""To create a menubar for a window, first, create a menu widget. Then, 
use the window's menu configuration option to attach the menu widget to the window."""
menubar = Menu(root)
root.config(menu=menubar)

# 为【菜单栏】添加一些【菜单】
"""The add_cascade method adds a menu item, which itself is a menu (a submenu)."""
menu_app = Menu(menubar)
menu_file = Menu(menubar)
menu_edit = Menu(menubar)
menubar.add_cascade(menu=menu_app, label='App')
menubar.add_cascade(menu=menu_file, label='File')
menubar.add_cascade(menu=menu_edit, label='Edit')

# 为所有的【菜单】添加具体【功能项】
menu_app.add_command(label='Exit', command=lambda: root.destroy())
# ---
menu_file.add_command(label='New', command=mock_menu_func)
menu_file.add_command(label='Open...', command=mock_menu_func)
menu_file.add_command(label='Close', command=mock_menu_func)
# ---
menu_edit.add_command(label='Redo', command=mock_menu_func)
menu_edit.add_command(label='Undo', command=mock_menu_func)
menu_edit.add_command(label='ClearAll', command=mock_menu_func)

# 为【菜单栏】中的【菜单】添加【子菜单】，并为【子菜单】添加菜单项
menu_recent = Menu(menu_file)
menu_file.add_separator()  # 菜单项分割线
menu_file.add_cascade(menu=menu_recent, label='Open Recent')
menu_recent.add_command(label='submenu item1', command=mock_menu_func)
menu_recent.add_command(label='submenu item2', command=mock_menu_func)
menu_recent.add_command(label='...', command=mock_menu_func)

# 单选、复选菜单项
"""Finally, there are also checkbutton and radiobutton menu items that 
behave analogously to checkbutton and radiobutton widgets. 
These menu items have a variable associated with them.

Depending on its value, an indicator (i.e., checkmark or selected radiobutton) 
may be shown next to its label."""
menu_check = Menu(menubar)
menubar.add_cascade(menu=menu_check, label='CheckMenu')
# ---
check1 = StringVar()
menu_check.add_checkbutton(label='Check1', variable=check1, onvalue=1, offvalue=0)
menu_file.add_separator()
# ---
radio = StringVar()
# radio.set('2')
menu_check.add_radiobutton(label='One', variable=radio, value=1)
menu_check.add_radiobutton(label='Two', variable=radio, value=2)

# ---------------------------------------------------------------------------------------------------
"""Manipulating Menu Items"""
# ---------------------------------------------------------------------------------------------------

# 菜单状态
"""You can disable a menu item so that users cannot select it. This can be done via the state option, 
setting it to the value disabled. Use a value of normal to re-enable the item."""
menu_check.entryconfigure('Check1', state=DISABLED)


def check1_state_flash():
    print(check2.get())
    if check2.get() == '0':
        menu_check.entryconfigure('Check1', state=NORMAL)
    else:
        menu_check.entryconfigure('Check1', state=DISABLED)


menu_check.add_separator()
check2 = StringVar()
check2.set('1')
menu_check.add_checkbutton(label='Check1Disabled', variable=check2, onvalue=1, offvalue=0, command=check1_state_flash)

# 为菜单项展示快捷键
"""The accelerator option is used to indicate a keyboard equivalent that corresponds to a menu item. 
This does not actually create the accelerator but only displays it next to the menu item.
You still need to create an event binding for the accelerator yourself."""
"""
For a complete description of all the different event names, modifiers, and the different event parameters 
that are available with each, the best place to look is the bind command reference.

<Activate>:     Window has become active.
<Deactivate>:   Window has been deactivated.
<MouseWheel>:   Scroll wheel on mouse has been moved.
<KeyPress>:     Key on keyboard has been pressed down.
<KeyRelease>:   Key has been released.
<ButtonPress>:  A mouse button has been pressed.
<ButtonRelease>:A mouse button has been released.
<Motion>:       Mouse has been moved.
<Configure>:    Widget has changed size or position.
<Destroy>:      Widget is being destroyed.
<FocusIn>:      Widget has been given keyboard focus.
<FocusOut>:     Widget has lost keyboard focus.
<Enter>:        Mouse pointer enters widget.
<Leave>:        Mouse pointer leaves widget. """

"""For keyboard events, it's the specific key, e.g., A, 9, space, plus, comma, equal. 
A complete list can be found in the keysyms command reference."""
# keysyms按键code参考1 https://tcl.tk/man/tcl8.6/TkCmd/keysyms.htm
# keysyms按键code参考2 https://www.luckydesigner.space/tkinter-bind-shortcut-key-sheet/
menu_app.entryconfigure('Exit', accelerator='Control_L + Q')
root.bind('<Control_L><KeyPress-q>', lambda event: root.destroy())  # Control_L + q
root.bind('<Control_L><KeyPress-Q>', lambda event: root.destroy())  # Control_L + Q
# 全局键盘事件
# def print_keysyms(event):
#     print(event.keysym)
# root.bind('<Key>', print_keysyms)

# 添加快捷启动（Alt + 字母）
"""All platforms support keyboard traversal of the menubar via the arrow keys.
 The keys that trigger these jumps are indicated by an underlined letter in the menu item's label. 
 To add one of these to a menu item, use the underline configuration option for the item."""
menubar.add_cascade(menu=menu_app, label='AppCopy', underline=0)
menubar.add_cascade(menu=menu_file, label='FileCopy', underline=0)
menubar.add_cascade(menu=menu_edit, label='EditCopy', underline=0)


# 虚拟事件
"""The events we've seen so far are low-level operating system events like mouse clicks and window resizes. 
Many widgets also generate higher-level, semantic events called virtual events. 
These are indicated by double angle brackets around the event name, e.g., <<foo>>."""
"""For example, a listbox widget will generate a <<ListboxSelect>> virtual event whenever its selection changes."""
menubar.add_command(label='GenerateAVirtualEvent', command=lambda: root.event_generate('<<Shanghai-is-Ok>>'))
root.bind('<<Shanghai-is-Ok>>', lambda event: messagebox.showinfo(message=str(event)+'\n<<Shanghai-is-Ok>>'))

root.mainloop()
