text = "abciiidef"
k=3
vowels = 'aeiou'
new_text = sum(1 for ch in text if ch in vowels)

print(new_text)