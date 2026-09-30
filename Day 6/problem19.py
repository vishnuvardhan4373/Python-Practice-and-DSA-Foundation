original_list = [4, 3, 2, 4, 1, 3, 4]
unique_numbers = []
for num in original_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
most_frequent = None
highest_count = 0
for target in unique_numbers:
    tally = 0
    for item in original_list:
        if item == target:
            tally += 1
    if tally > highest_count:
        highest_count = tally
        most_frequent = target
print(f"Most frequent = {most_frequent}")
print(f"Frequency = {highest_count}")