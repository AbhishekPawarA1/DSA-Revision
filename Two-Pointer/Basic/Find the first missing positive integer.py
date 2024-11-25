# Find the first missing positive integer

# Problem: Find the smallest missing positive integer.
# Example:
# Input: [3, 4, -1, 1]
# Output: 2


arr = [2, 4, -1,5,7]
arr.sort()  # Sort the array
expected = 1  # Start looking for 1 as the smallest missing positive integer

for num in arr:
    if num == expected:  # If the current number is the expected number
        expected += 1  # Update to the next expected number

# The first missing positive integer will be in `expected`
print(expected)



# time complexity=0(n log n)
# space complexity=0(1)