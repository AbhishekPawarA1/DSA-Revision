# Maximum Product of Two Elements in an Array
# Question: Find the maximum product of two distinct elements in an integer array.
# Example:
# Input: arr = [1, 5, 4, 5]
# Output: 20 (product of 5 * 4)

arr = [1, 5, 4, 5]
n=len(arr)-1
multiply=0
for i in range(n):
    if (arr[i]*arr[i+1])>multiply:
        multiply=(arr[i]*arr[i+1])
print(multiply)        
