def file_writer():
    file = open("my_first_file.txt", "w")
    file.write('I just created my first file!')
    file.close()


file_writer()

test_file = open("my_first_file.txt", "r")
print(test_file.read())
test_file.close()