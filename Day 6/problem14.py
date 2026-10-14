numbers = [10, 3, 8, 15, 6]

minimum_difference = abs(numbers[0] - numbers[1])
first = numbers[0]
second = numbers[1]

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        difference = abs(numbers[i] - numbers[j])

        if difference < minimum_difference:
            minimum_difference = difference
            first = numbers[i]
            second = numbers[j]

print(first, second)
print(minimum_difference)