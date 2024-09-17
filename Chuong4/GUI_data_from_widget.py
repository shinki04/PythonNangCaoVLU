from tkinter import messagebox as msg
from tkinter import scrolledtext, Spinbox
import tkinter as tk
from tkinter import ttk
from time import sleep  # careful - this can freeze the GU
win = tk.Tk()

win.title("Python GUI")


win.iconbitmap('Chuong3\pyc.ico')

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


# Sử dụng grid thay vì pack
tabControl.grid(row=0, column=0, sticky='nsew')  # Dùng grid để quản lý tabControl
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

scrol = scrolledtext.ScrolledText(mighty, width=30, height=3, wrap=tk.WORD)
scrol.grid(column=0, columnspan=3, row=6)

'''
Lỗi "AttributeError: 'NoneType' object has no attribute 'insert'" xuất hiện vì bạn đang gán scrol bằng cách sử dụng .grid() trên cùng một dòng mà không tách biệt. 
Phương thức .grid() (cũng như .pack() hay .place()) không trả về giá trị, thay vào đó, nó luôn trả về None, nên sau khi gọi .grid(), scrol trở thành None, dẫn đến lỗi khi gọi .insert().
'''
# Spinbox callback


def _spin():
    value = spin.get()
    print(value)
    scrol.insert(tk.INSERT, value + '\n')
    strData = spin.get()  
    print("Spinbox value: " + strData)



# Adding a Spinbox widget
# spin = Spinbox(mighty, from_=0, to=10, width=5, bd=8,  command=_spin)
# spin.grid(column=0, row=2)
spin = Spinbox(mighty, values=(1, 2, 4, 42, 100),
               width=5, bd=8,  command=_spin)
spin.grid(column=0, row=2)


# Add some space around each label
for child in mighty.winfo_children():
    child.grid_configure(padx=8)


# * Tab 2
mighty2 = ttk.LabelFrame(tab2, text=' The Snake ')
mighty2.grid(column=0, row=0, padx=8, pady=4)

# Create 3 checkbuttons
chVarDis = tk.IntVar()
check1 = tk.Checkbutton(mighty2, width=12, text="Disabled",
                        variable=chVarDis, state='disabled')
check1.select()
check1.grid(column=0, row=0)

chVarUn = tk.IntVar()
check2 = tk.Checkbutton(mighty2, width=12, text="UnChecked", variable=chVarUn)
check2.deselect()
check2.grid(column=1, row=0)

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(mighty2, width=12, text="Enabled", variable=chVarEn)

text = "Enabled"
check3.select()
check3.grid(column=2, row=0)


# COLOR1 = "Blue"
# COLOR2 = "Gold"
# COLOR3 = "Red"


# def radCall():
#     radSel = radVar.get()
#     if radSel == 1:
#         mighty2.configure(background=COLOR1)
#     elif radSel == 2:
#         mighty2.configure(background=COLOR2)
#     elif radSel == 3:
#         mighty2.configure(background=COLOR3)


# radVar = tk.IntVar()
# rad1 = tk.Radiobutton(mighty2, text=COLOR1,
#                       variable=radVar, value=1, command=radCall)
# rad1.grid(column=0, row=2, sticky=tk.W, columnspan=3)
# rad2 = tk.Radiobutton(mighty2, text=COLOR2,
#                       variable=radVar, value=2, command=radCall)
# rad2.grid(column=1, row=2, sticky=tk.W, columnspan=3)
# rad3 = tk.Radiobutton(mighty2, text=COLOR3,
#                       variable=radVar, value=3, command=radCall)
# rad3.grid(column=2, row=2, sticky=tk.W, columnspan=3)


# First, we change our Radiobutton global variables into a list
colors = ["Blue", "Gold", "Red"]

# We have also changed the callback function to be zero-based, using the list
# instead of module-level global variables
# Radiobutton Callback


def radCall():
    radSel = radVar.get()
    if radSel == 0:
        mighty2.configure(text='Blue')
    elif radSel == 1:
        mighty2.configure(text='Gold')
    elif radSel == 2:
        mighty2.configure(text='Red')


# create three Radiobuttons using one variable
radVar = tk.IntVar()

# Next we are selecting a non-existing index value for radVar
radVar.set(99)

# Now we are creating all three Radiobutton widgets within one loop
for col in range(3):
    curRad = tk.Radiobutton(
        mighty2, text=colors[col], variable=radVar, value=col, command=radCall)
    curRad.grid(column=col, row=1, sticky=tk.W)             # row=6


# Add a Progressbar to Tab 2
progress_bar = ttk.Progressbar(tab2, orient='horizontal', length=286, mode='determinate')
progress_bar.grid(column=0, row=3, pady=2)

# update progressbar in callback loop


def run_progressbar():
    progress_bar["maximum"] = 100
    for i in range(101):
        sleep(0.05)
        progress_bar["value"] = i   # increment progressbar
        progress_bar.update()       # have to call update() in loop
    progress_bar["value"] = 0       # reset/clear progressbar


def start_progressbar():
    progress_bar.start()


def stop_progressbar():
    progress_bar.stop()


def progressbar_stop_after(wait_ms=1000):
    win.after(wait_ms, progress_bar.stop)


# NEW CODE
# Create a container to hold buttons
buttons_frame = ttk.LabelFrame(mighty2, text=' ProgressBar ')
buttons_frame.grid(column=0, row=2, sticky='W', columnspan=2)


# Add Buttons for Progressbar commands
ttk.Button(buttons_frame, text=" Run Progressbar   ",
           command=run_progressbar).grid(column=0, row=0, sticky='W')
ttk.Button(buttons_frame, text=" Start Progressbar  ",
           command=start_progressbar).grid(column=0, row=1, sticky='W')
ttk.Button(buttons_frame, text=" Stop immediately ",
           command=stop_progressbar).grid(column=0, row=2, sticky='W')
ttk.Button(buttons_frame, text=" Stop after second ",
           command=progressbar_stop_after).grid(column=0, row=3, sticky='W')

for child in buttons_frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

for child in mighty2.winfo_children():
    child.grid_configure(padx=8, pady=2)


win.mainloop()
