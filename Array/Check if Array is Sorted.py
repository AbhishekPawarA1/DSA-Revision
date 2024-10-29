# Check if Array is Sorted
# Question: Check if a given array is sorted in ascending order.
# Example:
# Input: arr = [1, 2, 3, 4]
# Output: True

arr = [1, 2, 3, 4, 8]
n=len(arr)
res=[]
for i in range(n-1):
    if arr[i]>arr[i+1]:
        print("False")
    else:
        res.append(arr[i])
if len(res)==n-1:
    print("True")     