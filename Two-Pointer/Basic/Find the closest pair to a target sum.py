# Find the closest pair to a target sum

# Problem: Find the closest pair to a target sum in a sorted array.
# Example:
# Input: arr = [1, 3, 4, 7], target = 8
# Output: (3, 4)

arr = [1, 2, 4, 5, 7, 11, 15, 18, 20, 25, 30, 35, 40, 45, 50]
target = 32

left = 0
right = len(arr) - 1
res = []
min_diff = 99999 
while left < right:
    current_sum = arr[left] + arr[right]
    if current_sum < target:
        diff = target - current_sum
        if diff < min_diff:
            min_diff = diff
            res = [(arr[left], arr[right])]  
        left += 1 
    else:
        right -= 1  

print(res)

# time complexity is 0(n)
# space complexity is 0(1)