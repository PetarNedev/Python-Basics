city = input()
sales = float(input())
valid_city = True
total_price = 0

if city == "Sofia":
    if 0 <= sales <= 500:
        total_price = sales * 0.05
    elif 500 < sales <= 1000:
        total_price = sales * 0.07
    elif 1000 < sales <= 10000:
        total_price = sales * 0.08
    elif sales > 10000:
        total_price = sales * 0.12
    else:
        valid_city = False

elif city == "Varna":
    if 0 <= sales <= 500:
        total_price = sales * 0.045
    elif 500 < sales <= 1000:
        total_price = sales * 0.075
    elif 1000 < sales <= 10000:
        total_price = sales * 0.10
    elif sales > 10000:
        total_price = sales * 0.13
    else:
        valid_city = False

elif city == "Plovdiv":
    if 0 <= sales <= 500:
        total_price = sales * 0.055
    elif 500 < sales <= 1000:
        total_price = sales * 0.08
    elif 1000 < sales <= 10000:
        total_price = sales * 0.12
    elif sales > 10000:
        total_price = sales * 0.145
    else:
        valid_city = False

else:
    valid_city = False

if valid_city:
    print(f"{total_price:.2f}")
else:
    print("error")
