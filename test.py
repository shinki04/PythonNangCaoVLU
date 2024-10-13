import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2
from psycopg2 import sql

class TableApp():
    def __init__(self, root):
        # Khởi tạo lớp cha (DBconnection)
        self.root = root
        self.root.title("Bảng dữ liệu sinh viên")
        self.db_name = tk.StringVar(value='dbtest')
        self.user = tk.StringVar(value='postgres')
        self.password = tk.StringVar(value='123456')
        self.host = tk.StringVar(value='localhost')
        self.port = tk.StringVar(value='5432')
        self.table_name = tk.StringVar(value='sinhvien')
        
        # Giao diện connect db
        self.widgets_connect() 

    def widgets_connect(self):
        connection_frame = tk.Frame(self.root)
        connection_frame.pack(pady=10)

        tk.Label(connection_frame, text="DB Name:").grid(row=0, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.db_name).grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(connection_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Host:").grid(row=3, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.host).grid(row=3, column=1, padx=5, pady=5)

        tk.Label(connection_frame, text="Port:").grid(row=4, column=0, padx=5, pady=5)
        tk.Entry(connection_frame, textvariable=self.port).grid(row=4, column=1, padx=5, pady=5)

        tk.Button(connection_frame, text="Connect", command= self.connect_db).grid(row=5, columnspan=2, pady=10)

    def widgets_login(self):
        login_frame = tk.Frame(self.root)
        tk.Label(login_frame, text="User:").grid(row=1, column=0, padx=5, pady=5)
        tk.Entry(login_frame, textvariable=self.user).grid(row=1, column=1, padx=5, pady=5)

        tk.Label(login_frame, text="Password:").grid(row=2, column=0, padx=5, pady=5)
        tk.Entry(login_frame, textvariable=self.password, show="*").grid(row=2, column=1, padx=5, pady=5)
    
    
    def widgets_manage(self):
        # Khung chứa bảng
        table_frame = tk.Frame(self.root)
        table_frame.pack(pady=10)

        # Tạo bảng Treeview
        self.data_table = ttk.Treeview(table_frame, columns=("MSSV", "Tên Sinh Viên"), show="headings", height=10)
        self.data_table.heading("MSSV", text="MSSV")
        self.data_table.heading("Tên Sinh Viên", text="Tên Sinh Viên")
        self.data_table.column("MSSV", width=100)
        self.data_table.column("Tên Sinh Viên", width=200)
        self.data_table.pack()

        # Khung chứa các ô nhập liệu
        form_frame = tk.Frame(self.root)
        form_frame.pack(pady=10)

        # Nhãn và ô nhập MSSV
        ttk.Label(form_frame, text="MSSV : ").grid(row=0, column=0, padx=5, pady=5)
        self.mssv = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.mssv).grid(row=0, column=1, padx=5, pady=5)

        # Nhãn và ô nhập Họ Tên
        ttk.Label(form_frame, text="Họ Tên : ").grid(row=1, column=0, padx=5, pady=5)
        self.hoten = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.hoten).grid(row=1, column=1, padx=5, pady=5)

        # Nút để thêm hàng mới
        add_button = ttk.Button(self.root, text="Thêm hàng mới", command=self.on_add_button_click)
        add_button.pack(pady=10)
        
        # Nút để load data
        load_button = ttk.Button(self.root, text="Load data", command=self.load_data)
        load_button.pack(pady=10)
        # Nút để xóa data đang chọn
        delete_button = ttk.Button(self.root, text="Xóa hàng đang chọn", command=self.delete_selected_row)
        delete_button.pack(pady=10)
        
        # Nút để xóa data trong ô
        delete_input_button = ttk.Button(self.root, text="Xóa mssv đang nhập", command= lambda:self.delete_data(self.mssv.get()))
        delete_input_button.pack(pady=10)


    def on_add_button_click(self):
        """Thêm sinh viên mới vào cơ sở dữ liệu và bảng Treeview"""
        mssv = self.mssv.get().strip()
        hoten = self.hoten.get().strip()

        if self.validate_input(mssv, hoten):
            self.insert_data()
            self.add_table(mssv, hoten)
            self.clear_inputs()

    def validate_input(self, mssv, hoten):
        """Kiểm tra đầu vào không được để trống."""
        if not mssv or not hoten:
            messagebox.showwarning("Lỗi nhập liệu", "MSSV và Họ Tên không được để trống.")
            return False
        return True

    def add_table(self, mssv, hoten):
        """Thêm hàng mới vào bảng Treeview."""
        new_row = (mssv, hoten)
        self.data_table.insert("", tk.END, values=new_row)

    def clear_inputs(self):
        """Xóa các ô nhập liệu sau khi thêm dữ liệu thành công."""
        self.mssv.set("")
        self.hoten.set("")
    
    def connect_db(self):
        """Kết nối tới cơ sở dữ liệu PostgreSQL"""
        try:
            self.conn = psycopg2.connect(
                dbname=self.db_name.get(),
                user=self.user.get(),
                password=self.password.get(),
                host=self.host.get(),
                port=self.port.get()
            )
            self.cur = self.conn.cursor()
            messagebox.showinfo("Success", "Connected to the database successfully!")
            return True
        except Exception as e:
            messagebox.showerror("Error", f"Error connecting to the database: {e}")
            return False
        
    def load_data(self):
        """Tải dữ liệu từ cơ sở dữ liệu và hiển thị trong bảng Treeview"""
        try:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(query)
            rows = self.cur.fetchall()
            self.data_table.delete(*self.data_table.get_children())  # Xóa toàn bộ dữ liệu hiện tại
            for row in rows:
                self.data_table.insert("", tk.END, values=row)  # Thêm từng hàng dữ liệu
        except Exception as e:
            messagebox.showerror("Error", f"Error loading data: {e}")

    def insert_data(self):
        """Chèn dữ liệu sinh viên vào cơ sở dữ liệu"""
        try:
            insert_query = sql.SQL("INSERT INTO {} (mssv, hoten) VALUES (%s, %s)").format(sql.Identifier(self.table_name.get()))
            data_to_insert = (self.mssv.get(), self.hoten.get())
            self.cur.execute(insert_query, data_to_insert)
            self.conn.commit()
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

    # def delete_data(self):
    #     """Xóa sinh viên khỏi cơ sở dữ liệu"""
    #     try:
    #         delete_query = sql.SQL("DELETE FROM {} WHERE mssv = %s").format(sql.Identifier(self.table_name.get()))
    #         data_to_delete = (self.mssv.get(),)  # MSSV cần xóa
    #         self.cur.execute(delete_query, data_to_delete)
    #         self.conn.commit()
    #         messagebox.showinfo("Success", "Data deleted successfully!")
    #     except Exception as e:
    #         messagebox.showerror("Error", f"Error deleting data: {e}")

    def delete_selected_row(self):
        """Xóa hàng đang được chọn trong Treeview"""
        try:
            selected_items = self.data_table.selection()  # Lấy tất cả các hàng đang được chọn
            if not selected_items:
                messagebox.showwarning("Lỗi", "Vui lòng chọn hàng để xóa.")
                return

            for item in selected_items:
                values = self.data_table.item(item, 'values')  # Lấy dữ liệu của hàng đã chọn
                mssv = values[0]  # Giả sử MSSV nằm ở cột đầu tiên
                # Xóa dữ liệu trong cơ sở dữ liệu
                self.delete_data(mssv)

                # Xóa hàng từ Treeview (chỉ xóa nếu nó còn tồn tại)
                if item in self.data_table.get_children():
                    self.data_table.delete(item)
                else:
                    messagebox.showwarning("Lỗi", f"Item {item} không tồn tại trong bảng.")
            
            messagebox.showinfo("Thành công", "Đã xóa hàng thành công.")
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting selected row: {e}")

    def delete_data(self, mssv):
        """Xóa dữ liệu sinh viên khỏi cơ sở dữ liệu theo MSSV"""
        try:
            delete_query = sql.SQL("DELETE FROM {} WHERE mssv = %s").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(delete_query, (mssv,))
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Error", f"Error deleting data from database: {e}")

        
    
    
    def check_login(self):
        """Chèn dữ liệu sinh viên vào cơ sở dữ liệu"""
        try:
            query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(self.table_name.get()))
            self.cur.execute(query)
            rows = self.cur.fetchall()
            for i in rows :
                print(i)
            messagebox.showinfo("Success", "Data inserted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Error inserting data: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    TableApp(root)
    root.mainloop()
