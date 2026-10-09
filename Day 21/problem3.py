def count_vowels(text):
    vowels = 'AEIOUaeiou'
    return sum(1 for ch in text if ch in vowels)

text = "Programming"
print(count_vowels(text))