budget = float(input())
count_statist = int(input())
price_cloth_one = float(input())

price_decor = (budget * 10)/100
price_cloth = count_statist * price_cloth_one
if count_statist > 150:
    discount = (price_cloth * 10) / 100
    price_cloth = price_cloth - discount

total_sum = price_decor + price_cloth
money_left = abs(budget - total_sum)
if total_sum > budget:
    print("Not enough money!")
    print(f"Wingard needs {money_left:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")