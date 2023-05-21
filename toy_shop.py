trip = float(input())
number_puzzle = int(input())
number_doll = int(input())
number_bear = int(input())
number_minions = int(input())
number_truck = int(input())

number_toys = number_puzzle + number_doll + number_bear + number_minions + number_truck
price_toys = (number_puzzle*2.60) + (number_doll*3) + (number_bear*4.10) + (number_minions*8.20) + (number_truck*2)
if number_toys >= 50:
    discount = (price_toys * 25) / 100
    end_price = price_toys - discount
else:
    end_price = price_toys

rent = (end_price*10)/100
win_price = end_price - rent

if win_price >= trip:
    yes_trip = win_price-trip
    print(f"Yes! {yes_trip:.2f} lv left.")
else:
    no_trip = trip-win_price
    print(f"Not enough money! {no_trip:.2f} lv needed.")
