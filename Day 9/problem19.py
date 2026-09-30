def first_non_repeating(text):
    frequency ={}
    for ch in text:
        frequency[ch] = frequency.get(ch,0)+1
    if frequency[ch] == 1:
        print(ch)
    
text = "aabbcde"
print(first_non_repeating(text))
