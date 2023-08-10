import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from summerizer import summarize
from tkinter import messagebox
import splash
import get_info
from PIL import Image, ImageTk

def main():
#This part is to set the window size and title
	splash.splash()
	root = tk.Tk()
	root.geometry("580x250")
	root.title("Summerizer V1.1")
	root.iconbitmap("resources/Summarizer.ico") 

	#This part is to set the frame and the labels and buttons
	frame=tk.Frame(master=root)
	frame.pack(fill="both", expand=True)
	#frame.grid(column=0, row=0,padx=20,pady=20)

	#This part is to set the buttons
	folder_button = tk.Button(frame, text="Select Folder >>", width=20, command=lambda: get_info.get_folder(labelpath, dropdown))
	folder_button.grid(column=0, row=0, padx=5, pady=5)

	labelpath = tk.Label(frame,text="timesheets Folder",wraplength=180,justify="left")
	labelpath.grid(column=1, row=0,padx=5, pady=5)

	# Create a dropdown list with state set to "readonly"
	dropdown_var = tk.StringVar(root)
	dropdown = ttk.Combobox(frame, textvariable=dropdown_var, state="readonly", width=20,)
	dropdown.grid(column=0, row=1, padx=5, pady=5)

	#dropdown.bind("<<ComboboxSelected>>", lambda event: text= dropdown_var.get())

	save_button = tk.Button(frame, text="Save output as >>", width=20, command=lambda: get_info.save_folder(savepath))
	save_button.grid(column=0, row=2, padx=5, pady=5)
	
	savepath = tk.Label(frame,text="timesheets Folder  ",wraplength=180, padx=25,justify="left")
	savepath.grid(column=1, row=2,padx=5, pady=5)

	execute_button = tk.Button(frame, text="Execute", width=45, command=lambda: get_info.save_folder(savepath))
	execute_button.grid(column=0,columnspan=2, row=3, padx=5, pady=5, sticky="w")

	exit_button = tk.Button(frame, text="Exit", width=45, command=lambda: exit())
	exit_button.grid(column=0,columnspan=2,  row=4, padx=5, pady=5, sticky="w")

	image = Image.open("resources/logo.png")
	resized_image = image.resize((200, 200))
	tk_image = ImageTk.PhotoImage(resized_image)
	image_label = tk.Label(frame, image=tk_image, height=200, width=200)
	image_label.grid(column=2, row=0, rowspan=5, padx=5, pady=5, sticky="e")

	frame.pack_propagate(False)
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