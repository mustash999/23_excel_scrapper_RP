from tkinter import messagebox
import get_info	
import os

def restore(labelpath, dropdown, savepath, entry_widget):

	try:
			with open("resources/data", "r") as file:
				lines = file.readlines()
				print(lines[0])
				print(lines[1])

			if lines:
				# Update labelpath, dropdown values, and savepath
				labelpath.config(text=lines[0].strip())
				dropdown['values'] = get_info.get_tabs(labelpath.cget("text"))
				dropdown.current(0)  																# set selection
				dropdown.state(['readonly'])
				savepath.config(text=lines[1].strip())
				entry_widget.delete(0, 'end')
				entry_widget.insert(0, lines[2].strip())
	except FileNotFoundError:
		messagebox.showerror("Error", "Restore data not found.")

def save(labelpath, dropdown, savepath, entry_widget):
    file_path = "resources/data"
    
    # Check if the file exists, create one if it doesn't
    if not os.path.exists(file_path):
        with open(file_path, "w") as file:  # This will create the file
            pass  # Do nothing, just create the file
    
    # Save labelpath, dropdown values, and savepath to file
    with open(file_path, "w") as file:
        file.write(labelpath.cget("text") + "\n")
        file.write(savepath.cget("text") + "\n")
        file.write(entry_widget.get() + "\n")