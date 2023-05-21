text = input()
sum = 0

for letter in range(len(text)):
    if text[letter] == "a":
        sum += 1
    if text[letter] == "e":
        sum += 2
    if text[letter] == "i":
        sum += 3
    if text[letter] == "o":
        sum += 4
    if text[letter] == "u":
        sum += 5

print(sum)
