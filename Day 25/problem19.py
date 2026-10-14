nums1 = [1, 2, 2, 3, 4]
nums2 = [2, 2, 4, 6]
seen = set(nums1)
result = []
for num in nums2:
    if num in seen and num not in result:
        result.append(num)
print(result)
