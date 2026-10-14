original_list = [4, 3, 2, 4, 1, 3, 4]
unique_numbers = []
for num in original_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
less_frequent = None
least_count = 0
for target in unique_numbers:
    tally = 0
    for item in original_list:
        if item == target:
            tally += 1
    if tally < least_count:
        least_count = tally
        less_frequent = target
print(f"Less frequent = {less_frequent}")
print(f"Frequency = {least_count}")