width = int(input())
length = int(input())
high = int(input())

room_cubic_meter = width * length * high
box_cubic_meter = 0
input_data = input()
while input_data != "Done":
    input_data = int(input_data)
    box_cubic_meter += input_data

    if room_cubic_meter < box_cubic_meter:
        break
    if input_data == "Done":
        break
    input_data = input()

diff = abs(room_cubic_meter - box_cubic_meter)
if room_cubic_meter < box_cubic_meter:
    print(f"No more free space! You need {diff} Cubic meters more.")
else:
    print(f"{diff} Cubic meters left.")