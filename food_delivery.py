num_chicken_menu=int(input())
num_fish_menu=int(input())
num_vegetarian_menu=int(input())

chicken_price=num_chicken_menu*10.35
fish_price=num_fish_menu*12.40
vegetarian_price=num_vegetarian_menu*8.15
total_price_menu=chicken_price+fish_price+vegetarian_price
desert_prise=total_price_menu*(20/100)
delivery_price=2.50
price_of_order=total_price_menu+desert_prise+delivery_price

print(price_of_order)

