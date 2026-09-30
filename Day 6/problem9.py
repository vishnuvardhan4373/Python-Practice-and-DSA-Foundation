list = [1, 2, 1, 3, 2, 4, 3]
for i in range(len(list)):
    for j in range(i+1,len(list)):
        if list[i] == list[j]:
            print(list[i])