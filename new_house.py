type_flowers = input()
number_flowers = int(input())
budgets = int(input())
price = 0
if type_flowers == "Roses":
    price = number_flowers * 5
    if number_flowers > 80:
        price = price * 0.90
elif type_flowers == "Dahlias":
    price = number_flowers * 3.80
    if number_flowers > 90:
        price = price * 0.85
elif type_flowers == "Tulips":
    price = number_flowers * 2.80
    if number_flowers > 80:
        price = price * 0.85
elif type_flowers == "Narcissus":
    price = number_flowers * 3
    if number_flowers < 120:
        price = price * 1.15
elif type_flowers == "Gladiolus":
    price = number_flowers * 2.50
    if number_flowers < 80:
        price = price * 1.20
diff = abs(budgets - price)
if price > budgets:
    print(f"Not enough money, you need {diff:.2f} leva more.")
else:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {diff:.2f} leva left.")
