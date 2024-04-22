import os


def create_file(*args):
    file = open(f"{args[0]}", "w")          # create NEW. If there is a file already, empty it
    file.close()


def add_file(*args):
    with open(f"{args[0]}", "a") as file:       # open to ADD something to it
        file.write(f"{args[1]}\n")


def replace_file(*args):
    try:
        with open(f"{args[0]}", "r") as file:   # first we open to READ
            lines = file.readlines()            # represent all lines as elements of a list

        for l in range(len(lines)):             # for every line
            lines[l] = lines[l].replace(args[1], args[2])   # replace OLD string with NEW

        # NOTE: changes are still NOT SAVED into our "file.txt"!!
        with open(f"{args[0]}", "w") as file:       # so, open to WRITE the file
            file.write("".join(lines))              # and make the changes

    except FileNotFoundError:
        print("An error occurred")


def delete_file(*args):
    try:
        file = f"{args[0]}"
        os.remove(file)
    except FileNotFoundError:
        print("An error occurred")


instruction = input()
while not instruction == "End":
    act, *info = instruction.split("-")     # We will ALWAYS have some "act"

    if act == "Create":
        create_file(*info)
    elif act == "Add":
        add_file(*info)
    elif act == "Replace":
        replace_file(*info)
    elif act == "Delete":
        delete_file(*info)

    instruction = input()