list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]
result = []
for i in range(len(list1)):
    for j in range(len(list2)):
        if list1[i] == list2[j]:
            result.append(list1[i])
print(result)