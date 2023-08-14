from tkinter import messagebox
import get_info	

def restore(labelpath, dropdown, savepath):
	with open("src/data", "r") as file:
			lines = file.readlines()
			print(lines[0])
			print(lines[1])
	"""
	try:
		

			if lines:
				# Update labelpath, dropdown values, and savepath
				labelpath.config(text=lines[0].strip())
				dropdown['values'] = get_info.get_tabs(labelpath.cget("text"))
				dropdown.current(0)  																# set selection
				dropdown.state(['readonly'])
				savepath.config(text=lines[1].strip())
	except FileNotFoundError:
		messagebox.showerror("Error", "Restore data not found.")"""
	
with open("src/data", "r") as file:
			lines = file.readlines()
			print(lines[0], lines[1])
			print(lines[1])