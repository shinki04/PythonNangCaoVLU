from tkinter import Tk, Listbox, Button, END, mainloop
import sqlite3

master = Tk()

def prepare_data():
    connection = sqlite3.connect(':memory:') 
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE foo
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                          bar TEXT)''')
    sql = 'INSERT INTO foo (bar) values (?)'
    for i in range(5):
        cursor.execute(sql, (i+1,))
    return(cursor)

def process_data(cursor):
    cursor.execute('SELECT * from foo')
    data = list()
    for row in cursor.fetchall():
        # here process the row, e.g. concatenate, compute, replace, etc.
        data.append(row)
    return(data)

def show_data(parent, data):
    listbox = Listbox(parent)
    listbox.pack()
    for row in data:
        listbox.insert(END, row[0])


cursor = prepare_data()
data_processed = process_data(cursor)
show_data(master, data_processed)
mainloop()