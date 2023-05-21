# 1.	Име на филм - текст
# 2.	Брой дни - цяло число в диапазона [1… 90]
# 3.	Брой билети  - цяло число в диапазона [100… 100000]
# 4.	Цена на билет - реално число в диапазона [5.0… 25.0]
# 5.	Процент за киното - цяло число в диапазона [5... 35]

name_of_movie = input()
number_of_days = int(input())
number_of_tickets = int(input())
price_per_tickets = float(input())
percent_for_cinema = int(input())

profit_per_day = number_of_tickets * price_per_tickets
total_profit = profit_per_day * number_of_days
cinema_percent = total_profit * (percent_for_cinema / 100)
profit_for_all_period = total_profit - cinema_percent
print(f"The profit from the movie {name_of_movie} is {profit_for_all_period:.2f} lv.")