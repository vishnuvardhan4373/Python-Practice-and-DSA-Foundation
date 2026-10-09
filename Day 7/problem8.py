numbers = [10, 20, 30, 40]
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        if numbers[i] != numbers[j]:
            print(numbers[i],numbers[j])