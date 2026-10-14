nums1 = [1, 3, 5, 7]
nums2 = [2, 4, 6, 8]
result = []
left1 = 0
right1 = len(nums1)
left2 = 0
right2 = len(nums2)
while left1 < right1 and left2 < right2:
    if nums1[left1] < nums2[left2]:
        result.append(nums1[left1])
        left1 += 1
    else:
        result.append(nums2[left2])
        left2 += 1
while left1 < right1:
    result.append(nums1[left1])
    left1 += 1
while left2 < right2:
    result.append(nums2[left2])
    left2 += 1
print(result)