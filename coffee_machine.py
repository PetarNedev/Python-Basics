drink = input()
sugar = input()
number_drink = int(input())
price = 0


if drink == "Espresso":
    if sugar == "Without":
        price = 0.90 * 0.65
    elif sugar == "Normal":
        price = 1
    elif sugar == "Extra":
        price = 1.20


elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1 * 0.65
    elif sugar == "Normal":
        price = 1.20
    elif sugar == "Extra":
        price = 1.60

elif drink == "Tea":
    if sugar == "Without":
        price = 0.50 * 0.65
    elif sugar == "Normal":
        price = 0.60
    elif sugar == "Extra":
        price = 0.70

total_price = number_drink * price

if number_drink >= 5 and drink == "Espresso":
    total_price *= 0.75

if total_price > 15:
    total_price *= 0.80
print(f"You bought {number_drink} cups of {drink} for {total_price:.2f} lv.")

