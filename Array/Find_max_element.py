#  Find the Largest Element in an Array
# Question: Find the largest element in an integer array.
# Example:
# Input: arr = [1, 3, 5, 7, 9]
# Output: 9

arr = [1, 3, 5, 7, 9]
max=0
n=len(arr)
for i in range(n):
    if arr[i]>max:
        max=arr[i]
print(max)        