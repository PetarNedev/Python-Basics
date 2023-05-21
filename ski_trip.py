days = int(input())
type_room = input()
rating = input()
night = days - 1
expenses = 0

if type_room == "room for one person":
    expenses = night * 18
elif type_room == "apartment":
    expenses = night * 25
    if days < 10:
        expenses *= 0.70
    elif 10 <= days <= 15:
        expenses *= 0.65
    else:
        expenses *= 0.50
elif type_room == "president apartment":
    expenses = night * 35
    if days < 10:
        expenses *= 0.90
    elif 10 <= days <= 15:
        expenses *= 0.85
    else:
        expenses *= 0.80

if rating == "positive":
    expenses *= 1.25
else:
    expenses *= 0.90

print(f"{expenses:.2f}")
