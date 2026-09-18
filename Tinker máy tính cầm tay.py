from tkinter import *
from tkinter import Tk
import math

def btnclick(numbers): #Hàm này được gọi khi một nút được nhấn, nó sẽ thêm số hoặc toán tử vào biến toàn cục operator và cập nhật hiển thị
    global operator  #Sử dụng biến toàn cục để lưu toán tử
    operator = operator + str(numbers)
    Text_Input.set(operator)

def btnclear():   #Hàm này được gọi khi nút "C" được nhấn, nó sẽ xóa biến toàn cục operator và cập nhật hiển thị
    global operator
    operator=""
    Text_Input.set("0") # Trả về 0 khi xóa trắng giống Windows Calc
    
def btnequal():      #Hàm này được gọi khi nút "=" được nhấn, nó sẽ tính toán kết quả của biểu thức trong biến toàn cục operator và cập nhật hiển thị
    global operator
    if not operator: 
        return
    try:
        sumup=str(eval(operator))
        Text_Input.set(sumup)
        operator=sumup # Lưu lại để tính tiếp
    except Exception:
        Text_Input.set("Lỗi")
        operator=""

def btnbackspace():
    global operator
    operator = operator[:-1]  # Cắt bỏ ký tự cuối cùng
    if operator == "":
        Text_Input.set("0")
    else:
        Text_Input.set(operator)   # Cập nhật lại màn hình hiển thị

def btnsqrt():
    global operator   #Hàm này được gọi khi nút "√" được nhấn, nó sẽ tính căn bậc hai của số hiện tại
    try:
        # Lấy giá trị hiện tại, nếu trống thì mặc định là 0
        current_val = float(Text_Input.get()) if Text_Input.get() and Text_Input.get() != "Lỗi" else 0
        if current_val < 0:
            Text_Input.set("Lỗi (Số âm)")
            operator = ""
        else:
            res = math.sqrt(current_val)     # Tính căn bậc hai
            if res.is_integer():
                res = int(res)
            Text_Input.set(str(res))
            operator = str(res)    # Lưu lại kết quả để tính toán tiếp
    except Exception:
        Text_Input.set("Lỗi")
        operator = ""

cal = Tk()   #Tạo một cửa sổ mới
cal.title("Máy tính cầm tay")  #Đặt tiêu đề cho cửa sổ
cal.geometry("340x500") # Kích thước cửa sổ gọn lại
cal.resizable(False, False)
cal.configure(bg="#202020") # Nền tối giống Windows Calc

operator = ""  #Biến toàn cục để lưu toán tử  
Text_Input = StringVar()  #Biến để lưu giá trị nhập vào
Text_Input.set("0") # Mặc định hiển thị số 0

# Ô nhập liệu / Hiển thị kết quả
txtdisplay = Entry(cal, font=('Segoe UI', 36, 'bold'), textvariable=Text_Input, bd=0, insertwidth=0, bg='#202020', fg='#ffffff', justify='right', highlightthickness=0)
txtdisplay.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=30, pady=10, sticky="nsew")

# Cấu hình màu sắc theo ảnh Windows Calculator
btn_params = {'bd': 0, 'font': ('Segoe UI', 16)}
num_bg = '#3b3b3b'   # Màu xám vừa cho số
op_bg = '#323232'    # Màu xám đậm cho toán tử
equal_bg = '#4cc2ff' # Màu xanh dương cho dấu bằng
equal_fg = '#000000' # Chữ đen cho dấu bằng
fg_white = '#ffffff' # Chữ trắng cho các nút khác

# Hàm tạo nút
def create_button(text, row, col, bg_color, command, fg_color=fg_white):
    Button(cal, text=text, bg=bg_color, fg=fg_color, command=command, activebackground='#505050', activeforeground=fg_color, **btn_params).grid(row=row, column=col, sticky="nsew", padx=2, pady=2)

# Cấu hình grid để các nút co giãn đều nhau
for i in range(1, 6):
    cal.grid_rowconfigure(i, weight=1)
for i in range(4):
    cal.grid_columnconfigure(i, weight=1)

# Hàng 1: C, √, ←, /
create_button('C', 1, 0, op_bg, btnclear)
create_button('√', 1, 1, op_bg, btnsqrt)
create_button('←', 1, 2, op_bg, btnbackspace)
create_button('/', 1, 3, op_bg, lambda: btnclick("/"))

# Hàng 2: 7, 8, 9, *
create_button('7', 2, 0, num_bg, lambda: btnclick(7))
create_button('8', 2, 1, num_bg, lambda: btnclick(8))
create_button('9', 2, 2, num_bg, lambda: btnclick(9))
create_button('*', 2, 3, op_bg, lambda: btnclick("*"))

# Hàng 3: 4, 5, 6, -
create_button('4', 3, 0, num_bg, lambda: btnclick(4))
create_button('5', 3, 1, num_bg, lambda: btnclick(5))
create_button('6', 3, 2, num_bg, lambda: btnclick(6))
create_button('-', 3, 3, op_bg, lambda: btnclick("-"))

# Hàng 4: 1, 2, 3, +
create_button('1', 4, 0, num_bg, lambda: btnclick(1))
create_button('2', 4, 1, num_bg, lambda: btnclick(2))
create_button('3', 4, 2, num_bg, lambda: btnclick(3))
create_button('+', 4, 3, op_bg, lambda: btnclick("+"))

# Hàng 5: xʸ, 0, ., =
create_button('xʸ', 5, 0, op_bg, lambda: btnclick("**"))
create_button('0', 5, 1, num_bg, lambda: btnclick(0))
create_button('.', 5, 2, num_bg, lambda: btnclick("."))
create_button('=', 5, 3, equal_bg, btnequal, fg_color=equal_fg)

cal.mainloop()  #Bắt đầu vòng lặp chính của giao diện