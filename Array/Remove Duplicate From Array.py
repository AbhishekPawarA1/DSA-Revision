# Remove Duplicates from an Array
# Question: Remove duplicates from a given integer array.
# Example:
# Input: arr = [1, 2, 2, 3, 4, 4]
# Output: [1, 2, 3, 4]

arr = [1, 2, 2, 3, 4, 4]
n=len(arr)
output=[]
for i in range(n):
    if arr[i] not in output:
            output.append(arr[i])
print(output)            
