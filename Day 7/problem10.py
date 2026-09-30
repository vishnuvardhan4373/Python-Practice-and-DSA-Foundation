numbers = [5, 8, 2, 9, 8]
has_duplicate = False

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            has_duplicate = True
            break 
    if has_duplicate:
        break      

if has_duplicate:
    print("Duplicate exists")
else:
    print("No duplicates found")