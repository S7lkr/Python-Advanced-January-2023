try:
    with open("text.txt", "r") as some_file:
        print("File found!")
except FileNotFoundError as error:
    print(f"{error}\tFile not found!")
else:
    with open("text.txt") as a_file:
        print(a_file.read())
        a_file.close()