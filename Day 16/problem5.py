def calculate_total(marks):
    return sum(marks)
def calculate_average(total,count):
    return total/count
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    else:
        return "D"
marks = [80, 75, 90, 85, 70]

total = calculate_total(marks)
average = calculate_average(total,len(marks))
grade = calculate_grade(average)

print(f"Total: {total}")
print(f"Average: {average}")
print(f"Grade: {grade}")