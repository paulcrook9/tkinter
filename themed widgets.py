import tkinter as tk
import tkinter.messagebox as messagebox

# random comment

def button_click(number):
    current = display.get()
    display.delete(0, tk.END)
    display.insert(0, current + str(number))

def button_clear():
    display.delete(0, tk.END)

def button_equal():
    try:
        expression = display.get()
        result = eval(expression)
        display.delete(0, tk.END)
        display.insert(0, str(result))
    except (SyntaxError, ZeroDivisionError):
        messagebox.showerror("Error", "Invalid input or division by zero.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")


window = tk.Tk()
window.title("Simple Calculator")
window.configure(bg="#f0f0f0")

display = tk.Entry(window, width=25, borderwidth=5, font=("Arial", 16), justify="right")
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=5)
display.configure(bg="white")

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "=", "+"
]

row_num = 1
col_num = 0

for button_text in buttons:
    if button_text == "=":
        button = tk.Button(window, text=button_text, padx=30, pady=20, font=("Arial", 14), bg="#4CAF50", fg="white", command=button_equal)
    elif button_text in ["/", "*", "-", "+"]: # Corrected handling of operators
        button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 14), bg="#FF9800", fg="white", command=lambda op=button_text: button_click(op))
    else:
        button = tk.Button(window, text=button_text, padx=20, pady=20, font=("Arial", 14), command=lambda num=button_text: button_click(num))

    button.grid(row=row_num, column=col_num, padx=5, pady=5)
    col_num += 1
    if col_num > 3:
        col_num = 0
        row_num += 1

clear_button = tk.Button(window, text="C", padx=20, pady=20, font=("Arial", 14), bg="#f44336", fg="white", command=button_clear)
clear_button.grid(row=5, column=0, padx=5, pady=5)

window.mainloop()