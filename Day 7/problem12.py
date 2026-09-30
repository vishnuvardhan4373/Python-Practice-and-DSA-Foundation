numbers = [4, 15, 2, 9, 20]
max_difference = abs(numbers[0]-numbers[1])

for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        difference = abs(numbers[i] - numbers[j])

    if difference > max_difference:
        max_difference = difference
        first = numbers[i]
        second = numbers[j]
print(first,second)
print(max_difference)