count_of_numbers = int(input())
left_sum = 0
right_sum = 0
for number in range(count_of_numbers):
    current_number = int(input())
    left_sum += current_number
for number in range(count_of_numbers):
    current_number = int(input())
    right_sum += current_number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")
