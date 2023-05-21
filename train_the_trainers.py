number_judge = int(input())
input_data = input()
iteration = 0
average_success = 0
while input_data != "Finish":

    presentation = input_data
    point = 0
    for i in range(number_judge):
        rating = float(input())
        point += rating
        average_success += rating
        iteration += 1

    print(f"{presentation} - {point / number_judge:.2f}.")
    input_data = input()

if input_data == "Finish":
    print(f"Student's final assessment is {average_success / iteration:.2f}.")
