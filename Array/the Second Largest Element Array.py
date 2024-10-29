# Find the Second Largest Element in an Array
# Question: Find the second largest element in an integer array.
# Example:
# Input: arr = [3, 1, 4, 4, 5, 2]
# Output: 4 (the second largest element)

arr = [3, 1, 4, 4, 5, 2]
arr.sort()
print(len(arr)-2)
