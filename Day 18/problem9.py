nums_a = [5, 2, 8, 1, 3]
sorted_a = sorted(nums_a)
print("Part A:")
print("Original:", nums_a)
print("Sorted:", sorted_a)
print()

nums_b = [5, 2, 8, 1, 3]
nums_b.sort(reverse=True)
print("Part B:")
print("In-place sorted (descending):", nums_b)
print()

nums_c = [5, 2, 8, 1, 3]
nums_c.sort()
print("Part C:")
print("Result of nums.sort():", nums_c)
print()

nums_d = [10, 4, 7, 2, 9]
sorted_d = sorted(nums_d, reverse=True)
print("Part D:")
print("Original:", nums_d)
print("Sorted (descending):", sorted_d)