nums = [5, 3, 4, 2, 3, 7, 4]
seen = set()
for num in nums:
    if num in seen:
        print(num)
        break
    seen.add(num)