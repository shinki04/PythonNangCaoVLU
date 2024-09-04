import tkinter as tk
from tkinter import ttk
win = tk.Tk()
win.title("Simple test")


a_label = ttk.Label(win,text="A Label")
a_label.grid(column=0,row=0)


name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=3, row=2)



# Click Event Handle Func

def click_me():
    action.configure(text = "Hello " + name.get())
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

# Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=2,row=4)
action.configure(state='disabled') #Không cho ấn , Disable the button widget
name_entered.focus() #Nó tự focus con trỏ vào ô nhập







# Căn giữa form ra màn hình
window_width = 450 #đơn vị pixel
window_height = 175 
screen_width = win.winfo_screenwidth() 
screen_height = win.winfo_screenheight() 
center_x = int((screen_width - window_width)/2) 
center_y = int((screen_height - window_height)/2)
win.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
win.mainloop()