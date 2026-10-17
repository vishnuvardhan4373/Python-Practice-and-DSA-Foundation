def insert_element(nums, index, value):
    nums.append(0)
    for i in range(len(nums) - 1, index, -1):
        nums[i] = nums[i-1]
    nums[index] = value
    return nums

nums = [10, 20, 30, 40]
print(insert_element(nums,2,25))