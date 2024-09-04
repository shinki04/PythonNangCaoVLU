import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("Python GUI")

# Nơi chứa nhãn : win
a_label = ttk.Label(win, text="A Label")
a_label.grid(column=0,row=0)

b_label = ttk.Label(win, text="B Label")
b_label.grid(column=1,row=1)
# .configure(background="Red")


win.mainloop()