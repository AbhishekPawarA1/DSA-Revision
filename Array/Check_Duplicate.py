# Contains Duplicate

# Problem: Check if there are any duplicates in an array of integers.
# Example:
# Input: nums = [1, 2, 3, 4, 5]
# Output: False
# Input: nums = [1, 2, 3, 4, 1]
# Output: True


nums = [1, 2, 3, 4, 5]
output=[]
for i in range(len(nums)):
    if nums[i] not in output:
        output.append(nums[i])
if len(nums)==len(output):
    print("True")
else:
    print("False") 
