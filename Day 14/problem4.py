nums = [4, 2, 7, 2, 5, 4]
seen = set()
for num in nums:
    if num in seen:
        print(num)
        break
    seen.add(num)