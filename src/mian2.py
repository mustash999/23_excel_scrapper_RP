import tkinter as tk
from tkinter import ttk
import get_info as gi

def on_dropdown_selection(event):
    selected_item = dropdown_var.get()
    status_label.config(text=f"Selected: {selected_item}")

# Create the main application window
root = tk.Tk()
root.title("Dropdown List Example")

# Create a label
instruction_label = tk.Label(root, text="Select an item:")
instruction_label.pack(pady=10)

# Create a dropdown variable and set its initial value
dropdown_var = tk.StringVar(root)
dropdown_var.set("Item 1")

# Create a dropdown list with state set to "readonly"
dropdown = ttk.Combobox(root, textvariable=dropdown_var, state="readonly")
dropdown['values'] = gi.get_tabs('tests/File1.xlsx')
dropdown.pack()
dropdown.state(['readonly'])


# Bind the selection event to a function
dropdown.bind("<<ComboboxSelected>>", on_dropdown_selection)

