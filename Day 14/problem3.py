nums = [1, 2, 2, 3, 1, 2, 4]
frequency = {}
for num in nums:
    frequency[num] = frequency.get(num,0) + 1
print(frequency)
