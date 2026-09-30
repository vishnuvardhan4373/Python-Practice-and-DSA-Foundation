numbers = [10, 3, 8, 15, 6]
maximum_difference = abs(numbers[0] - numbers[1])
first = numbers[0]
second = numbers[1]

for i in range(len(numbers)):
    for j in range(len(numbers)):
        difference = abs(numbers[i] - numbers[j])
        if difference > maximum_difference:
            maximum_difference = difference
            first = numbers[i]
            second = numbers[j]
print(first,second)
print(maximum_difference)