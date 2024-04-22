# ERRORS are result of an incorrect, bad code
# REMEMBER: Errors detected during execution, are called EXCEPTIONS!

# in TRY, we write the code, which either will be CORRECT or NO.
try:
    lst = input().split(", ")
    ind = int(input("Enter an index: "))
    print(f"Element with index {ind} is: {lst[ind]}")
    # raise IndexError  # -> NOTE: raise DIRECTLY throws an error, no matter if the code is valid or not!

# only ONE of the EXCEPTS below will be engaged.
except IndexError:  # only if "IndexError" detected, this except will engage
    print("Invalid Index! Please enter a valid index!")
except ValueError:  # # only if "ValueError" is detected
    print("Incorrect Value Type! Please enter a valid value!")
except (NameError, SyntaxError):    # only if ONE OF THE TWO errors are encountered in the code!
    print("Syntax or NameError!")

else:   # if the code in TRY is fine and NO EXCEPTION (ERROR) to handle, else will be engaged.
    print(lst)

finally:    # FINALLY, will ALWAYS be engaged, NO MATTER the code is correct or not!
    print("Program complete!")