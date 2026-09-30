text = "PyThOn"
uppercase_count = 0
lowercase_count = 0
for ch in text:
    if ch.islower():
        lowercase_count += 1
    elif ch.isupper():
        uppercase_count += 1
print(f"lower case: {lowercase_count}")
print(f"upper case: {uppercase_count}")