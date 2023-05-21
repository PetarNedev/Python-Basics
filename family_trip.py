budget = float(input())
nights = int(input())
price_one_night = float(input())
percent_extra_expenses = int(input())


if nights > 7:
    price_one_night *= 0.95
    all_night = nights * price_one_night
else:
    all_night = nights * price_one_night

extra_expenses = budget * percent_extra_expenses / 100
total_expenses = all_night + extra_expenses
left_money = abs(budget - total_expenses)

if total_expenses <= budget:
    print(f"Ivanovi will be left with {left_money:.2f} leva after vacation.")
else:
    print(f"{left_money:.2f} leva needed.")
