numbers = [2, 5, 2, 3, 5, 2, 7, 5, 5]

most_frequent = None
highest_count = 0
for i in range(len(numbers)):
    tally = 0
    for j in range(len(numbers)):
        if numbers[i] == numbers[j]:
            tally += 1
    if tally > highest_count:
        highest_count = tally
        most_frequent = numbers[i]

print(f"Most frequent = {most_frequent}")
print(f"Frequency = {highest_count}")