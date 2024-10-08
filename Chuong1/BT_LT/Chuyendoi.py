import tkinter as tk
from tkinter import ttk

# # Hàm chuyển đổi


def convert():
    input_value = float(entry.get())
    from_unit = from_combo.get()
    to_unit = to_combo.get()

#     # Chuyển đổi từ km
#     if from_unit == 'Kilometers (km)':
#         if to_unit == 'Centimeters (cm)':
#             result = input_value * 100000
#         elif to_unit == 'Millimeters (mm)':
#             result = input_value * 1000000
#         else:
#             result = input_value

#     # Chuyển đổi từ cm
#     elif from_unit == 'Centimeters (cm)':
#         if to_unit == 'Kilometers (km)':
#             result = input_value / 100000
#         elif to_unit == 'Millimeters (mm)':
#             result = input_value * 10
#         else:
#             result = input_value
#     # Chuyển đổi từ mm
#     elif from_unit == 'Millimeters (mm)':
#         if to_unit == 'Kilometers (km)':
#             result = input_value / 1000000
#         elif to_unit == 'Centimeters (cm)':
#             result = input_value / 10
#         else:
#             result = input_value
    # Hệ số chuyển đổi giữa các đơn vị
    conversion_factors = {
        'Kilometers (km)': {'Kilometers (km)': 1, 'Centimeters (cm)': 100000, 'Millimeters (mm)': 1000000},
        'Centimeters (cm)': {'Kilometers (km)': 1/100000, 'Centimeters (cm)': 1, 'Millimeters (mm)': 10},
        'Millimeters (mm)': {'Kilometers (km)': 1/1000000, 'Centimeters (cm)': 1/10, 'Millimeters (mm)': 1}
    }

    # Tính kết quả dựa trên hệ số chuyển đổi
    result = input_value * conversion_factors[from_unit][to_unit]

    # Hiển thị kết quả
#     .rstrip('0'): Xóa các số 0 ở cuối.
#     .rstrip('.'): Xóa dấu chấm nếu không có phần thập phân nào sau dấu chấm.
    result_label.grid(row=5, column=0, columnspan=2, pady=10, sticky="N")
    result_label.config(text=f"Result: {format(
        result, '.10f').rstrip('0').rstrip('.')} {to_unit}")
    re.set(result)


# Tạo cửa sổ chính
window = tk.Tk()
window.title("Distance Converter")
# window.geometry("400x200")

# Tiêu đề
title_label = tk.Label(
    window, text="Convert Between Kilometers, Centimeters, and Millimeters")
title_label.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Nhập số liệu
entry_label = tk.Label(window, text="From:")
entry_label.grid(row=1, column=0)

entry = tk.Entry(window, width=10)
entry.grid(row=1, column=1)

# # Chọn đơn vị gốc
# from_label = tk.Label(window, text="From:")
# from_label.grid(row=1, column=0, padx=10, pady=5)

from_combo = ttk.Combobox(window, width=15, state='readonly')
from_combo['value'] = (
    'Kilometers (km)', 'Centimeters (cm)', 'Millimeters (mm)')

from_combo.current(0)
from_combo.grid(row=1, column=2)

# Chọn đơn vị đích
to_label = tk.Label(window, text="To:")
to_label.grid(row=2, column=0)

re = tk.IntVar()
entry_to = tk.Entry(window, width=10, state="disabled", textvariable=re)
entry_to.grid(row=2, column=1)

to_combo = ttk.Combobox(window, width=15, state='readonly')
to_combo['value'] = ('Kilometers (km)', 'Centimeters (cm)', 'Millimeters (mm)')
to_combo.current(0)
to_combo.grid(row=2, column=2, pady=3)

# Nút chuyển đổi
convert_button = tk.Button(window, text="Convert", command=convert)
convert_button.grid(row=4, column=0, columnspan=3, pady=10)

# Nhãn hiển thị kết quả
result_label = tk.Label(window, text="Result: ")
result_label.grid(row=5, column=0, columnspan=2, pady=10, sticky="N")

# Chạy ứng dụng
window.mainloop()
