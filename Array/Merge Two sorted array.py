#  Merge Two Sorted Arrays
# Question: Merge two sorted arrays into a single sorted array.
# Example:
# Input: arr1 = [1, 3, 5], arr2 = [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
array=arr1+arr2;
n=len(array)
for i in range(n):
    for j in range(n-i-1):
        if array[j]>array[j+1]:
            array[j],array[j+1]=array[j+1],array[j]
print(array)        

        

