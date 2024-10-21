import psycopg2
from tkinter import messagebox

class Dbconnection:
    def __init__(self, db_name, user, password, host, port):
        self.db_name = db_name
        self.user = user
        self.password = password
        self.host = host
        self.port = port
        self.conn = None  # Kết nối cơ sở dữ liệu ban đầu là None
        self.cur = None   # Con trỏ cơ sở dữ liệu ban đầu là None

    def connect_db(self):
        """Kết nối tới cơ sở dữ liệu PostgreSQL"""
        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name,
                user=self.user,
                password=self.password,
                host=self.host,
                port=self.port
            )
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")

    def disconnect_db(self):
        """Ngắt kết nối với cơ sở dữ liệu PostgreSQL"""
        try:
            if self.cur:
                self.cur.close()  # Đóng con trỏ nếu tồn tại
            if self.conn:
                self.conn.close()  # Đóng kết nối nếu tồn tại
                messagebox.showinfo("Success", "Disconnected from the database successfully!")
            else:
                messagebox.showwarning("Warning", "No active connection to disconnect.")
        except Exception as e:
            messagebox.showerror("Error", f"Error disconnecting from the database: {e}")
