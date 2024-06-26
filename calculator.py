import tkinter as tk
from tkinter import *

# Create the main application window
app = tk.Tk()

# Set window properties
app.geometry("300x300")
app.title("Calculator")
app.maxsize(300, 300)
app.minsize(300, 300)

# Entry widget for displaying input/output
ent = Entry(app, width=38, font=('Arial', 10), borderwidth=5, relief=RIDGE)
ent.grid(pady=10, row=0, sticky="w", padx=15, ipady=7)  # Adjust ipady for vertical padding

# Function to delete the last character in the entry widget
def delete_last():
    a = ent.get()
    ent.delete(first=len(a) - 1, last="end")

# Function to evaluate the expression and display the result
def fresult():
    try:
        if ent.get() == "":
            pass
        elif ent.get()[0] == "0":
            ent.delete(0, "end")
        else:
            c_res = ent.get()
            c_res = eval(c_res)
            clearf()
            ent.insert("end", c_res)
    except ZeroDivisionError:
        clearf()
        ent.insert("end", "Undefined")

# Function to clear the entry widget
def clearf():
    ent.delete(0, "end")

# Buttons for numeric input and arithmetic operations
clean = Button(app, text="C", width=7, command=clearf, bg="black", fg="white")
clean.grid(row=0, sticky="w", padx=230, ipady=5)  # Adjust ipady for button height

Char_nine = Button(text="9", width=7, command=lambda: ent.insert("end", "9"), borderwidth=3)
Char_nine.grid(row=1, sticky="w", padx=15, pady=10)

Char_eight = Button(text="8", width=7, command=lambda: ent.insert("end", "8"), borderwidth=3)
Char_eight.grid(row=1, sticky="w", padx=85, pady=10)

Char_seven = Button(app, text="7", width=7, command=lambda: ent.insert("end", "7"), borderwidth=3)
Char_seven.grid(row=1, sticky="w", padx=155, pady=10)

Char_plus = Button(app, text="+", width=7, command=lambda: ent.insert("end", "+"), borderwidth=3)
Char_plus.grid(row=1, sticky="e", padx=230, pady=10)

Char_six = Button(text="6", width=7, command=lambda: ent.insert("end", "6"), borderwidth=3)
Char_six.grid(row=2, sticky="w", padx=15, pady=10)

Char_five = Button(text="5", width=7, command=lambda: ent.insert("end", "5"), borderwidth=3)
Char_five.grid(row=2, sticky="w", padx=85, pady=10)

Char_four = Button(app, text="4", width=7, command=lambda: ent.insert("end", "4"), borderwidth=3)
Char_four.grid(row=2, sticky="w", padx=155, pady=10)

Char_minus = Button(app, text="-", width=7, command=lambda: ent.insert("end", "-"), borderwidth=3)
Char_minus.grid(row=2, sticky="e", padx=230, pady=10)

Char_three = Button(text="3", width=7, command=lambda: ent.insert("end", "3"), borderwidth=3)
Char_three.grid(row=3, sticky="w", padx=15, pady=10)

Char_two = Button(text="2", width=7, command=lambda: ent.insert("end", "2"), borderwidth=3)
Char_two.grid(row=3, sticky="w", padx=85, pady=10)

Char_one = Button(app, text="1", width=7, command=lambda: ent.insert("end", "1"), borderwidth=3)
Char_one.grid(row=3, sticky="w", padx=155, pady=10)

Char_multiply = Button(app, text="*", width=7, command=lambda: ent.insert("end", "*"), borderwidth=3)
Char_multiply.grid(row=3, sticky="e", padx=230, pady=10)

Char_zero = Button(text="0", width=7, command=lambda: ent.insert("end", "0"), borderwidth=3)
Char_zero.grid(row=4, sticky="w", padx=15, pady=10)

Char_double_zero = Button(text="00", width=7, command=lambda: ent.insert("end", "00"), borderwidth=3)
Char_double_zero.grid(row=4, sticky="w", padx=85, pady=10)

Char_dot = Button(app, text=".", width=7, command=lambda: ent.insert("end", "."), borderwidth=3)
Char_dot.grid(row=4, sticky="w", padx=155, pady=10)

Char_divide = Button(app, text="/", width=7, command=lambda: ent.insert("end", "/"), borderwidth=3)
Char_divide.grid(row=4, sticky="e", padx=230, pady=10)

result = Button(app, text="=", width=17, command=fresult, bg="black", fg="white", borderwidth=3)
result.grid(row=5, sticky="w", padx=15, pady=10)

Char_modulus = Button(app, text="%", width=7, command=lambda: ent.insert("end", "%"), borderwidth=3)
Char_modulus.grid(row=5, sticky="e", padx=230, pady=10)

delete_button = Button(app, text="Del", width=7, command=delete_last, borderwidth=3)
delete_button.grid(row=5, sticky="w", padx=155, pady=10)

# Start the main event loop
app.mainloop()
