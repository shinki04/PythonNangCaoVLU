from tkinter import scrolledtext, Menu
from tkinter import messagebox as msg
import tkinter as tk
from tkinter import ttk
win = tk.Tk()


win.title("Python GUI")
msg.showinfo('Python GUI created using tkinter:\nThe year is 2022') 

# Creating a Menu BarGUI_independent_msg_info.py
menu_bar = Menu(win)
win.config(menu=menu_bar)


def _msgBox():
    answer = msg.askyesnocancel("Python Message Multi Choice Box", "Are  you sure you really wish to do this?")
    print(answer)


# Create menu and add menu items
file_menu = Menu(menu_bar, tearoff=0)  # create File menu  , mất cái - - -
file_menu.add_command(label="New")  # add File menu item
file_menu.add_separator()

file_menu.add_command(label="Exit", command=win.quit)  # Ấn thoát chương trình
# add File menu  to menu bar and give it a label
menu_bar.add_cascade(label="File", menu=file_menu)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=_msgBox)


# Create tabControl using the ttk Notebook:
tabControl = ttk.Notebook(win)
# Add the tab to tabControl:
tab1 = ttk.Frame(tabControl)  # Create a tab
tab2 = ttk.Frame(tabControl)
# Add a second tab
# * Thêm tab phải theo thứ tự 1 2 3 , chứ không nó loạn
tabControl.add(tab1, text='Tab 1')  # Add the tab

tabControl.add(tab2, text='Tab 2')

tabControl.pack(expand=1, fill='both')  # Pack to make visible


# Add another label
mighty = ttk.LabelFrame(tab1, text="Mighty Python")
'''
expand=1 (hoặc expand=True) nghĩa là bạn yêu cầu widget mở rộng (expand) để chiếm không gian trống thêm nếu có. Khi giá trị của expand là 1, widget sẽ chiếm thêm diện tích nếu vùng chứa của nó (ví dụ như cửa sổ hoặc một frame) mở rộng. Nếu không có giá trị này, widget sẽ chỉ chiếm không gian tối thiểu mà nó cần và không mở rộng khi cửa sổ hoặc vùng chứa của nó thay đổi kích thước.

Nếu expand=0 (hoặc expand=False), widget không mở rộng khi vùng chứa của nó lớn hơn.

Ví dụ:

Nếu bạn mở rộng cửa sổ chính (window), thì frame hoặc widget nào được thiết lập expand=1 sẽ tự động mở rộng để chiếm thêm không gian.
'''
mighty.pack(expand=1, fill='both')  # Pack mighty to make it visible in tab1
# Add a label to mighty frame
# ttk.Label(mighty, text="Enter a name").grid(column=1, row=0)
# ttk.Label(mighty, text="Choose a number:").grid(column=2, row=0)


a_label = ttk.Label(mighty, text="Enter a name")
a_label.grid(column=0, row=0)
name = tk.StringVar()
name_entered = ttk.Entry(mighty, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus()  # Nó tự focus con trỏ vào ô nhập

b_label = ttk.Label(mighty, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(
    mighty, width=12, textvariable=number,  state='readonly')
number_chosen['value'] = (1, 2, 4, 42, 100)
number_chosen.grid(column=1, row=1)
number_chosen.current(0)


def click_me():
    action.configure(text='Hello ' + name.get() + ' ' + number_chosen.get())


# Adding a button
action = ttk.Button(mighty, text="Click Me!", command=click_me)
action.grid(column=2, row=1)

scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD).grid(
    column=0, columnspan=3, row=6, sticky="WE")


# Add some space around each label
for child in mighty.winfo_children():
    child.grid_configure(padx=8)


# * Tab 2
mighty2 = ttk.LabelFrame(tab2, text='The Snake')
mighty2.grid(column=0, row=0, padx=8, pady=4)
mighty2.pack(expand=1, fill='both')

# Create 3 checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, width=12, text="Disabled",
                        variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0, padx=5, pady=5)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, width=12, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0, padx=5, pady=5)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, width=12, text="Enabled", variable=chVarEn)

text = "Enabled"
check3.select()
check3.grid(column=2, row=0, padx=5, pady=5)


# Định nghĩa màu sắc
COLOR1 = "Blue"
COLOR2 = "Gold"
COLOR3 = "Red"

# Hàm thay đổi màu nền của buttons_frame


def radCall():
    radSel = radVar.get()
    if radSel == 1:
        buttons_frame.configure(bg=COLOR1)  # Sử dụng biến COLOR1
    elif radSel == 2:
        buttons_frame.configure(bg=COLOR2)  # Sử dụng biến COLOR2
    elif radSel == 3:
        buttons_frame.configure(bg=COLOR3)  # Sử dụng biến COLOR3


radVar = tk.IntVar()
rad1 = tk.Radiobutton(mighty2, text=COLOR1,
                      variable=radVar, value=1, command=radCall)
rad1.grid(column=0, row=1, padx=5, pady=5)
rad2 = tk.Radiobutton(mighty2, text=COLOR2,
                      variable=radVar, value=2, command=radCall)
rad2.grid(column=1, row=1, padx=5, pady=5)
rad3 = tk.Radiobutton(mighty2, text=COLOR3,
                      variable=radVar, value=3, command=radCall)
rad3.grid(column=2, row=1, padx=5, pady=5)

buttons_frame = tk.LabelFrame(mighty2, text='Labels in a Frame')
buttons_frame.grid(column=0, row=7)
# button_frame.grid(column=1, row=7)
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0,  sticky=tk.W)


win.mainloop()
