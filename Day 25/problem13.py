nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

total = 0
min_prefix = 0
max_sub_array = None

for n in nums:
    total += n
    sub_array_sum = total - min_prefix
    if max_sub_array is None or sub_array_sum > max_sub_array:
        max_sub_array = sub_array_sum
    if total < min_prefix:
        min_prefix = total

print(max_sub_array)  