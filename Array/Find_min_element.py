#  Find the Smallest Element in an Array
# Question: Find the smallest element in an integer array.
# Example:
# Input: arr = [10, 4, 3, 8, 5]
# Output: 3

min=999999999
arr = [10, 4, 3, 8, 5]
n=len(arr)
for i in range(n):
    if arr[i]<min:
        min=arr[i]
print(min)        