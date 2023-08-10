import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import splash
import get_info

def main():
    splash.splash()
    root = tk.Tk()
    root.geometry("580x250")
    root.title("Summerizer V1.1")
    root.iconbitmap("resources/Summarizer.ico")

    # Set up the frame
    frame = tk.Frame(master=root)
    frame.pack(fill="both", expand=True)

    # Create the "Select Folder" button
    folder_button = tk.Button(frame, text="Select Folder >>", width=20, command=lambda: get_info.get_folder(labelpath, dropdown))
    folder_button.grid(column=0, row=0, padx=5, pady=5)

    # Create the label for the selected folder
    labelpath = tk.Label(frame, text="timesheets Folder", wraplength=180, justify="left")
    labelpath.grid(column=1, row=0, padx=5, pady=5)

    # Create the dropdown
    dropdown_var = tk.StringVar(root)
    dropdown = ttk.Combobox(frame, textvariable=dropdown_var, state="readonly", width=20)
    dropdown.grid(column=0, row=1, padx=5, pady=5)

    # Create the "Save Output As" button
    save_button = tk.Button(frame, text="Save output as >>", width=20, command=lambda: get_info.save_folder(savepath))
    save_button.grid(column=0, row=2, padx=5, pady=5)

    # Create the label for the save folder
    savepath = tk.Label(frame, text="timesheets Folder  ", wraplength=180, padx=25, justify="left")
    savepath.grid(column=1, row=2, padx=5, pady=5)

    # Create the "Execute" button
    execute_button = tk.Button(frame, text="Execute", width=45, command=lambda: some_function())
    execute_button.grid(column=0, columnspan=2, row=3, padx=5, pady=5, sticky="w")

    # Create the "Exit" button
    exit_button = tk.Button(frame, text="Exit", width=45, command=root.destroy)
    exit_button.grid(column=0, columnspan=2, row=4, padx=5, pady=5, sticky="w")

    # Load and display the logo image
    image = Image.open("resources/logo.png")
    resized_image = image.resize((234, 236))
    tk_image = ImageTk.PhotoImage(resized_image)
    image_label = tk.Label(frame, image=tk_image)
    image_label.grid(column=2, row=0, rowspan=5, padx=5, pady=5, sticky="e")

    frame.pack_propagate(False)
    root.mainloop()

if __name__ == "__main__":
    main()
