with open("numbers.txt","r") as file:
    content = file.read()
    list1 = content.split()
    max_num = max(list1)
    min_num = min(list1)
    length = len(list1)
    numbers = []
    for num in list1:
        num = int(num)
        numbers.append(num)
    total = sum(numbers)
    average = total/length
    
    print(f"Minimum Number: {min_num}")
    print(f"Maximum Number: {max_num}")
    print(f"Length of List1: {length}")
    print(f"Sum of Numbers: {total}")
    print(f"Average of Numbers: {average}")
 