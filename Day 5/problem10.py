numbers = [1, 2, 3, 2, 4, 2, 5]
target = 2
total = 0
for number in numbers:
    if number == target:
        total += 1
print(f"Number of Occurances of {target} is:",total)