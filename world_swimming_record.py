import math

record_in_seconds = float(input())
distance_meter = int(input())
time_for_meter = float(input())

swim_seconds = distance_meter * time_for_meter
added_time = distance_meter // 15 * 12.5
total_time = swim_seconds + added_time

if total_time < record_in_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    print(f"No, he failed! He was {total_time - record_in_seconds:.2f} seconds slower.")
