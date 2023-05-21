import sys
numbers_of_line = input()

max_number = -sys.maxsize
while numbers_of_line != "Stop":
    current_number = int(numbers_of_line)

    if current_number > max_number:
        max_number = current_number

    numbers_of_line = input()

print(max_number)
