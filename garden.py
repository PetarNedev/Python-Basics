sqrm = int(input())
one_sqrm = 7.61
discount = 0.18

price_for_garden = sqrm * one_sqrm

price_for_discount = price_for_garden * discount

total_count = price_for_garden - price_for_discount

print(f"The final price is: {total_count:.2f} lv.")

print(f"The discount is: {price_for_discount:.2f} lv.")
