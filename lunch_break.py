from math import ceil
name = input()
cont_episod = int(input())
cont_break = int(input())

time_lunch = cont_break / 8
time_break = cont_break / 4
left_time = cont_break - time_break - time_lunch
diff = abs(left_time - cont_episod)
if left_time >= cont_episod:
    print(f"You have enough time to watch {name} and left with {ceil(diff)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name}, you need {ceil(diff)} more minutes.")