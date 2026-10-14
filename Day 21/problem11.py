def is_palindrome(text):
    new_text = "".join(ch.lower() for ch in text if ch.isalnum())
    return new_text == new_text[::-1]

text = "A man, a plan, a canal: Panama"
print(is_palindrome(text))