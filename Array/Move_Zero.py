# Problem: Move all zeroes in an array to the end while maintaining the order of non-zero elements.
# Example:
# Input: nums = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

nums = [0, 1, 0, 3, 12]
output=[]
zero=[]
for i in range(len(nums)):
    if nums[i]==0:
        zero.append(nums[i])
    else:
        output.append(nums[i])    
print(output+zero)        