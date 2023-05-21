ticket_type = input()
row = int(input())
columns = int(input())

income = 0
cinema_capacity = row * columns

if ticket_type == "Premiere":
    income = cinema_capacity * 12
elif ticket_type == "Normal":
    income = cinema_capacity * 7.50
else:
    income = cinema_capacity * 5
print(f"{income:.2f} leva")
