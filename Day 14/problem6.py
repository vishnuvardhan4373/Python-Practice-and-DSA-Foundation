text = "programming"
counts = {}
for ch in text:
    counts[ch] = counts.get(ch,0) + 1
print(counts)