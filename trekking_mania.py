count_groups = int(input())
musala_sum = 0
montblanc_sum = 0
kilimandjaro_sum = 0
k2_sum = 0
everest_sum = 0
total_sum = 0
for i in range(1, count_groups + 1):
    people = int(input())
    total_sum += people

    if people <= 5:
        musala_sum += people
    elif people <= 12:
        montblanc_sum += people
    elif people <= 25:
        kilimandjaro_sum += people
    elif people <= 40:
        k2_sum += people
    else:
        everest_sum += people

percent_musala = musala_sum / total_sum * 100
percent_montblanc = montblanc_sum / total_sum * 100
percent_kilimandjaro = kilimandjaro_sum / total_sum * 100
percent_k2 = k2_sum / total_sum * 100
percent_everest = everest_sum / total_sum * 100
print(f"{percent_musala:.2f}%")
print(f"{percent_montblanc:.2f}%")
print(f"{percent_kilimandjaro:.2f}%")
print(f"{percent_k2:.2f}%")
print(f"{percent_everest:.2f}%")