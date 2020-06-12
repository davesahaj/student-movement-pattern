import os
import shutil

if not os.path.exists("data"):
    os.makedirs("data/csv")
shutil.copyfile("file.xlsx", "data/file.xlsx")

os.system("python xlsToCsvConverter.py data/file.xlsx")
os.system("python csv_preprocessor.py")
os.system("python unique_wifi.py")
os.system("python frequency.py")
os.system("python binder.py")
os.remove("data/file.xlsx")