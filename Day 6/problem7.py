list1 = [1, 2, 1, 2, 5]
list2 = [1, 2, 1, 2, 5]
for i in range(len(list1)):
    for j in range(i+1,len(list2)):
        if list1[i] == list2[j]:
            print(list1[i])