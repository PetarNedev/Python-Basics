wished_money = float(input())
command = input()
target = 0


while command != "Party!" or target == wished_money:
    number_of_cocktail = int(input())
    price_one_cocktail = 0
    for i in command:
        price_one_cocktail += 1
    one_order = number_of_cocktail * price_one_cocktail
    if one_order % 2 != 0:
        one_order *= 0.75
        target += one_order
    else:
        target += one_order
    if target >= wished_money:
        break
    command = input()


diff = abs(target - wished_money)
if target < wished_money:
    print(f"We need {diff:.2f} leva more.")
    print(f"Club income - {target:.2f} leva.")
if target >= wished_money:
    print(f"Target acquired.")
    print(f"Club income - {target:.2f} leva.")
    