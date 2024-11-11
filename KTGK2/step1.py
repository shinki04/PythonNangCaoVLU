from tkinter import Tk, Listbox, END, mainloop
import sqlite3

master = Tk()

listbox = Listbox(master)
listbox.pack()

connection = sqlite3.connect(':memory:')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE foo
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                      bar TEXT)''')

sql = 'INSERT INTO foo (bar) values (?)'

for i in range(5):
    cursor.execute(sql, (i+1,))

cursor.execute('SELECT * from foo')
for row in cursor.fetchall():
    listbox.insert(END, row[0])

mainloop()