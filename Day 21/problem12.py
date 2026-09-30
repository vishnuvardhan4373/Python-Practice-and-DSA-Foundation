nums = [1, 5, 7, -1, 5]
target = 6
seen = set()
pairs = set()

for num in nums:
    complement = target - num
    if complement in seen:
        pairs.add(tuple(sorted((num, complement))))
    seen.add(num)
print(len(pairs))