numbers = [12, 45, 7, 89, 23]
smallest = numbers[0]
for number in numbers:
    if number < smallest:
        smallest = number
print("Smallest Number in the List is:",smallest)