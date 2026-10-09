def max_of_vowels(text,k):
    vowels = 'aeiou'
    vowels_count = sum(1 for i in range(k) if text[i] in vowels)
    max_vowel = vowels_count

    for i in range(k,len(text)):
        if text[i-k] in vowels:
            vowels_count -= 1
        if text[i] in vowels:
            vowels_count += 1
        max_vowel = max(max_vowel, vowels_count)
        if max_vowel == k:
            return k

    return max_vowel
text = "abciiidef"
print(max_of_vowels(text,3))