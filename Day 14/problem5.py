text = input("Enter Word: ")
reverse_text = text[::-1]
if reverse_text == text:
    print(f"{text} is a Palindrome.")
else:
    print(f"{text} is not a Palindrome.")