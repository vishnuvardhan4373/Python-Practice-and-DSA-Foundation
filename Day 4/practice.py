a = int(input("Enter Start Range: "))
b = int(input("Enter End Range: "))

for i in range(a,b):
    if i < 2:
        continue        
    is_prime = True
    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break        
    if is_prime:
        print(i)
        found_any = True   
if not found_any:
    print(f"No Prime Numbers between {a} and {b}.")