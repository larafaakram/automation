import tkinter as tk
from tkinter import filedialog, messagebox
import os
import shutil
from datetime import datetime

file_types = {
    'Images': ['.jpg', '.png', 'jpeg'],
    'Documents': ['.pdf', '.docx'],
    'Texts': ['.txt'],
    'Scripts': ['.py']} 

#path = '.'

def organize_by_type(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            for folder, extention in file_types.items():
                if ext in extention:
                    folder_path = os.path.join(path, folder)
                    os.makedirs(folder_path, exist_ok=True)
                    shutil.move(file_path, os.path.join(folder_path, file))
                    break

def organize_by_date(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            mod_time = os.path.getmtime(file_path)
            date_folder = datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d')
            folder_path = os.path.join(path, date_folder)
            os.makedirs(folder_path, exist_ok=True)
            shutil.move(file_path, os.path.join(folder_path, file))

def start_organizing():
    path = filedialog.askdirectory()
    if not path:
        return
    if var.get() == "type":
        organize_by_type(path)
        messagebox.showinfo("Success", "Files organized by type!")
    else:
        organize_by_date(path)
        messagebox.showinfo("Success", "Files organized by date!")

root = tk.Tk()
root.title('File organizer')
root.geometry('350x200')

tk.Label(root, text="choose how to organize your files:", font=('Arial', 12)).pack(pady=10)

var = tk.StringVar(value="type")

tk.Radiobutton(root, text="By file type", variable=var, value="type").pack()
tk.Radiobutton(root, text="By date Modified", variable=var, value="date").pack()

tk.Button(root, text="Select folder and organize", command=start_organizing, bg="#4CAF50", fg="white", font=('Arial', 11)).pack(pady=20)

root.mainloop()

