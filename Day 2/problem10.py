units = int(input("Enter Voltage Units: "))
if units > 0 and units<=100:
    print(units*5,"rupees to be Paid.")
elif units > 100 and units <= 200:
    print(units*7,"rupees to be Paid.")
elif units > 200 and units <= 300:
    print(units*10,"rupees to be Paid.")
elif units > 300:
    print(units*15,"rupees to be Paid.")
