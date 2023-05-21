budgets = float(input())
season = input()

destination = ""
price = 0
location = ""
if budgets <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budgets * 0.30
        location = "Camp"
    elif season == "winter":
        price = budgets * 0.70
        location = "Hotel"

elif 100 < budgets <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budgets * 0.40
        location = "Camp"
    elif season == "winter":
        price = budgets * 0.80
        location = "Hotel"
elif budgets > 1000:
    destination = "Europe"
    if season == "summer" or season == "winter":
        price = budgets * 0.90
        location = "Hotel"


print(f"Somewhere in {destination}")
print(f"{location} - {price:.2f}")
