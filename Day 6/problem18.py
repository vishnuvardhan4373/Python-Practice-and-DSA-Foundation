original_list = [4, 3, 2, 4, 1, 3, 4]
unique_numbers = []

for num in original_list:
    if num not in unique_numbers:
        unique_numbers.append(num)
for target in unique_numbers:
    tally = 0  

    for item in original_list:
        if item == target:
            tally += 1 

    print(f"{target} appears {tally} times")