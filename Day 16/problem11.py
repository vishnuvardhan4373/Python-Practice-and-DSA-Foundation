def largest_number(nums):
    return max(nums)
def smallest_number(nums):
    return min(nums)
def calculate_sum(nums):
    return sum(nums)
def calculate_average(total,count):
    return total / count
def count_even(nums):
    even_count = 0
    for num in nums:
        if num %2 == 0:
            even_count += 1
    return even_count
def count_odd(nums):
    return len(nums) - count_even(nums)
def analyze_list(nums):
    largest = largest_number(nums)
    smallest = smallest_number(nums)
    total = calculate_sum(nums)
    average = calculate_average(total,len(nums))
    even_count = count_even(nums)
    odd_count = count_odd(nums)
    return largest, smallest, total, average, even_count, odd_count

nums = [12, 7, 25, 4, 18, 9, 30]
print(analyze_list(nums))
    
