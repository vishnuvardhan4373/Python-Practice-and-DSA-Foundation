def non_repeating_char(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch,0) + 1
    for ch in freq:
        if freq[ch] == 1:
            return ch
    return None

text = "aabbcdd"
print(non_repeating_char(text))