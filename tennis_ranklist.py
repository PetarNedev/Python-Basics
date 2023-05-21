import math
tournament_number = int(input())
init_point = int(input())

wins = 0
point = 0
for i in range(1, tournament_number + 1):
    level = input()

    if level == "W":
        wins += 1
        point += 2000
    elif level == "F":
        point += 1200
    elif level == "SF":
        point += 720

total_points = point + init_point
avg_point = math.floor(point / tournament_number)
percent_of_wins = (wins / tournament_number) * 100
print(f'Final points: {total_points}')
print(f'Average points: {avg_point}')
print(f'{percent_of_wins:.2f}%')
