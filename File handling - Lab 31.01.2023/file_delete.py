import os   # in order to delete files or folders, import os

file_path = "my_first_file.txt"
if os.path.exists(file_path):
    os.remove(file_path)
    print("File deleted!")
else:
    print("File not found!")