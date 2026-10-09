students = [("Alice", 85), ("Bob", 92), ("Charlie", 78), ("David", 95)]
student_name = input("Enter Student Name: ")
for name, mark in students:
    if student_name == name:
        print(f"{student_name}:{mark}")