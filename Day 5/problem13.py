numbers = [1, 2, 2, 3, 1, 2, 3]
highest_count = 0
most_frequent = numbers[0]
for number in numbers:
    count = 0
    for other in numbers:
        if number == other:
            count += 1
    if number != other:
        highest_count = count
        most_frequent = number
print(most_frequent)

        


