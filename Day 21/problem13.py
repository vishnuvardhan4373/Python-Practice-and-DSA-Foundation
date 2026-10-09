def max_area(height):
    left = 0
    right = len(height) - 1
    maximum_area = 0

    while left < right:
        area = min(height[left],height[right]) * (right - left)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
        maximum_area = max(maximum_area, area)
    return maximum_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area(height))