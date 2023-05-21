budgets = int(input())
season = input()
fishermen = int(input())

price = 0
if season == "Spring":
    if fishermen <= 6:
        price = 3000 * 0.90
    elif 7 <= fishermen <= 11:
        price = 3000 * 0.85
    else:
        price = 3000 * 0.75

elif season == "Summer" or season == "Autumn":
    if fishermen <= 6:
        price = 4200 * 0.90
    elif 7 <= fishermen <= 11:
        price = 4200 * 0.85
    else:
        price = 4200 * 0.75

else:
    if fishermen <= 6:
        price = 2600 * 0.90
    elif 7 <= fishermen <= 11:
        price = 2600 * 0.85
    else:
        price = 2600 * 0.75

if fishermen % 2 == 0 and season != "Autumn":
    price = price * 0.95

diff = abs(price - budgets)
if price > budgets:
    print(f"Not enough money! You need {diff:.2f} leva.")
else:
    print(f"Yes! You have {diff:.2f} leva left.")
    