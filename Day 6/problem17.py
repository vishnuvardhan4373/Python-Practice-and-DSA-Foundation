numbers = [10, 20, 30]
duplicate_exists = False
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] == numbers[j]:
            duplicate_exists = True
            break
    if duplicate_exists:
        break
if duplicate_exists:
    print("Duplicate exists")
else:
    print("All Unique")
        