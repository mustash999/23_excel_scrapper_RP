import pandas as pd
import os
from datetime import datetime


def execute(folder, text, messagebox):
	month= text.get()
	try:
		summarize(month, folder)
		messagebox.showinfo ( 'summarizer', 'export done succesfully ')
	except ValueError:
		messagebox.showerror( 'error', 'Oops something went wrong !!')

def summarize(sheet, folder_path):
    all_data = []
    # loop through each excel file in folder
    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)
            df = pd.read_excel(file_path, sheet_name= sheet,header=None)
            name = df.at[0, 0]
            projects=[]
            for p in range(6,14):
                project = {'Name':name,"project Name":df.iloc[3, p], "hours":df.iloc[35, p]}
                projects.append(project)
            
            df2=pd.DataFrame(projects)
            all_data= all_data+ projects



    # create new dataframe from all_data list
    final_df = pd.DataFrame(all_data)
    date= str( datetime.now()).replace("-", "").replace(".", "").replace(":", "").replace(" ", "")[: -8]
    
    # save dataframe to new excel file
    final_df.to_excel(f'final_data{date}.xlsx', index=False)

