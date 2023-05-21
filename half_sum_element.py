import sys
number_of_lines = int(input())
max_num = -sys.maxsize
number_sum = 0

for i in range(number_of_lines):
    current_number = int(input())

    if current_number > max_num:
        max_num = current_number
    number_sum += current_number

other_sum = number_sum - max_num

if max_num == other_sum:
    print("Yes")
    print(f"Sum = {other_sum}")
else:
    diff = abs(max_num - other_sum)
    print("No")
    print(f"Diff = {diff}")
