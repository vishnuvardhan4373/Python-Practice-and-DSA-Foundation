numbers = [4, 2, 4, 1, 2, 5, 1]
result = []
for i in range(len(numbers)):
    if numbers[i] not in result:
        result.append(numbers[i])
print(result)

