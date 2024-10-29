# Find the Index of an Element
# Question: Find the index of a specific element in an array.
# Example:
# Input: arr = [10, 20, 30, 40], target = 30
# Output: 2 (the index of 30)

arr = [10, 20, 30, 40]
target = 30
n=len(arr)

for i in range(n):
    if arr[i]==target:
        print(i)
