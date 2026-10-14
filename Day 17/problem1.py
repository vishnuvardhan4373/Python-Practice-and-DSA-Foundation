def Searching_number(nums,target):
    for num in nums:
        if num == target:
            return "Element Found."
    return -1
nums = [10, 20, 30, 40, 50]
print(Searching_number(nums,30))