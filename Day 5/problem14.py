numbers = [1, 2, 3, 5]
for i in range(len(numbers)):
    if numbers[i+1] - numbers[i] == 1:
        print(i)
    else:
        print()