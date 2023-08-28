#import for the main window
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# Local imports
import get_info, restore, summerizer, start

#-------------------------------------------------Commands finctions---------------------------------------------------

def check_enable_execute(labelpath, dropdown_var, entry_widget, execute_button):
	if labelpath.cget("text") and dropdown_var.get() and entry_widget.get():
		execute_button.config(state="normal")  # Enable the button
	else:
		execute_button.config(state="disabled")

def com_execute(labelpath, dropdown, savepath, entry_widget, execute_button):
	summerizer.execute(labelpath, entry_widget.get(), dropdown, savepath)
	restore.save(labelpath, dropdown, savepath, entry_widget)
	check_enable_execute(labelpath, dropdown, entry_widget, execute_button)

def com_save(savepath, labelpath, dropdown, entry_widget, execute_button):
	get_info.save_folder(savepath)
	check_enable_execute(labelpath, dropdown, entry_widget, execute_button)

def com_restore( labelpath, dropdown, savepath, entry_widget, execute_button):
	restore.restore(labelpath, dropdown, savepath, entry_widget)	
	check_enable_execute(labelpath, dropdown, entry_widget, execute_button)

def com_gt_folder(labelpath, dropdown, entry_widget, execute_button):
	get_info.get_folder(labelpath, dropdown)
	check_enable_execute(labelpath, dropdown, entry_widget, execute_button)

def main():
#This part is to set the window size and title
	start.splash()
	root = tk.Tk()
	# -------------------------------------------------Main Window construction------------------------------------------------
	root.title("Summerizer V1.1")
	root.iconbitmap("resources/Summarizer.ico") 

	#This part is to set the frame and the labels and buttons
	frame=tk.Frame(root)
	frame.pack(fill="both", expand=True)
	


	#----------------------------------------------- inner components ----------------------------------------------------------------
	#This part is to set the buttons
	folder_button = tk.Button(frame, text="Select Folder >>", width=35, command=lambda: com_gt_folder(labelpath, dropdown,entry_widget, execute_button))
	folder_button.pack(padx=5, pady=5)

	labelpath = tk.Label(frame,text="Excel files Folder",wraplength=220,justify="left")
	labelpath.pack(padx=5, pady=5)

	#----------------------------------------------Dropdown to Select tabs -----------------------------------------------------------
	label_spe_tab = tk.Label(frame,text="\n Choose the Excel Tab",wraplength=220,justify="left")
	label_spe_tab.pack(padx=5, pady=5)

	
	dropdown_var = tk.StringVar(root)
	dropdown = ttk.Combobox(frame, textvariable=dropdown_var, state="readonly", width=39,)
	dropdown.pack(padx=5, pady=5)


	#----------------------------------------------which cells ( 1-a label  2. an entry box ) ----------------------------------------

	label_specify = tk.Label(frame,text="\n Choose the cells to parse \n Format like this  (A1 B1 C1, A2 B2 C2 ... etc)",wraplength=220,justify="left")
	label_specify.pack(padx=5, pady=5)

	ent_var = tk.StringVar()
	ent_var.trace_add("write", lambda *args: check_enable_execute(labelpath, dropdown, entry_widget, execute_button))
	entry_widget = tk.Entry(frame, width=41, textvariable= ent_var)  # Create a single-line Entry widget
	entry_widget.pack(padx=5, pady=5)

	#----------------------------------------------Save output as --------------------------------------------------------------------

	save_button = tk.Button(frame, text="Save output as >>", width=35, command=lambda: com_save(savepath, labelpath, dropdown, entry_widget, execute_button))
	save_button.pack(padx=5, pady=5)
	
	savepath = tk.Label(frame,text="timesheets Folder  ",wraplength=220, padx=25,justify="left")
	savepath.pack(padx=5, pady=5)

	#----------------------------------------------Restore last session info ---------------------------------------------------------

	restore_button = tk.Button(frame, text="Restore Previous", width=35, command=lambda: com_restore(labelpath, dropdown, savepath, entry_widget, execute_button))

	restore_button.pack(padx=5, pady=5)

	try:
		with open("src/data", "r"):
			pass  # If file exists, keep the Restore button enabled
	except FileNotFoundError:
		restore_button.config(state="disabled")
	
	# ----------------------------------------------Execute button and command -------------------------------------------------------

	execute_button = tk.Button(frame, text="Execute", width=35, command=lambda: com_execute(labelpath, dropdown, savepath, entry_widget, execute_button))
	execute_button.pack(padx=5, pady=5)


	# ----------------------------------------------Exit button--------------- -------------------------------------------------------


	exit_button = tk.Button(frame, text="Exit", width=35, command=lambda: exit())
	exit_button.pack(padx=5, pady=5)

	# ----------------------------------------------Check if all fields are filled ---------------------------------------------------
	check_enable_execute(labelpath, dropdown, entry_widget, execute_button)

	#----------------------------------------------Image------------------------------------------------------------------------------
	image = Image.open("resources/logo.png")
	resized_image = image.resize((250, 250))
	tk_image = ImageTk.PhotoImage(resized_image)
	image_label = tk.Label(frame, image=tk_image, height=250, width=250)
	image_label.pack(padx=5, pady=5)
	root.mainloop()

if __name__ == "__main__":
	main()

