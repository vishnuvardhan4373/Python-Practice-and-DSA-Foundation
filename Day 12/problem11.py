names = ["Alice", "Bob", "Charlie"]
marks = [85, 90, 78]
student_dict = {}
for name, mark in zip(names, marks):
    student_dict[name] = mark
print(student_dict)