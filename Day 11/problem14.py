text = "abcdef"
required = "abcdefghi"
text_set = set(text)
required_set = set(required)
print(required_set - text_set)