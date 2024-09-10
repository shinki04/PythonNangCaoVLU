# Dựa trên bài combox - button nhập 2 dòng A B , click me lấy giá trị a , b + , hoặc giải phương trình 1 2 , xuất kq ra button
import tkinter as tk
from tkinter import ttk,BOTTOM
import tkinter.messagebox as mbox
# from tkinter import *

win = tk.Tk()
win.title("Simple Math")

main_label = ttk.Label(win,text="ax + b = 0")
main_label.grid(column=0,row=0)


a_label = ttk.Label(win,text="ax")
a_label.grid(column=0,row=2)
a = tk.IntVar()  
a_entered = ttk.Entry(win, width=12, textvariable=a)
a_entered.grid(column=1, row=2)
   
b_label = ttk.Label(win,text="b")
b_label.grid(column=0,row=3)
b = tk.IntVar()
b_entered = ttk.Entry(win, width=12, textvariable=b)
b_entered.grid(column=1, row=3)

c = tk.IntVar()
c.set(0)

c_entered = ttk.Entry(win,width=12,textvariable=c ,state="disable")
c_entered.grid(column=2,row=2)
# Click Event Handle Func
def click_me():
    try:
        # Kiểm tra nếu `a` và `b` là số
        a_value = a.get()
        b_value = b.get()

       
        if a_value != 0:
            c.set(-b_value / a_value)
        else:
            mbox.showerror("Error", "a must be different from 0")

    # Lỗi này là do sai giá trị
    except tk.TclError:
        
        mbox.showerror("Input Error", "Please enter valid numbers for a and b")
    
    # ktra những lỗi khác, này dư thừa nhưng để cho bt
    except :
        mbox.showerror("Something wrong", "Check again")


# # Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=0,row=4,columnspan=2)


win.geometry("300x300")
win.mainloop()