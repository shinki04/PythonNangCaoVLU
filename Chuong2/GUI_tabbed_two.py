import tkinter as tk ; from tkinter import ttk
win = tk.Tk()
win.title ("Python GUI")
# Create tabControl using the ttk Notebook:
tabControl = ttk.Notebook(win)
# Add the tab to tabControl:
tab1 = ttk.Frame(tabControl) #Create a tab

tab2 = ttk.Frame(tabControl) 
# Add a second tab 
#* Thêm tab phải theo thứ tự 1 2 3 , chứ không nó loạn 
tabControl.add(tab1, text='Tab 1')#Add the tab

tabControl.add(tab2, text='Tab 2') 

tabControl.pack(expand=1 , fill='both') #Pack to make visible

win.mainloop()