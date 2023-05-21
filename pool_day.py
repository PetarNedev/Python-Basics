import math
number_of_people = int(input())
entre_price = float(input())
sunbed_price = float(input())
umbrella_price = float(input())

total_entre_price = number_of_people * entre_price
needed_sunbed = math.ceil(number_of_people * 0.75) * sunbed_price
needed_umbrella = math.ceil(number_of_people * 0.5) * umbrella_price
total_price = total_entre_price + needed_umbrella + needed_sunbed
print(f"{total_price:.2f} lv.")