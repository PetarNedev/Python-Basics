name_actor = input()
init_points = float(input())
people = int(input())

total_points = init_points

for i in range(1, people + 1):
    name = input()
    points = float(input())
    current_points = (len(name) * points) / 2
    total_points += current_points
    if total_points >= 1250.5:
        break

if total_points < 1250.5:
    diff = abs(total_points - 1250.5)
    print(f'Sorry, {name_actor} you need {diff:.1f} more!')
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
