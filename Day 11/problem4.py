nums = [1, 2, 3, 2, 4, 5, 1, 6]
seen = set()
for num in nums:
    if num in seen:
        print("Seen Duplicates:",num)
    seen.add(num)