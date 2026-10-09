def max_area_for_water(height):
    left = 0
    right = len(height) - 1
    result = []

    while left < right:
        length = min((height[left],height[right]))
        breadth = right - left
        area = length * breadth
        result.append(area)
        Highest_area = max(result)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return Highest_area

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(max_area_for_water(height))