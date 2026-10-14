s = "aabbcdde"
frequency = {}
for ch in s:
    frequency[ch] = frequency.get(ch, 0) + 1
for ch in s:
    if frequency[ch] == 1:
        print(ch)
        break