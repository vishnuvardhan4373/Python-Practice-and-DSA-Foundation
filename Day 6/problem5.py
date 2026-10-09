numbers = [1, 2, 3, 2, 4, 1, 5]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] != numbers[j]:
            continue
        else:
            print(numbers[i])