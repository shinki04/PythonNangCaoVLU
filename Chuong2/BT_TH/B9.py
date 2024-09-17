import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.title("Python GUI")
#=======================================================================================================================#

#* Start Col 0

a_label = ttk.Label(win,text="A Label")
a_label.grid(column=0,row=0)
name = tk.StringVar()
name_entered = ttk.Entry(win, width=12, textvariable=name)
name_entered.grid(column=0, row=1)
name_entered.focus() #Nó tự focus con trỏ vào ô nhập



scrol_w = 30
scrol_h = 3
scr = scrolledtext.ScrolledText(win, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scr.grid(column=0, columnspan=3,row=5)
#* https://stackoverflow.com/questions/50158866/what-is-the-difference-between-column-and-columnspan-in-tkinter-python


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


colors = ["Blue", "Gold", "Red"]


def radCall():
    radSel = radVar.get()
    if radSel == 0:
        win.configure(background=colors[0])
    elif radSel == 1:
        win.configure(background=colors[1])
    elif radSel == 2: 
        win.configure(background=colors[2])


    
    
radVar=tk.IntVar()
# rad1 = tk.Radiobutton(win,text=COLOR1,variable=radVar,value=1,command=radCall)
# rad1.grid(column=0,row=5 ,sticky=tk.W,columnspan=3)
# rad2 = tk.Radiobutton(win,text=COLOR2,variable=radVar,value=2,command=radCall)
# rad2.grid(column=1,row=5 ,sticky=tk.W,columnspan=3)
# rad3 = tk.Radiobutton(win,text=COLOR3,variable=radVar,value=3,command=radCall)
# rad3.grid(column=2,row=5 ,sticky=tk.W,columnspan=3)

radVar.set(99)
for col in range(3):
    curRad = tk.Radiobutton(win, text=colors[col], variable=radVar,  value=col , command=radCall)
    curRad.grid(column=col, row=6, sticky=tk.W)


#* End Col 1
#=======================================================================================================================#

#* Start Col 2

# Click Event Handle Func

def click_me():
    action.configure(text='Hello ' + name.get() + ' ' +  number_chosen.get())
    a_label.configure(foreground='red')
    a_label.configure(text='A Red Label')

# Adding a button
action = ttk.Button(win, text="Click Me!", command=click_me)  
action.grid(column=2, row=1)
#* End Col 2



#=======================================================================================================================#

buttons_frame = ttk.LabelFrame(win,text=   'Labels in a Frame')  
# buttons_frame.grid(column=0, row=7)
buttons_frame.grid(column=1, row=7)
ttk.Label(buttons_frame, text="Label1").grid(column=0, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label2").grid(column=1, row=0,  sticky=tk.W)
ttk.Label(buttons_frame, text="Label3").grid(column=2, row=0,  sticky=tk.W)


win.mainloop()

