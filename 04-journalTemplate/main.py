import os
import sys
from datetime import datetime
import subprocess


mood_options = ["Happy", "Neutral", "Sad", "Excited", "Anxious", "Grateful", "Tired"]
print("Select your mood today:")

for idx, mood in enumerate(mood_options, 1):
    print(f"{idx}. {mood}")

while True:
    try:
        mood_choice = int(input("Enter the number corresponding to your mood: "))
        if 1 <= mood_choice <= len(mood_options):
            selected_mood = mood_options[mood_choice -1]
            break
        else:
            print("Invalid choice. Please select a valid number.")
    except ValueError:
        print("Invalid input. please enter a number.")


journal_folder = "journals"
os.makedirs(journal_folder, exist_ok=True)

today = datetime.now().strftime("%Y-%m-%d")
journal_filename = f"{today}_journal.txt"
file_path = os.path.join(journal_folder, journal_filename)

template = f""" Date: {today}

    Today i'm gratefull for:
1.
2.
3.

    Today's goals:
-
-
-
Mood: {selected_mood}

"""

if not os.path.exists(file_path):
    with open(file_path, "w", encoding="utf=8") as f:
        f.write(template)

try:
    if os.name == 'nt':
        os.startfile(file_path)
    elif os.name == 'posix':
        subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', file_path])
except Exception as e:
    print(f"Couldn't open the journal file: {e}")





