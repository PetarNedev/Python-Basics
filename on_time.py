hour_exam = int(input())
minute_exam = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

all_minute_exam = (hour_exam * 60) + minute_exam
all_minute_arrival = (arrival_hour * 60) + arrival_minute
diff = abs(all_minute_arrival - all_minute_exam)

if all_minute_arrival > all_minute_exam:
    print("Late")
    if diff >= 60:
        hour = diff // 60
        minute = diff % 60
        print(f"{hour}:{minute:02d} hours after the start")
    else:
        print(f"{diff} minutes after the start")

elif all_minute_arrival == all_minute_exam or diff <= 30:
    print("On time")
    if diff > 0:
        print(f"{diff} minutes before the start")
else:
    print("Early")
    if diff >= 60:
        hour = diff // 60
        minutes = diff % 60
        print(f"{hour}:{minutes:02d} hours before the start")
    else:
        print(f"{diff} minutes before the start")
