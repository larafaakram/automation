import os
import shutil
from pathlib import Path

source_dir = Path("C:/Users/akram/Downloads")

if not source_dir.exists():
    print(f"Directory {source_dir} does not exist")
else:
    for file in source_dir.iterdir():
        if file.suffix == ".jpg":
            photo_folder = source_dir / "Photos"
            photo_folder.mkdir(exist_ok=True)
            shutil.move(str(file), photo_folder)

        




