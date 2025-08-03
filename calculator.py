import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

def calculate(operation):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())

        if operation == "add":
            result = num1 + num2
        elif operation == "subtract":
            result = num1 - num2
        elif operation == "multiply":
            result = num1 * num2
        elif operation == "divide":
            if num2 == 0:
                result = "Cannot divide by zero!"
            else:
                result = num1 / num2

        result_var.set(f"Result: {result:.4f}".rstrip('0').rstrip('.') if isinstance(result, float) else f"Result: {result}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers!")

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("350x450")
root.resizable(False, False)
root.configure(bg="#f5f5f5")

# Custom font
title_font = Font(family="Helvetica", size=14, weight="bold")
button_font = Font(family="Arial", size=10)
result_font = Font(family="Courier New", size=12, weight="bold")

# Style configuration
style = ttk.Style()
style.configure("TButton", padding=6, relief="flat", background="#e1e1e1", font=button_font)
style.map("TButton", 
          background=[("active", "#d1d1d1")], 
          relief=[("active", "sunken")])

# Header frame
header_frame = tk.Frame(root, bg="#3f51b5", height=60)
header_frame.pack(fill="x")
header_frame.pack_propagate(False)

tk.Label(header_frame, text="Calculator", font=title_font, bg="#3f51b5", fg="white").pack(expand=True)

# Main content frame
content_frame = tk.Frame(root, bg="#f5f5f5", padx=20, pady=20)
content_frame.pack(expand=True, fill="both")

# Entry fields
tk.Label(content_frame, text="First Number:", bg="#f5f5f5", anchor="w").grid(row=0, column=0, sticky="ew", pady=(0, 5))
entry1 = ttk.Entry(content_frame, font=button_font)
entry1.grid(row=1, column=0, sticky="ew", pady=(0, 15))

tk.Label(content_frame, text="Second Number:", bg="#f5f5f5", anchor="w").grid(row=2, column=0, sticky="ew", pady=(0, 5))
entry2 = ttk.Entry(content_frame, font=button_font)
entry2.grid(row=3, column=0, sticky="ew", pady=(0, 20))

# Button frame
button_frame = tk.Frame(content_frame, bg="#f5f5f5")
button_frame.grid(row=4, column=0, sticky="ew")

ttk.Button(button_frame, text="Add", command=lambda: calculate("add")).pack(side="left", expand=True, padx=2)
ttk.Button(button_frame, text="Subtract", command=lambda: calculate("subtract")).pack(side="left", expand=True, padx=2)
ttk.Button(button_frame, text="Multiply", command=lambda: calculate("multiply")).pack(side="left", expand=True, padx=2)
ttk.Button(button_frame, text="Divide", command=lambda: calculate("divide")).pack(side="left", expand=True, padx=2)

# Result display
result_var = tk.StringVar()
result_var.set("Result: ")
result_label = ttk.Label(content_frame, textvariable=result_var, font=result_font, background="#f5f5f5", 
                        relief="sunken", padding=10, anchor="center")
result_label.grid(row=5, column=0, sticky="ew", pady=(20, 0))

# Configure grid weights
content_frame.columnconfigure(0, weight=1)

root.mainloop()
