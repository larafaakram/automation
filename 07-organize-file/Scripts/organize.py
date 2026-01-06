import os
import shutil

file_types = {
    'Images': ['.jpg', '.png', 'jpeg'],
    'Documents': ['.pdf', '.docx'],
    'Texts': ['.txt'],
    'Scripts': ['.py']} 

path = '.'

for file in os.listdir():
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        ext = os.path.splitext(file)[1].lower()
        for folder, extention in file_types.items():
            if ext in extention:
                folder_path = os.path.join(path, folder)
                os.makedirs(folder_path, exist_ok=True)
                shutil.move(file_path, os.path.join(folder_path, file_path))
                break
