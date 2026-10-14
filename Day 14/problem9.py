text = "python is easy and python is powerful"
list1 = text.split()
count = {}
for word in list1:
    count[word] = count.get(word,0) + 1
print(count)