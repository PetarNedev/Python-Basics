destination = input()

while destination != "End":
    price_trip = float(input())

    needed_money = 0
    while needed_money < price_trip:
        salary = float(input())
        needed_money += salary
    print(f"Going to {destination}!")
    destination = input()


