# Sum of All Elements in an Array
# Question: Calculate the sum of all elements in an integer array.
# Example:
# Input: arr = [1, 2, 3, 4]
# Output: 10 (1 + 2 + 3 + 4)

arr = [1, 2, 3, 4]
sum=0
n=len(arr)
for i in range(n):
    sum+=arr[i]
print(sum)    

