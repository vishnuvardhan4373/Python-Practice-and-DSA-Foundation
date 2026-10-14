name = input("Enter Name: ")
with open("students.txt","r") as file:
    content = file.read()
    students = content.split("\n")
    for student in students:
        if name in student:
           print("Student Found.")
           break
    else:
        print("student Doesn't Exist.")