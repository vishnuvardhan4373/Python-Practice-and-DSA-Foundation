def frequency_character(text):
    frequency = {}

    for ch in text:
        frequency[ch] = frequency.get(ch,0) + 1
    return frequency

text = "banana"
print(frequency_character(text))