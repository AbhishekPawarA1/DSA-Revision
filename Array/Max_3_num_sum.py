# Maximum Product of Three Numbers

# Problem: Find the maximum product of any three numbers in a given array.
# Example:
# Input: nums = [1, 2, 3, 4]
# Output: 24 (from the product of 2 * 3 * 4)

nums = [1, 2, 3, 4]

nums.sort()
output=1
for i in range(len(nums)-1,(len(nums)-4),-1):
       output*=nums[i]
print(output)       