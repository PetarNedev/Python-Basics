product = input()
city = input()
quantity = float(input())
price = 0

if city == "Sofia":
    if product == "coffee":
        price = quantity * 0.50
        print(f"{price:.2f}")
    elif product == "water":
        price = quantity * 0.80
        print(f"{price:.2f}")
    elif product == "beer":
        price = quantity * 1.20
        print(f"{price:.2f}")
    elif product == "sweets":
        price = quantity * 1.45
        print(f"{price:.2f}")
    elif product == "peanuts":
        price = quantity * 1.60
        print(f"{price:.2f}")

if city == "Varna":
    if product == "coffee":
        price = quantity * 0.45
        print(f"{price:.2f}")
    elif product == "water":
        price = quantity * 0.70
        print(f"{price:.2f}")
    elif product == "beer":
        price = quantity * 1.10
        print(f"{price:.2f}")
    elif product == "sweets":
        price = quantity * 1.35
        print(f"{price:.2f}")
    elif product == "peanuts":
        price = quantity * 1.55
        print(f"{price:.2f}")

if city == "Plovdiv":
    if product == "coffee":
        price = quantity * 0.40
        print(f"{price:.2f}")
    elif product == "water":
        price = quantity * 0.70
        print(f"{price:.2f}")
    elif product == "beer":
        price = quantity * 1.15
        print(f"{price:.2f}")
    elif product == "sweets":
        price = quantity * 1.30
        print(f"{price:.2f}")
    elif product == "peanuts":
        price = quantity * 1.50
        print(f"{price:.2f}")
