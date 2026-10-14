numbers = [1, 2, 3, 2, 4, 1, 5, 2]
seen_duplicates = []

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            if numbers[i] not in seen_duplicates:
                seen_duplicates.append(numbers[i])

print("Numbers occurring more than once =", len(seen_duplicates))