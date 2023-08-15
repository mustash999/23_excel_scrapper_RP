import pandas as pd
import os
from datetime import datetime
from tkinter import messagebox

def entry_to_dframe(entry_value):
	cells= entry_value.split(",")
	up_cells= []
	for c in cells:
		inner = c.split()
		group = []
		for i in inner:
			column = ord(c[0].upper()) - ord('A')
			row = int(c[1:]) - 1
			group.append((row, column))
		up_cells.append(group)
	return up_cells

def execute(folder, entry_text, dropdown, savepath):
	month= dropdown.get()
	cells= entry_to_dframe(entry_text)

	try:
		summarize(month, folder, cells, savepath)
		messagebox.showinfo ( 'summarizer', 'export done succesfully ')
	except ValueError:
		messagebox.showerror( 'error', 'Oops something went wrong !!')

def summarize(sheet, folder_path, cells, savepath):
	all_data = []
	folder_path = folder_path.cget("text")
	# loop through each excel file in folder
	for file_name in os.listdir(folder_path):
		if file_name.endswith('.xlsx'):
			file_path = os.path.join(folder_path, file_name)
			df = pd.read_excel(file_path, sheet_name=sheet, header=None)
			projects = []
			for c in cells:
				inner_lst = c.split()
				project = {'filename': file_name}
				
				for i, col_index in enumerate(inner_lst):
					project[f"column_{i+1}"] = df.iloc[int(col_index[1:]), int(col_index[0], 36) - 10]  # Convert column letter to index
					
				projects.append(project)
			
			df2 = pd.DataFrame(projects)
			all_data = all_data + projects

	# create new dataframe from all_data list
	final_df = pd.DataFrame(all_data)
	date= str( datetime.now()).replace("-", "").replace(".", "").replace(":", "").replace(" ", "")[: -8]
	
	# save dataframe to new excel file
	final_df.to_excel(f'{savepath.cget("text")}final_data{date}.xlsx', index=False)

