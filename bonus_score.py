score = int(input())

bonus = 0
if score <= 100:
    bonus = 5

elif score <= 1000:
    bonus = (score*20)/100

else:
    bonus = (score * 10) / 100

if score % 2 == 0:
    bonus = bonus + 1
elif score % 10 == 5:
    bonus = bonus + 2
print(bonus)
print(score+bonus)

