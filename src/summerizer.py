import pandas as pd
import os
from datetime import datetime
from tkinter import messagebox


# ------------------------------------------------- transform Excel cells to pandas --------------------------------------------------
def entry_to_dataframe_indices(entry_value):
    cells = entry_value.split(",")
    updated_cells = []
    for cell_group in cells:
        inner = cell_group.split()
        group = []
        for i in inner:
            column = ord(i[0].upper()) - ord('A')
            row = int(i[1:]) - 1
            group.append((row, column))
        updated_cells.append(group)
    return updated_cells


def summarize(sheet, folder_path, cells, save_path):
	all_data = []
	for file_name in os.listdir(folder_path):
		if file_name.endswith('.xlsx'):
			file_path = os.path.join(folder_path, file_name)
			try:
				df = pd.read_excel(file_path, sheet_name=sheet, header=None)
			except Exception as e:
				print(f"Error reading file {file_name}: {e}")
				continue

			cell_indices = entry_to_dataframe_indices(cells)
			projects = []
			line = {}
			count = 0
			for ind in cell_indices:
				if type(ind) is list:
					line = {}
					count = 1
					for cg in ind:
						try:
							line[(f"Column{count}")] = df.iloc[cg[0], cg[1]]
							count += 1

						except IndexError:
							print(f"Invalid index ({cg[0]}, {cg[1]}) for file {file_name}")
							continue
					projects.append(line)
				else:
					try:
						
						line[(f"Column{count}")] = df.iloc[ind[0], ind[1]]
						count += 1
					except IndexError:
						print(f"Invalid index ({ind[0]}, {ind[1]}) for file {file_name}")
						continue
					projects.append(line)	

			all_data.extend(projects)

	# Create new DataFrame from all_data list
	final_df = pd.DataFrame(all_data)
	date_str = datetime.now().strftime("%Y%m%d%H%M%S")

	# Save DataFrame to new Excel file
	try:
		final_df.to_excel(f'{save_path}/final_data_{date_str}.xlsx', index=False)
	except Exception as e:
		print(f"Error saving final DataFrame: {e}")

def execute(folder, entry_text, dropdown, savepath):
	month= dropdown.get()
	try:
		fldr_txt = folder.cget("text")
		sve_txt = savepath.cget("text")
		summarize(month, fldr_txt, entry_text, sve_txt)
		messagebox.showinfo ( 'summarizer', 'export done succesfully ')
	except ValueError:
		messagebox.showerror( 'error', 'Oops something went wrong !!')

"""folder = "C:/Users/mshor/OneDrive/000_Programing Exercise and Learning/_Python/23_excel_scrapper_RP/test_files"
entry_text = "A1 A2 B2, A1 A3 B3"
sheet = "Tabelle1"
savepath = "C:/Users/mshor/OneDrive/000_Programing Exercise and Learning/_Python/23_excel_scrapper_RP/test_files"

summarize(sheet, folder, entry_text, savepath)"""