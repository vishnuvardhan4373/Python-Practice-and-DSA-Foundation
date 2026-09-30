students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
highest = 0
student_name = ""
for name, mark in students:
    if mark > highest:
        highest = mark
        student_name = name
print(f"{student_name}: {highest}")
