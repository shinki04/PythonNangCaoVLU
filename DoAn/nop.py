import psycopg2
from psycopg2 import sql

from tkinter import Tk, Label, Button, Entry, Frame, messagebox, Checkbutton, IntVar
from tkcalendar import Calendar
from datetime import datetime

now = datetime.now()
print(now.year)

class TaskManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        # Calendar
        cal_frame = Frame(root)
        cal_frame.grid(row=0, column=0, columnspan=3, padx=20)
        self.calendar = Calendar(cal_frame, font=("Arial", 12), selectmode="day", year=now.year, month=now.month, day=now.day)
        self.calendar.pack(expand=True)
        self.calendar.bind("<<CalendarSelected>>", self.calendar_date_changed)

        task_list = Frame(self.root)
        task_list.grid(column=3, row=0, padx=50)

        # Task Entry and Buttons
        Label(task_list, text="Task:").grid(row=1, column=0)
        self.task_entry = Entry(task_list)
        self.task_entry.grid(row=1, column=1)

        self.add_button = Button(task_list, text="Add Task", command=self.add_new_task)
        self.add_button.grid(row=2, column=0)

        self.save_button = Button(task_list, text="Save Changes", command=self.save_changes)
        self.save_button.grid(row=2, column=1)

        # Task List (using Checkbuttons)
        self.task_frame = Frame(task_list)
        self.task_frame.grid(row=3, column=0, columnspan=2)

        # Initialize selected date and populate tasks
        self.connect_db()
        self.calendar_date_changed()

    def connect_db(self):
        try:
            self.conn = psycopg2.connect(
                dbname="task_manager",
                user="postgres",
                password="123456",
                host="localhost"
            )
            self.cursor = self.conn.cursor()
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def calendar_date_changed(self, event=None):
        date_selected = self.calendar.get_date()
        self.update_task_list(date_selected)

    def update_task_list(self, date):
        # Clear the existing checkbuttons
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        self.cursor.execute("SELECT task, completed FROM tasks WHERE date = %s", (date,))
        results = self.cursor.fetchall()

        self.checkbuttons = []  # Store checkbuttons and associated task data
        for idx, (task, completed) in enumerate(results):
            var = IntVar(value=1 if completed == 'YES' else 0)  # 1 if completed, 0 if incomplete
            checkbutton = Checkbutton(self.task_frame, text=task, variable=var)
            checkbutton.grid(row=idx, column=0, sticky="w")
            self.checkbuttons.append((checkbutton, var, task))  # Store checkbutton, variable, task

    def save_changes(self):
        try:
            date_selected = self.calendar.get_date()
            date_selected = datetime.strptime(date_selected, "%d/%m/%y").strftime("%Y-%m-%d")

            # Update database with the state of each checkbox
            for checkbutton, var, task in self.checkbuttons:
                completed = 'YES' if var.get() == 1 else 'NO'
                save_changes_query = sql.SQL("UPDATE tasks SET completed = %s WHERE task = %s AND date = %s")
                data_to_insert = (completed, task, date_selected)
                self.cursor.execute(save_changes_query, data_to_insert)

            self.conn.commit()
            messagebox.showinfo("Save Changes", "Changes saved successfully.")
        except Exception as e:
            messagebox.showerror("Failed", f"An error occurred: {e}")

    def add_new_task(self):
        try:
            new_task = self.task_entry.get()
            date_selected = self.calendar.get_date()

            # Insert new task into database
            add_new_task_query = sql.SQL("INSERT INTO tasks(task, completed, date) VALUES (%s, %s, %s)")
            data_to_insert = (new_task, "NO", date_selected)
            self.cursor.execute(add_new_task_query, data_to_insert)

            self.conn.commit()

            self.update_task_list(date_selected)
            self.task_entry.delete(0, END)
        except Exception as e:
            messagebox.showerror("Failed", f"Data not saved because: {e}")


if __name__ == "__main__":
    root = Tk()
    app = TaskManager(root)
    root.mainloop()
