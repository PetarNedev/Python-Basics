number = int(input())
combination_counter = 0
number_of_combination = 0
for x1 in range(number + 1):
    for x2 in range(number + 1):
        for x3 in range(number + 1):
            if x1 + x2 + x3 == number:
                combination_counter += 1
            print(x1, x2, x3)
            number_of_combination += 1
        number_of_combination += 1
    number_of_combination += 1

print(combination_counter)
print(number_of_combination)