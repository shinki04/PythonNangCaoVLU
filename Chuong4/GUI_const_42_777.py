import tkinter as tk

win = tk.Tk()


GLOBAL_CONST = 42  # ...

def usingGlobal():  
   global GLOBAL_CONST  
   print(GLOBAL_CONST)  
   GLOBAL_CONST = 777
   print(GLOBAL_CONST)

# print(GLOBAL_CONST)

usingGlobal()


