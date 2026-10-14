def first_non_repeating(text):
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch, 0) + 1
    non_frequent = next((ch for ch in frequency if frequency[ch] == 1), None)
    return non_frequent

text = "aabbcdde"
print(first_non_repeating(text))                                                