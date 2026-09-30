try:
    student = {
    "name": "Alice",
    "age": 22,
    "marks": 90
    }
    key = input("Enter Key: ")
    print(student[key])
except KeyError:
    print("The Required Key doesn't Exists in the Dictionary.")