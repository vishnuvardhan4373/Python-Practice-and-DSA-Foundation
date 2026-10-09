nums = [1, 3, 4, 2, 2]
seen = set()
for num in nums:
    if num in seen:
        print("True")
        break
    seen.add(num)
else:
    print("False")