numbers = [2, 4, 3, 7, 5, 8, 1]
target = 9
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i],numbers[j])