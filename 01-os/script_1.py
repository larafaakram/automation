import os

from datetime import datetime

print("Current Working Directory:", os.getcwd())
print("Current Date and Time:", datetime.now())

folder_name = "folder_script_1"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created successfully!")

file_path = os.path.join(folder_name, "message.txt")
with open(file_path, "w") as file:
    file.write("This is a message from script_1.py\n")
    file.write(f"Script executed on: {datetime.now()}\n")



print(f"file 'message.txt' created inside folder '{folder_name}' with custom message")

