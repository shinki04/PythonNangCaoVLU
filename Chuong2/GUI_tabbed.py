import tkinter as tk ; from tkinter import ttk
win = tk.Tk()
win.title ("Python GUI")
# Create tabControl using the ttk Notebook:
tabControl = ttk.Notebook(win)
# Add the tab to tabControl:
tab1 = ttk.Frame(tabControl) #Create a tab
tabControl.add(tab1, text='Tab 1') #Add the tab
tabControl.pack(expand=1 , fill='both') #Pack to make visible

win.mainloop()