init_hour = int(input())
init_minute = int(input())

total_time = (init_hour * 60) + init_minute + 15
hour = total_time // 60
minutes = total_time % 60

if hour > 23:
    hour = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")
else:
    print(f"{hour}:{minutes}")
