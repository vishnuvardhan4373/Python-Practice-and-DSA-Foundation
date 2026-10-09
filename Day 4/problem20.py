def primes_in_range(start, end):
    found_any = False    
    for i in range(start, end):
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
        print(f"No Prime Numbers between {start} and {end}.")
print(primes_in_range(2, 10))