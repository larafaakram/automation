import os
import shutil

folder_path = "simple_files"

file_type = {
    'Images': ['.png', '.gif'],
    'Videos': ['.mov', '.wav'],
    'Documents': ['.txt', '.pdf', '.docx'],
    'Archives': ['.zip', '.rar'],
    'Musiques': ['.mp3']
}

for folder in file_type.keys():
    os.makedirs(os.path.join(folder_path, folder), exist_ok=True)

for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(file)
        for folder_name, extentions in file_type.items():
            if ext.lower() in extentions:
                to_folder = os.path.join(folder_path, folder_name) 
                shutil.move(file_path, os.path.join(to_folder, file))
                break
print("File/Folder organized successfully")
