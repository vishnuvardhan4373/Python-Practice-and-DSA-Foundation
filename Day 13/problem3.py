try:
    nums = [10, 20, 30, 40]
    index_value = int(input("Enter Index Value: "))
    print(nums[index_value])
except IndexError:
    print("Index is Out of Range.")