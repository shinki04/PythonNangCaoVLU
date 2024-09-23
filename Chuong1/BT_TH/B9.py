import tkinter as tk
from tkinter import ttk
win = tk.Tk()

#=======================================================================================================================#

#* Start Col 0

a_label = ttk.Label(win,text="Enter a name")
a_label.grid(column=0,row=0)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus() #Nó tự focus con trỏ vào ô nhập



#* End Col 0

#=======================================================================================================================#

#* Start Col 1

ttk.Label(win, text="Choose a number:").grid(column=1, row=0)
number = tk.StringVar()
number_chosen = ttk.Combobox(win, width=12, textvariable=number,  state='readonly')
number_chosen['value'] = (1,2,4,42,100)
number_chosen.grid(column=1,row=1)
number_chosen.current(0)


#Create 3 checkbuttons
chVarDis = tk.IntVar()  
check1 = tk.Checkbutton(win,width=12,text="Disabled" ,variable=chVarDis,state='disabled')
check1.select()  
check1.grid(column=0, row=4, sticky=tk.W)  

chVarUn = tk.IntVar()  
check2 = tk.Checkbutton(win,width=12,text="UnChecked" ,variable=chVarUn)
check2.deselect()  
check2.grid(column=1, row=4, sticky=tk.W)  

chVarEn = tk.IntVar()
check3 = tk.Checkbutton(win,width=12,text="Enabled" ,variable=chVarEn)

text="Enabled"
check3.select()
check3.grid(column=2, row=4, sticky=tk.W)


#* End Col 1
#=======================================================================================================================#

#* Start Col 2

# Click Event Handle Func

def click_me():
    action.configure(text='Hello ' + name.get() + ' ' +  number_chosen.get())
    
# Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)  
action.grid(column=2, row=1)
#* End Col 2



#=======================================================================================================================#

win.mainloop()
