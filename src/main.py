import tkinter as tk
from tkinter import filedialog
import splash
from summerizer import summarize
from tkinter import messagebox
import os

splash.splash()

def open_folder_dialog():
    folder_path = filedialog.askdirectory()
    label.config(text=folder_path)
    width= label.winfo_width()
    text.config(width=width)
    


def execute():
    month= text.get()
    folder= label.cget("text")
    try:
        summarize(month, folder)
        messagebox.showinfo ( 'summarizer', 'export done succesfully ')
    except ValueError:
        messagebox.showerror( 'error', 'Oops something went wrong !!')


root = tk.Tk()
#root.geometry("300x100")
root.title("Folder Dialog")

frame=tk.Frame(master=root)
frame.grid(column=0, row=0,padx=10,pady=10)

labelmonth = tk.Label(frame,text="Month as in excel tab ",padx=5, pady=5,justify="left")
labelmonth.grid(column=0, row=0,padx=5)

labelpath = tk.Label(frame,text="timesheets Folder  ",padx=5, pady=5,justify="left")
labelpath.grid(column=0, row=1,padx=5)


label = tk.Label(frame,text="C:/",padx=5, pady=5)
label.grid(column=1, row=1,padx=5)



global width
width= "30"

text= tk.Entry(frame,text="Enter Text",borderwidth=5, width= width)
text.grid(column=1, row=0,padx=5)



folder_button = tk.Button(frame, text="Select Folder",width=20, command=open_folder_dialog)
folder_button.grid(column=2, row=0)



execute_button = tk.Button(frame, text="   Execute   ",width=20, command=execute)
execute_button.grid(column=2, row=1)


root.mainloop()
