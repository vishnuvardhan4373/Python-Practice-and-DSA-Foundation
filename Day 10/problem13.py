text = "programming"
seen = set({})
result = ""
for ch in text:
    if ch not in seen:
        seen.add(ch)
        result += ch
print(result)