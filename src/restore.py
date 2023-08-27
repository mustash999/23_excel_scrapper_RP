from tkinter import messagebox
import get_info	

def restore(labelpath, dropdown, savepath, entry_widget):

	try:
			with open("src/data", "r") as file:
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
	# Save labelpath, dropdown values, and savepath to file
	with open("src/data", "w") as file:
		file.write(labelpath.cget("text") + "\n")
		file.write(savepath.cget("text") + "\n")
		file.write(entry_widget.get() + "\n")