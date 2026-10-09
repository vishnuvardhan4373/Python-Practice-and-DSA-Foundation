def insert_element_slice(nums, index, value):
    return nums[:index] + [value] + nums[index:]

nums = [10, 20, 30, 40]
index = 2
value = 25
print(insert_element_slice(nums, index, value))
# Output: [10, 20, 25, 30, 40]