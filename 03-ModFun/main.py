import my_mod
import os
import shutil



os.mkdir("test_dir")
shutil.copy("my_mod.py", "test_dir/my_mod.py")


my_mod.say_hello()