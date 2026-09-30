numbers = [2, 7, 11, 15]
target = 9
result = []
for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] + numbers[j] == target:
            result.append(numbers[i])
            result.append(numbers[j])

print(result)