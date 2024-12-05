import tkinter as tk
from tkinter import messagebox

def validate_on_button_click():
    """Validate input when the button is clicked."""
    user_input = entry.get()  # Get the current text from the Entry widget
    if user_input.isdigit():
        messagebox.showinfo("Success", "Input is valid!")
    else:
        messagebox.showerror("Invalid Input", "Please enter a valid number!")

root = tk.Tk()
root.title("Validation on Button Click")

# Create an Entry widget
entry = tk.Entry(root)
entry.pack(pady=10)

# Create a button to validate input
validate_button = tk.Button(root, text="Submit", command=validate_on_button_click)
validate_button.pack(pady=10)

root.mainloop()
