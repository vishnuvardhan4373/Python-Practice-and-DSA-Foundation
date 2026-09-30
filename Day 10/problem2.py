text = "Python"
vowel_count = 0
vowel = 'aeiou'
text1 = text.lower()
for ch in text1:
    if ch in vowel:
        vowel_count += 1
print(vowel_count)