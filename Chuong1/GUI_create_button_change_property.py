import tkinter as tk
from tkinter import ttk
win = tk.Tk()



a_label = ttk.Label(win,text="Enter a name : ")
a_label.grid(column=0,row=0)


name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
# name_entered.configure(justify='center')


# Click Event Handle Func

def click_me():
    action.configure(text = "Hello " + name.get())
 #     a_label.configure(foreground='red')
 #   a_label.configure(text='A Red Label')

# Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)
action.grid(column=1,row=1)


win.mainloop()





# import tkinter as tk
# from tkinter import ttk
# win = tk.Tk()



# a_label = ttk.Label(win,text="A Label")
# a_label.grid(column=0,row=0)


# # Click Event Handle Func

# def click_me():
#     action.configure(text="** I have been Clicked! **")  
#     a_label.configure(foreground='red')
#     a_label.configure(text='A Red Label')

# # Adding a button
# action = ttk.Button(win, text="Click Me!", command=click_me)
# action.grid(column=1,row=0) 



# win.mainloop()