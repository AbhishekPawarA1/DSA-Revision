# Find the Missing Number

# Problem: Given an array containing n distinct numbers from 0 to n, find the missing number.
# Example:
# Input: nums = [3, 0, 1]
# Output: 2

nums = [3, 0, 1]
n = len(nums)
expected_sum = n * (n + 1) // 2
actual_sum = sum(nums)
missing_number = expected_sum - actual_sum
print(missing_number)
