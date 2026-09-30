def count_unique_pairs(nums, target):
    seen = set()
    pairs = set()

    for num in nums:
        complement = target - num
        if complement in seen:
            # Store the pair as a sorted tuple to ensure uniqueness (e.g., (1, 5) and (5, 1) are treated as identical)
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)

    return len(pairs)


nums = [1, 5, 7, -1, 5]
target = 6
print(count_unique_pairs(nums, target))