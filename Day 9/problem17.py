def char_frequency(text):
    frequency = {}
    for ch in text:
        frequency[ch] = frequency.get(ch,0)+1
    return frequency

text = "programming"
print(char_frequency(text))