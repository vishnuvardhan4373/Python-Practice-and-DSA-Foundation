text = "aabbcddee"
count = {}
for ch in text:
    count[ch] = count.get(ch, 0) + 1
    if count[ch] == 1:
        print(ch)
        break