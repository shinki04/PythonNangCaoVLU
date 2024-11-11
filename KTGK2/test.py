import tkinter as tk
from tkinter import ttk

def generate_report():
    # Thực hiện các logic để tạo báo cáo ở đây
    print("Tạo báo cáo...")

# Tạo cửa sổ chính
root = tk.Tk()
root.title("Ứng dụng tạo báo cáo")

# Tạo các nhãn và ô nhập liệu
file_label = tk.Label(root, text="File:")
file_entry = tk.Entry(root)

format_label = tk.Label(root, text="File format:")
format_combobox = ttk.Combobox(root, values=["Example", "MBank", "Bos", "Alianz"])

time_period_label = tk.Label(root, text="Time period")
year_from_label = tk.Label(root, text="Year:")
year_from_entry = tk.Spinbox(root, from_=2017, to=2025)
month_from_label = tk.Label(root, text="Month:")
month_from_entry = tk.Spinbox(root, from_=1, to=12)
year_to_label = tk.Label(root, text="Year:")
year_to_entry = tk.Spinbox(root, from_=2017, to=2025)
month_to_label = tk.Label(root, text="Month:")
month_to_entry = tk.Spinbox(root, from_=1, to=12)
offset_label = tk.Label(root, text="Offset:")
offset_spinbox = tk.Spinbox(root, from_=1, to=12)

# Nút tạo báo cáo
generate_button = tk.Button(root, text="Generate report", command=generate_report)

# Sắp xếp các thành phần bằng grid()
file_label.grid(row=0, column=0)
file_entry.grid(row=0, column=1, columnspan=3)

format_label.grid(row=1, column=0)
format_combobox.grid(row=1, column=1, columnspan=3)

time_period_label.grid(row=2, column=0)
year_from_label.grid(row=3, column=0)
year_from_entry.grid(row=3, column=1)
month_from_label.grid(row=3, column=2)
month_from_entry.grid(row=3, column=3)
year_to_label.grid(row=4, column=0)
year_to_entry.grid(row=4, column=1)
month_to_label.grid(row=4, column=2)
month_to_entry.grid(row=4, column=3)
offset_label.grid(row=1, column=4)
offset_spinbox.grid(row=1, column=5)

generate_button.grid(row=5, column=0, columnspan=6)

root.mainloop()