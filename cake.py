length = int(input())
width = int(input())
cake = length * width
pieces = cake
all_pieces = 0
input_data = input()
while input_data != "STOP":
    input_data = int(input_data)

    pieces -= input_data
    all_pieces += input_data

    if pieces <= 0:
        break

    input_data = input()
diff = abs(cake - all_pieces)
if input_data == "STOP" and pieces > 0:
    print(f"{diff} pieces are left.")
else:
    print(f"No more cake left! You need {diff} pieces more.")
