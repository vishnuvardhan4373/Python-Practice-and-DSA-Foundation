def is_anagram(text1,text2):
    if len(text1) != len(text2):
        return False
    freq1 = {}
    freq2 = {}
    for ch in text1:
        freq1[ch] = freq1.get(ch,0) + 1
    for ch in text2:
        freq2[ch] = freq2.get(ch,0) + 1
    return freq1 == freq2

text1 = "listen"
text2 = "silent"
print(is_anagram(text1,text2))