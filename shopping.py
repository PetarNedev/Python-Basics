budget = float(input())
number_GPU = int(input())
number_CPU = int(input())
number_RAM = int(input())

count_gpu = number_GPU * 250
cost_cpu = (count_gpu * 35) / 100
count_cpu = number_CPU * cost_cpu
cost_ram = (count_gpu * 10) / 100
count_ram = number_RAM * cost_ram
total_sum = count_ram + count_cpu + count_gpu
if number_GPU > number_CPU:
    total_sum = total_sum - ((total_sum * 15)/100)
diff = abs(total_sum - budget)
if total_sum <= budget:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")
