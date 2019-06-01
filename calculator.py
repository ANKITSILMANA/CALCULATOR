#----------------------CALCULATOR---------------------------------------


import tkinter as tk

mainWindow = tk.Tk()
mainWindow.title("CALCULATOR")

label = tk.Label(mainWindow, text="Enter First number",pady=(10))
label.pack()

name_field = tk.Entry(mainWindow)
name_field.pack()

label1 = tk.Label(mainWindow, text="Enter Second number")
label1.pack()

name_field1 = tk.Entry(mainWindow)
name_field1.pack()

label2 = tk.Label (mainWindow, text="Operation")
label2.pack()


def addition():
    try:
        first = int(name_field.get())
        second = int(name_field1.get())
        result = first+second
        # print(first+second)
        result_label.config(text="operation result is:"+ str(result))
    except ValueError:
        result_label.config(text='exception input keyword is not an integer')


def subtraction():
    try:
        first = int(name_field.get())
        second = int(name_field1.get())
        # print(first - second)
        result = first - second
        result_label.config(text="operation result is:" + str(result))
    except ValueError:
        result_label.config(text='exception input keyword is not an integer')

def multiplication():
    try:
        first = int(name_field.get())
        second = int(name_field1.get())
        # print(first * second)
        result = first * second
        result_label.config(text="operation result is:" + str(result))
    except ValueError:
        result_label.config(text='exception input keyword is not an integer')

def division():
    try:
        first = int(name_field.get())
        second = int(name_field1.get())
        # print(first / second)
        result = first / second
        result_label.config(text="operation result is:" + str(result))
    except ValueError:
        result_label.config(text='exception input keyword is nt an integer')
    except ZeroDivisionError:
        result_label.config(text='cannot divide by zero')

addition_button = tk.Button(mainWindow, text="+", command=lambda: addition ())
addition_button.pack()

subtraction_button = tk.Button(mainWindow, text="-", command=lambda: subtraction ())
subtraction_button.pack()


multiplication_button = tk.Button(mainWindow, text="*", command=lambda: multiplication ())
multiplication_button.pack()

division_button = tk.Button(mainWindow, text="/", command=lambda: division ())
division_button.pack()

result_label=tk.Label(mainWindow,text="Text is:")
result_label.pack()

mainWindow.mainloop()
