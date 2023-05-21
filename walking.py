input_data = input()

sum_steps = 0
while input_data != "Going home":
    steps = int(input_data)
    sum_steps += steps

    if sum_steps >= 10000:
        break

    input_data = input()

if input_data == "Going home":
    home_steps = int(input())
    sum_steps += home_steps

diff = abs(sum_steps - 10000)
if sum_steps >= 10000:
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")