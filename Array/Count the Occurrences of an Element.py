# Count the Occurrences of an Element in an Array
# Question: Count how many times a specific element appears in an array.
# Example:
# Input: arr = [1, 2, 2, 3, 4, 2], target = 2
# Output: 3 (because 2 appears three times)


arr = [1, 2, 2, 3, 4, 2]
n=len(arr)
target = 2
countOccurance=0
for i in range(n):
    if arr[i]==target:
        countOccurance+=1
print(countOccurance)
