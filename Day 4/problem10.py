def sum_even():
    even_total = 0
    for number in numbers:
        if number %2 == 0:
            even_total += number
    return even_total
numbers = [2, 12, 15, 28, 14, 19, 23, 37]
print("Sum of Even Numbers in the Given List is:",sum_even())
