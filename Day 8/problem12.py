nums = [4, 1, 2, 4, 3, 4, 2, 4]

frequency = {}
for num in nums:
    frequency[num] = frequency.get(num, 0) + 1

most_frequent = None
highest_count = 0

for num, count in frequency.items():
    if count > highest_count:
        highest_count = count
        most_frequent = num

print(most_frequent)