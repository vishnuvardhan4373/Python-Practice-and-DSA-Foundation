def find_element(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

def display_search_result(index):
    if index != -1:
        print(f"Element found at index {index}")
    else:
        print("Element not found")

nums = [10, 20, 30, 40, 50]

target1 = 30
index1 = find_element(nums, target1)
display_search_result(index1) 

target2 = 99
index2 = find_element(nums, target2)
display_search_result(index2)  