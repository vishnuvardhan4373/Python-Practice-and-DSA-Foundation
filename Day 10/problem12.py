text = "aabbcddee"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch,0) + 1
for ch, count in counts.items():
    if count == 1:
        print(ch)
        break