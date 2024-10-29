# Maximum Subarray Sum 

# Problem: Find the contiguous subarray within a one-dimensional array of numbers that has the largest sum.
# Example:
# Input: nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6 (from the subarray [4, -1, 2, 1])

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
larsum=0
output=[]
for i in range(len(nums)):
    res=[]
    for j in range(i,len(nums)):
        res.append(nums[j])
        if sum(res)>larsum:
            larsum=sum(res)
print(larsum) 
