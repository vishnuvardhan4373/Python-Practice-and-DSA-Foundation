numbers = [10, -5, 0, 8, -2, 0, 4]
positive_count = 0
negative_count = 0
zero_count = 0

for number in numbers:
    if number == 0:
        zero_count += 1
    elif number > 0:
        positive_count += 1
    else:
        negative_count += 1
print("Positive:",positive_count)
print("Negative:",negative_count)
print("Zero:",zero_count)