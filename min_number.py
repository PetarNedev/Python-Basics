import sys
numbers_of_line = input()

min_number = sys.maxsize
while numbers_of_line != "Stop":
    current_number = int(numbers_of_line)

    if current_number < min_number:
        min_number = current_number

    numbers_of_line = input()

print(min_number)
