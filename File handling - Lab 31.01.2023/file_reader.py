def sum_numbers(file_name):
    file = open(file_name, "r")
    sum_of_numbers = 0

    for number in file:
        sum_of_numbers += int(number)
    file.close()
    return sum_of_numbers


print(sum_numbers("numbers.txt"))