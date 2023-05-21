needed_money = float(input())
available_money = float(input())

current_money = available_money
spend_days = 0
total_days = 0


while current_money < needed_money:
    if spend_days == 5:
        break

    action = input()
    money = float(input())

    total_days += 1

    if action == "spend":
        spend_days += 1
        current_money = current_money - money
        if current_money < 0:
            current_money = 0

    elif action == "save":
        spend_days = 0
        current_money += money

if spend_days == 5:
    print("You can't save the money.")
    print(total_days)
else:
    print(f"You saved the money for {total_days} days.")

