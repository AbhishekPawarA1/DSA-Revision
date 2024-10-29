# Subarray with Given Sum
# Question: Given an unsorted array and a target sum, find a contiguous subarray that sums to the target sum. 
# Return the start and end indices of this subarray.
# Example: Input: arr = [1, 4, 20, 3, 10, 5], 
# target = 33, Output: [2, 4] (Subarray [20, 3, 10] adds up to 33).

arr = [1, 4, 20, 3, 10, 5]
target = 33
n=len(arr)
output=[]
for i in range(n):
    res=0
    for j in range(i,n):
        res+=arr[j]
        if res==target:
           output =[i,j]
print(output)




