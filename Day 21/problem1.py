def analyze_number(n):
    if n % 2 == 0:
        if n > 0:
            return "Positive Even."
        else:
            return "Negative Even."
    elif n %2 != 0:
        if n > 0:
            return "Positive Odd."
        else:
            return "Negative Odd."

print(analyze_number(-7))