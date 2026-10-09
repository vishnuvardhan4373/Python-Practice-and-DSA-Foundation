def delete_element(nums, index):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]

    nums = nums[:len(nums) - 1]
    return nums

nums = [10, 20, 30, 40]
print(delete_element(nums, 1))