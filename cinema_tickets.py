student_tickets_counter = 0
kid_tickets_counter = 0
standard_tickets_counter = 0

command = input()
while command != "Finish":
    movie_name = command
    sits = int(input())
    free_sits = sits
    current_sits = 0
    while free_sits > 0:
        type_ticket = input()
        if type_ticket == "End":
            break
        elif type_ticket == "student":
            student_tickets_counter += 1
        elif type_ticket == "standard":
            standard_tickets_counter += 1
        elif type_ticket == "kid":
            kid_tickets_counter += 1
        current_sits += 1
        free_sits -= 1

    percent_of_hall = current_sits / sits * 100
    print(f"{movie_name} - {percent_of_hall:.2f}% full.")
    command = input()

total_sits = student_tickets_counter + standard_tickets_counter + kid_tickets_counter
percent_student_ticket = student_tickets_counter / total_sits * 100
percent_standard_ticket = standard_tickets_counter / total_sits * 100
percent_kid_ticket = kid_tickets_counter / total_sits * 100
print(f"Total tickets: {total_sits}")
print(f"{percent_student_ticket:.2f}% student tickets.")
print(f"{percent_standard_ticket:.2f}% standard tickets.")
print(f"{percent_kid_ticket:.2f}% kids tickets.")

