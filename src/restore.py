from tkinter import messagebox
import get_info	
from main import check_enable_execute

def restore(labelpath, dropdown, savepath, entry_widget, execute_button):

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
				check_enable_execute(labelpath, dropdown, entry_widget, execute_button)
	except FileNotFoundError:
		messagebox.showerror("Error", "Restore data not found.")
