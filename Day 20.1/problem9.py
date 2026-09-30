nums = [1, 5, 7, -1, 5]
target = 6
count = 0
seen = {}
for i,num in enumerate(nums):
    needed = target - num
    if needed in seen:
        count += seen[needed]
    seen[num] = seen.get(num,0) + 1
print(count)