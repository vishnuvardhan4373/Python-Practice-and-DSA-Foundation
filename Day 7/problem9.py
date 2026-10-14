numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
target = 10
count = 0

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] + numbers[j] == target:
            count += 1
print(count)