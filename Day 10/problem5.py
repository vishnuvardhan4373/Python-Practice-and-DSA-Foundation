def is_palindrome(text):
    is_palindrome = True
    text1 = text[::-1]
    if text1 == text:
        return is_palindrome
    else:
        return False
text = "malayalap"
print(is_palindrome(text))