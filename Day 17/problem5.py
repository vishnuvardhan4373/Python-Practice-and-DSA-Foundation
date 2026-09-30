def char_search(text,target):
    for i, ch in enumerate(text):
        if ch == target:
            return i
    return -1
text = "programming"
print(char_search(text,"g"))