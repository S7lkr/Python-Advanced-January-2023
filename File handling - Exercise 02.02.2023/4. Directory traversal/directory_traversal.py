import os               # REMEMBER: in order to work with PATH TO FILE, we must import "os" lib


def save_extensions(folder, first_lvl=False):
    for filename in os.listdir(folder):             # for every file in the directory do:
        file = os.path.join(folder, filename)       # dir_name + filename -> "./test/text.txt". Get PATH to file\dir

        if os.path.isfile(file):                    # if path leads to a FILE:
            extension = filename.split(".")[-1]     # we get the last element (file extension) -> .py, .txt, .js, etc.

            if extension not in extensions.keys():  # add it to the dict
                extensions[extension] = []
            extensions[extension].append(filename)

        elif os.path.isdir(file) and not first_lvl:     # else, if path leads to a DIRECTORY:
            save_extensions(file, first_lvl=True)       # increase the lvl (sub-folder)


directory = input()     # enter a directory, where searched files shall be
extensions = {}         # create a dictionary to store the data

save_extensions(directory)
for ext, files in sorted(extensions.items()):   # sorted KEYS
    print(f".{ext}")
    for f in sorted(files):     # sorted VALUES
        print(f"- - - {f}")