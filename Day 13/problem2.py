try:
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))
    print(num1/num2)
except ValueError:
    print("Invalid Number.")
except ZeroDivisionError:
    print("Cannot Divide by Zero")