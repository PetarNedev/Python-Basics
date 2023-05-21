# 1.	Необходимо количество найлон (в кв.м.) - цяло число в интервала [1... 100]10
# 2.	Необходимо количество боя (в литри) - цяло число в интервала [1…100]11
# 3.	Количество разредител (в литри) - цяло число в интервала [1…30]4
# 4.	Часовете, за които майсторите ще свършат работата - цяло число в интервала [1…9]8

nylon=int(input())
paint=int(input())
razr=int(input())
working_hours=int(input())

# Сума за найлон: (10 + 2) * 1.50 = 18 лв.
# Сума за боя: (11 + 10%) * 14.50 = 175.45 лв.
# Сума за разредител: 4 * 5.00 = 20.00 лв.
# Сума за торбички: 0.40 лв.
# Обща сума за материали: 18 + 175.45 + 20.00 + 0.40 = 213.85 лв.
# Сума за майстори: (213.85 * 30%) * 8 = 513.24 лв.
# Крайна сума: 213.85 + 513.24 = 727.09 лв.

price_nylon=(nylon+2)*1.50
price_paint=(paint*1.10)*14.50
price_zarz=razr*5

total_price_for_materials=price_nylon+price_paint+price_zarz+0.4
price_workers=(total_price_for_materials*0.30)*working_hours
total_price=total_price_for_materials+price_workers
print(total_price)


