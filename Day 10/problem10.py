text = "hello world"
vowels = 'aeiouAEIOU'
result = " "
for ch in text:
    if ch not in vowels:
        result += ch
print(result)