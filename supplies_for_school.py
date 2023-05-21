# •	Пакет химикали - 5.80 лв.
# •	Пакет маркери - 7.20 лв.
# •	Препарат - 1.20 лв (за литър)
num_pen=int(input())
num_marker=int(input())
lt_prep=int(input())
discount=int(input())

# Цена на пакетите химикали => 2 * 5.80 = 11.60 лв.
# Цена на пакетите маркери => 3 * 7.20 = 21.60 лв.
# Цена на препарата => 4 * 1.20 = 4.80 лв.
# Цена за всички материали => 11.60 + 21.60 + 4.80 = 38.00 лв.
# 25% = 0.25
# Цена с намаление = 38.00 – (38.00 * 0.25) = 28.50 лв.

price_pen=num_pen*5.80
price_marker=num_marker*7.20
price_prep=lt_prep*1.20
total_price=price_pen+price_marker+price_prep
price_discout=total_price-((total_price*discount)/100)
print(price_discout)
