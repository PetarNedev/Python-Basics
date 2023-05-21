line_numbers = int(input())
p1 = 0
p2 = 0
p3 = 0
p4 = 0
p5 = 0

for i in range(1, line_numbers + 1):
    current_number = int(input())

    if current_number < 200:
        p1 += 1
    elif 200 <= current_number <= 399:
        p2 += 1
    elif 400 <= current_number <= 599:
        p3 += 1
    elif 600 <= current_number <= 799:
        p4 += 1
    else:
        p5 += 1
percent_1 = (p1 / line_numbers) * 100
percent_2 = (p2 / line_numbers) * 100
percent_3 = (p3 / line_numbers) * 100
percent_4 = (p4 / line_numbers) * 100
percent_5 = (p5 / line_numbers) * 100
print(f"{percent_1:.2f}%")
print(f"{percent_2:.2f}%")
print(f"{percent_3:.2f}%")
print(f"{percent_4:.2f}%")
print(f"{percent_5:.2f}%")

