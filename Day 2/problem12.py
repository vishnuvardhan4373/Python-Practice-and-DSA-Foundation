num = int(input("Enter Number: "))

if num >0:
    if num%2 == 0:
        print("Positive and Even")
    else:
        print("Positive and Odd")
elif num <0:
    if num%2 == 0:
        print("Negative and Even")
    else:
        print("Negative and Odd")
elif num == 0:
    if num%2 == 0:
        print("Zero and Even")

     