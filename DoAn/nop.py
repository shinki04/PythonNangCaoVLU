import psycopg2
from psycopg2 import sql
import pandas as pd
from tkinter import Tk, Label, Button, Entry, Frame, messagebox, Checkbutton, IntVar, ttk, Menu, filedialog, simpledialog
from tkcalendar import Calendar
from datetime import datetime

import tkinter as tk


class TaskManager:
    def __init__(self, root):
        now = datetime.now()
        self.root = root
        self.root.title("Task Manager")
        self.root.iconbitmap('DoAn/logo.ico')

        # Flag to track changes
        self.changed = False  # To track if any task's status has been changed

        # File menu
        self.menu_bar = Menu(self.root)
        file_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Xuất Excel", command=self.export_to_excel)
        file_menu.add_command(label="Exit", command=self.quit_app)        
        # Help_menux
        help_menu = Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.msg_box_info)
        self.root.config(menu=self.menu_bar)

        # Calendar
        cal_frame = Frame(root)
        cal_frame.grid(row=0, column=0, columnspan=3, padx=20)
        self.calendar = Calendar(cal_frame, font=("Arial", 12), selectmode="day", year=now.year, month=now.month, day=now.day)
        self.calendar.pack(expand=True)
        self.calendar.bind("<<CalendarSelected>>", self.calendar_date_changed)



        task_list = ttk.LabelFrame(self.root,height=60)
        task_list.grid(column=3, row=0, padx=50 ,pady=20)
        
        
        
        # Task Entry and Buttons
        Label(task_list, text="Task:").grid(row=0, column=0,padx=20 , pady=20)
        self.task = tk.StringVar()
        self.task_entry = Entry(task_list, textvariable=self.task)
        self.task_entry.grid(row=0, column=1)
                # Button "Today" to go back to the current day
        self.today_button = Button(task_list, text="Today", command=self.go_to_today)
        self.today_button.grid(row=1, column=0, padx=20, pady=10)
        
        self.add_button = Button(task_list, text="Add Task", command=self.add_new_task)
        self.add_button.grid(row=2, column=0)

        self.save_button = Button(task_list, text="Save Changes", command=self.save_changes)
        self.save_button.grid(row=1, column=1)

        # Task List (using Checkbuttons)
        self.task_frame = ttk.LabelFrame(task_list,text="To do list")
        self.task_frame.grid(row=3, column=0, columnspan=3 , padx=20 , pady=20)

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
        # Clear previous widgets
        for widget in self.task_frame.winfo_children():
            widget.destroy()

        # Query tasks for the selected date
        query = "SELECT id, task, completed FROM tasks WHERE date = %s"
        self.cursor.execute(query, (date,))
        results = self.cursor.fetchall()

        # Create checkbuttons for each task
        self.checkbuttons = []  # Clear the checkbuttons list before adding new ones
        row = 0  # Start placing widgets in the first row
        for task_id, task, completed in results:
            var = IntVar(value=1 if completed == 'YES' else 0)
            checkbutton = Checkbutton(self.task_frame, text=task, variable=var)
            checkbutton.grid(row=row, column=0, sticky="w")

            # Add Edit and Delete buttons next to each task
            edit_button = Button(self.task_frame, text="Edit", command=lambda task_id=task_id, task=task: self.edit_task(task_id, task))
            edit_button.grid(row=row, column=1, padx=5)

            delete_button = Button(self.task_frame, text="Delete", command=lambda task_id=task_id: self.delete_task(task_id))
            delete_button.grid(row=row, column=2, padx=5)

            self.checkbuttons.append((checkbutton, var, task_id))  # Store the id for future reference

            # Bind the checkbutton to the tracking function to detect changes
            var.trace("w", lambda *args, task_id=task_id: self.on_checkbox_change(task_id))

            row += 1  # Move to the next row after each task
    def on_checkbox_change(self, task_id):
        self.changed = True  # Mark that a change has occurred

    def save_changes(self):
        try:
            if not self.changed:
                messagebox.showinfo("No Changes", "No changes to save.")
                return

            date_selected = self.calendar.get_date()

            for i in range(len(self.checkbuttons)):
                checkbutton, var, task_id = self.checkbuttons[i]
                completed = 'YES' if var.get() == 1 else 'NO'

                # Update the completion status based on `id`
                update_query = sql.SQL("UPDATE tasks SET completed = %s WHERE id = %s")
                self.cursor.execute(update_query, (completed, task_id))

            self.conn.commit()
            self.changed = False  # Reset change tracking
            messagebox.showinfo("Save Changes", "Changes saved successfully.")
        except Exception as e:
            messagebox.showerror("Failed", f"Error saving changes: {e}")
            self.conn.rollback()

    def add_new_task(self):
        try:
            new_task = self.task.get()
            date_selected = self.calendar.get_date()

            # Insert new task into database
            add_new_task_query = sql.SQL("INSERT INTO tasks(task, completed, date) VALUES (%s, %s, %s)")
            data_to_insert = (new_task, "NO", date_selected)
            self.cursor.execute(add_new_task_query, data_to_insert)

            self.conn.commit()

            self.update_task_list(date_selected)
            self.changed = True  # Mark that a change has occurred after adding a task
            
            self.clear_input()
        except Exception as e:
            messagebox.showerror("Failed", f"Data not saved because: {e}")
            self.conn.rollback()

    def export_to_excel(self):
        try:
            # Lấy ngày hiện tại từ Calendar
            selected_date = self.calendar.get_date()

            # Chuyển đổi selected_date thành định dạng `yyyy-mm-dd`
            selected_date_dt = datetime.strptime(selected_date, "%d/%m/%y")

            # Tạo ngày đầu tiên và cuối cùng của tháng
            start_date = selected_date_dt.replace(day=1).strftime("%Y-%m-%d")
            end_date = selected_date_dt.replace(day=28).strftime("%Y-%m-%d")

            # Truy vấn tất cả các công việc trong tháng đã chọn
            self.cursor.execute(
                "SELECT task, completed, date FROM tasks WHERE date BETWEEN %s AND %s",
                (start_date, end_date)
            )
            results = self.cursor.fetchall()

            # Xuất ra file Excel
            if results:
                df = pd.DataFrame(results, columns=["Task", "Completed", "Date"])
            else:
                messagebox.showinfo("No Tasks", "No tasks found for the selected month.")

            # Mở hộp thoại lưu tệp để chọn đường dẫn lưu
            file_path = filedialog.asksaveasfilename(defaultextension= ".xlsx",
                                                     filetypes=[("Excel files", "*.xlsx"), ("All files", "*.*")],
                                                     title="Chọn nơi lưu file",
                                                     initialfile=f"tasks_{selected_date_dt.year}_{selected_date_dt.month}.xlsx"
                                                     )
            if file_path:  # Nếu người dùng không hủy
                # Xuất ra file Excel
                df.to_excel(file_path, index=True)
                messagebox.showinfo(
                    "Done", "The Excel file has been successfully exported")
            else:
                messagebox.showwarning("Cancel", "You have canceled saving the file.")

        except Exception as e:
            messagebox.showerror("Export Failed", f"Error exporting to Excel: {e}")


    def edit_task(self, task_id, current_task):
        new_task = simpledialog.askstring("Edit Task", "Enter new task name:", initialvalue=current_task)
        if new_task:
            try:
                # Update task in the database
                update_query = sql.SQL("UPDATE tasks SET task = %s WHERE id = %s")
                self.cursor.execute(update_query, (new_task, task_id))
                self.conn.commit()
                self.update_task_list(self.calendar.get_date())  # Refresh task list
                self.changed = True  # Mark that a change has occurred after editing
                messagebox.showinfo("Edit Task", "Task updated successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error updating task: {e}")
                self.conn.rollback()

    def delete_task(self, task_id):
        confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
        if confirm:
            try:
                # Delete task from the database
                delete_query = sql.SQL("DELETE FROM tasks WHERE id = %s")
                self.cursor.execute(delete_query, (task_id,))
                self.conn.commit()
                self.update_task_list(self.calendar.get_date())  # Refresh task list
                self.changed = True  # Mark that a change has occurred after deleting
                messagebox.showinfo("Delete Task", "Task deleted successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Error deleting task: {e}")
                self.conn.rollback()




    def msg_box_info(self):
        messagebox.showinfo("Info", "GUI made by Tran Van Hieu and Nguyen Lien Nhi")

    def quit_app(self):
        if self.changed:  # Nếu có thay đổi chưa lưu
            answer = messagebox.askyesno("Confirm", "You have unsaved changes. Do you want to exit?")
            if answer:
                self.root.destroy()
        else:
            self.root.destroy()


    def clear_input(self):
        self.task.set("")
        
    def go_to_today(self):
        # Set the calendar to the current date
        now = datetime.now()
        current_date = now.strftime("%d/%m/%y")
        self.calendar.selection_set(current_date)  # Set the selected date to today
        self.update_task_list(current_date)  # Update tasks for today

if __name__ == "__main__":
    root = Tk()
    app = TaskManager(root)
    root.mainloop()
