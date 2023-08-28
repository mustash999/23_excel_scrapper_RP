import tkinter as tk

def on_change(*args):
    print("Entry changed to:", var.get())

root = tk.Tk()

var = tk.StringVar()
var.trace_add("write", on_change)

entry = tk.Entry(root, textvariable=var)
entry.pack()

root.mainloop()