def palindrome(text):
    new_text = "".join(ch.lower() for ch in text if ch.isalnum())

    left = 0
    right = len(new_text) - 1

    while left < right:
        if new_text[left] == new_text[right]:
            left += 1
            right -= 1
        else:
            return False
    return True
          
text = "A man, a plan, a canal: Panama;"
print(palindrome(text))