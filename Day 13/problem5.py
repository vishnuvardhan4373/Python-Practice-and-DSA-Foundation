try:
    age = int(input("Enter age: "))

    if age < 0:
        raise ValueError("Age should not be negative.")

    print("Valid age.")

except ValueError as e:
    print(e)