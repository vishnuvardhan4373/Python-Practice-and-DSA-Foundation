nums = [100, 4, 200, 1, 3, 2]
seen = set(nums)
longest = 0
for num in seen:
    if num - 1 not in seen:
        current = num
        largest = 1
        while current + 1 in seen:
            current += 1
            largest += 1
        longest = max(longest, largest)
print(longest)