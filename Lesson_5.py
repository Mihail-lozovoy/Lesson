import tkinter as tk


def add():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    res = num1 + num2
    answer_entry.delete(0, "end")
    answer_entry.insert(0, res)










window = tk.Tk()
window.title("Калькулятор")
window.geometry("400x400")
window.resizable(False, False)
button_add = tk.Button(window, text="+", width=3, height=2, command=add)
button_add.place(x=125, y=200)
button_sub = tk.Button(window, text="-", width=3, height=2)
button_sub.place(x=175, y=200)
button_mul = tk.Button(window, text="*", width=3, height=2)
button_mul.place(x=225, y=200)
button_div = tk.Button(window, text="/", width=3, height=2)
button_div.place(x=275, y=200)
number1_entry = tk.Entry(window, width=30, )
number1_entry.place(x=125, y=50)
number2_entry = tk.Entry(window, width=30, )
number2_entry.place(x=125, y=130)
answer_entry = tk.Entry(window, width=30, )
answer_entry.place(x=125, y=300)
number1_entry = tk.Label(window, text="Введите первое число:")
number1_entry.place(x=125, y=25)
number2_entry = tk.Label(window, text="Введите второе число:")
number2_entry.place(x=125, y=105)
answer_entry = tk.Label(window, text="Результат:")
answer_entry.place(x=125, y=275)
window.mainloop()