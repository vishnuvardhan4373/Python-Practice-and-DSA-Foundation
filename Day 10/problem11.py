def most_frequent(text):
    counts = {}
    for ch in text:
        counts[ch] = counts.get(ch, 0) + 1

    max_char = ""
    max_count = 0
    for ch, count in counts.items():
        if count > max_count:
            max_count = count
            max_char = ch

    return max_char


text = "banana"
print(most_frequent(text))