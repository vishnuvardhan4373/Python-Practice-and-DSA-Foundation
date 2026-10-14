def calculate_total(marks):
    return sum(marks)
def calculate_average(total,count):
    return total / count
def calculate_grade(average):
    if average >= 90:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    elif average >= 40:
        return "E"
    else:
        return "F"
def check_pass_fail(marks):
    for mark in marks:
        if mark < 40:
            return "Fail"
        else:
            return "Pass"

def display_result(marks):
    total = calculate_total(marks)
    average = calculate_average(total,len(marks))
    grade = calculate_grade(average)
    result = check_pass_fail(marks)
    return total, average, grade, result

marks = [35, 76, 92, 67, 81]
print(display_result(marks))