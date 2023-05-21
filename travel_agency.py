name_of_city = input()
type_of_pack = input()
vip = input()
number_of_days = int(input())
days = number_of_days
price_per_day = 0
discount = 0


if number_of_days <= 0:
    print("Days must be positive number!")

elif vip != "yes" and vip != "no":
    print("Invalid input!")

elif number_of_days > 7:
    days -= 1

elif name_of_city == "Bansko" or name_of_city == "Borovets":
    if type_of_pack == "noEquipment":
        price_per_day = 80
        if vip != "no":
            discount = 0.05
    elif type_of_pack == "withEquipment":
        price_per_day = 100
        if vip != "no":
            discount = 0.10
    one_day = price_per_day - price_per_day * discount
    final_price = one_day * days
    print(f"The price is {final_price:.2f}lv! Have a nice time!")

elif name_of_city == "Varna" or name_of_city == "Burgas":
    if type_of_pack == "noBreakfast":
        price_per_day = 100
        if vip != "no":
            discount = 0.07
    elif type_of_pack == "withBreakfast":
        price_per_day = 130
        if vip != "no":
            discount = 0.12
    one_day = price_per_day - price_per_day * discount
    final_price = one_day * days
    print(f"The price is {final_price:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
