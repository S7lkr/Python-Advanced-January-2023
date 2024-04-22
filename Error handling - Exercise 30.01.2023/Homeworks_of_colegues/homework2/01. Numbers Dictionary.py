# 1. While-loop for filling dictionary with input numbers

numbers_dictionary = {}                                     # Definition of an empty dictionary for input numbers

line = input()
while line != "Search":

    try:                                                    # Tries to create input number as key in dictionary
        number_as_string = line
        number = int(input())
        numbers_dictionary[number_as_string] = number

    except ValueError:
        print("The variable number must be an integer")     # Value Error message if input is not valid (integer)

    line = input()                                          # Input for next number in loop or exit input


# 2. While-loop for searching dictionary for input numbers

line = input()
while line != "Remove":

    try:                                                    # Tries to pull input number value from dictionary
        searched = line
        print(numbers_dictionary[searched])

    except KeyError:
        print("Number does not exist in dictionary")        # Key Error message if no such key (input number) exists

    line = input()


# 3. While-loop for removing numbers from predefined dictionary

line = input()
while line != "End":

    try:                                                    # Tries to remove input number from dictionary
        searched = line
        del numbers_dictionary[searched]

    except KeyError:
        print("Number does not exist in dictionary")        # Key Error message if no such key (input number) exists

    line = input()                                          # Input for next number in loop or exit input


# 4. Output of dictionary with numbers

print(numbers_dictionary)
