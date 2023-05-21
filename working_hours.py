hours = int(input())
days = input()

if days == "Monday" \
        or days == "Tuesday" \
        or days == "Wednesday" \
        or days == "Thursday" \
        or days == "Friday" \
        or days == "Saturday":
    if 10 <= hours <= 18:
        print("open")
    else:
        print("closed")
else:
    print("closed")
