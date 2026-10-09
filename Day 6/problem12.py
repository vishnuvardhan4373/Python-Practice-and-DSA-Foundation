numbers = [1, 2, 3, 4, 5, 6]
target = 7

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            print(numbers[i],numbers[j])