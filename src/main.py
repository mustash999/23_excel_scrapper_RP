import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from summerizer import summarize
from tkinter import messagebox
import splash
import get_info
from PIL import Image, ImageTk
import restore

def check_enable_execute(labelpath, dropdown_var, entry_widget, execute_button):
    if labelpath.cget("text") and dropdown_var.get() and entry_widget.get():
        execute_button.config(state="normal")  # Enable the button
    else:
        execute_button.config(state="disabled") 

def main():
#This part is to set the window size and title
	splash.splash()
	root = tk.Tk()
	#root.geometry("640x300")
	root.title("Summerizer V1.1")
	root.iconbitmap("resources/Summarizer.ico") 

	#This part is to set the frame and the labels and buttons
	frame=tk.Frame(root)
	frame.pack(fill="both", expand=True)
	#frame.grid(column=0, row=0,padx=20,pady=20)

	#This part is to set the buttons
	folder_button = tk.Button(frame, text="Select Folder >>", width=35, command=lambda: get_info.get_folder(labelpath, dropdown))
	folder_button.pack(padx=5, pady=5)

	labelpath = tk.Label(frame,text="Excel files Folder",wraplength=220,justify="left")
	labelpath.pack(padx=5, pady=5)

	label_spe_tab = tk.Label(frame,text="\n Choose the Excel Tab",wraplength=220,justify="left")
	label_spe_tab.pack(padx=5, pady=5)

	# Create a dropdown list with state set to "readonly"
	dropdown_var = tk.StringVar(root)
	dropdown = ttk.Combobox(frame, textvariable=dropdown_var, state="readonly", width=39,)
	dropdown.pack(padx=5, pady=5)

	label_specify = tk.Label(frame,text="\n Choose the cells to parse",wraplength=220,justify="left")
	label_specify.pack(padx=5, pady=5)

	entry_widget = tk.Entry(frame, width=41)  # Create a single-line Entry widget
	entry_widget.insert(0, "A1 , A2")
	entry_widget.pack(padx=5, pady=5)

	#dropdown.bind("<<ComboboxSelected>>", lambda event: text= dropdown_var.get())

	save_button = tk.Button(frame, text="Save output as >>", width=35, command=lambda: get_info.save_folder(savepath))
	save_button.pack(padx=5, pady=5)
	
	savepath = tk.Label(frame,text="timesheets Folder  ",wraplength=220, padx=25,justify="left")
	savepath.pack(padx=5, pady=5)

	restore_button = tk.Button(frame, text="Restore Previous", width=35, command=lambda: restore.restore(labelpath, dropdown, savepath, entry_widget, execute_button))
	restore_button.pack(padx=5, pady=5)

	try:
		with open("src/data", "r"):
			pass  # If file exists, keep the Restore button enabled
	except FileNotFoundError:
		restore_button.config(state="disabled")
	
	execute_button = tk.Button(frame, text="Execute", width=35, command=lambda: summarize(dropdown.current, labelpath.cget("text")))
	execute_button.pack(padx=5, pady=5)
	check_enable_execute(labelpath, dropdown_var, entry_widget, execute_button)


	exit_button = tk.Button(frame, text="Exit", width=35, command=lambda: exit())
	exit_button.pack(padx=5, pady=5)

	image = Image.open("resources/logo.png")
	resized_image = image.resize((250, 250))
	tk_image = ImageTk.PhotoImage(resized_image)
	image_label = tk.Label(frame, image=tk_image, height=250, width=250)
	image_label.pack(padx=5, pady=5)

	#frame.pack_propagate(False)
	root.mainloop()

if __name__ == "__main__":
	main()

""" 

global width
width= "30"

text= tk.Entry(frame,text="Enter Text",borderwidth=5, width= width)
text.grid(column=1, row=0,padx=5)



execute_button = tk.Button(frame, text="   Execute   ",width=20, command=execute)
execute_button.grid(column=2, row=1)
"""