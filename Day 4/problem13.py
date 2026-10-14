def count_vowels(text):
    vowel_count = 0
    lower_text = text.lower()
    vowel = 'aeiou'
    for ch in lower_text:
        if ch in vowel:
            vowel_count += 1
    return vowel_count
text = input("Enter Text: ")
print("Number of Vowels in the Given Text is:",count_vowels(text))
