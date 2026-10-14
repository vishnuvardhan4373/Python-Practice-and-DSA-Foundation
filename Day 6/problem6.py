numbers = [10, 20, 30, 40, 50]
count = 0
for i in range(len(numbers)):
    for j in range(i+1,len(numbers)):
        count += 1
print(count)