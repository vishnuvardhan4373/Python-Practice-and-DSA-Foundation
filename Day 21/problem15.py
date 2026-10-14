def subarray_sum(nums, k):
    count = 0
    total = 0
    prefix_counts = {0: 1}   # empty prefix sums to 0, seen once

    for num in nums:
        total += num
        # if (total - k) was seen before, that subarray sums to k
        count += prefix_counts.get(total - k, 0)
        prefix_counts[total] = prefix_counts.get(total, 0) + 1

    return count

nums = [1, 1, 1]
print(subarray_sum(nums, 2))  # 2