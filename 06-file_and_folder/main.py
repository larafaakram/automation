import os
import shutil

base_dir = "folders"
source = os.path.join(base_dir, 'source_folder')
destination = os.path.join(base_dir, 'destination_folder')

print(f"Current work directory: ", os.getcwd())
print(f"Lokking for file at: ", os.path.join(source, "simple1.txt"))

# Renaming file
def rename_file(old_name, new_name):
    old_path = os.path.join(source, old_name)
    new_path = os.path.join(source, new_name)
    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f"Renamed: {old_name} -> {new_name}")
    else:
        print(f"File not found for renaming")

# Moving a file
def move_file(filename):
    src_path = os.path.join(source, filename)
    dest_path = os.path.join(destination, filename)
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
        print(f"Moved: {src_path} -> {dest_path}")
    else:
        print(f"File not found to move.")

# Deleting a file
def delete_file(folder, filename):
    file_path = os.path.join(folder, filename)
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")
    else:
        print(f"File not found to delete")

# Create folder
def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Directory created")
    else:
        print(f"Folder already exist")

# Delete Folder
def delete_folder(path):
    if os.path.exists(path):
        shutil.rmtree(path)
        print(f"Directory deleted")
    else:
        print(f"Directory not found")

if __name__ == "__main__":
    rename_file("simple1.txt", "renamed_simple1.txt")

    move_file("renamed_simple1.txt")

    delete_file(destination, "renamed_simple1.txt")

    create_folder(os.path.join(base_dir, "new_folder"))

    delete_folder(os.path.join(base_dir, "new_folder"))