def even_count(numbers):
    count = 0
    for number in numbers:
        if number %2 == 0:
            count += 1
    return count
numbers = [1, 6, 8, 9, 5, 12]
print("Number of Even Numbers in the List are:",even_count(numbers))