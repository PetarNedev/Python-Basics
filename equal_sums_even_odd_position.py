first_number = int(input())
second_number = int(input())

for num in range(first_number, second_number + 1):
    hundred_thousand = (num // 100000) % 10
    ten_thousand = (num // 10000) % 10
    thousand = (num // 1000) % 10
    hundred = (num // 100) % 10
    ten = (num // 10) % 10
    unit = num % 10

    odd = hundred_thousand + thousand + ten
    even = ten_thousand + hundred + unit
    if odd == even:
        print(num, end=" ")