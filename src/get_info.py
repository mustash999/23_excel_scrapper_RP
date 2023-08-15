import openpyxl
import tkinter as tk
import os
from tkinter import filedialog


def get_tabs(folder_path):
	try:
		# Iterate through files in the folder
		for filename in os.listdir(folder_path):
			if filename.endswith(".xlsx"):
				file_path = os.path.join(folder_path, filename)
				workbook = openpyxl.load_workbook(file_path)
				sheet_names = workbook.sheetnames
				workbook.close()
				return sheet_names
		# If no .xlsx file is found
		print("No .xlsx files found in the folder.")
		return []
	except Exception as e:
		print(f"An error occurred: {e}")
		return []

def get_folder( labelpath, dropdown):
	filedialog = tk.filedialog
	folder_path = filedialog.askdirectory()
	labelpath.config(text=folder_path)
	dropdown['values'] = get_tabs(labelpath.cget("text"))
	dropdown.current(0)  																# set selection
	dropdown.state(['readonly'])
	#width= labelpath.winfo_width()

def save_folder( savepath):
	filedialog = tk.filedialog
	folder_path = filedialog.askdirectory()
	savepath.config(text=folder_path)
	

