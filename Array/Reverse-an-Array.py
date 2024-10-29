# Reverse an Array

# Problem: Reverse the elements of an array in place.
# Example:
# Input: arr = [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]


arr = [1, 2, 3, 4, 5]
output=[]
for i in range(len(arr)-1,-1,-1):
      output.append(arr[i])
print(output)      