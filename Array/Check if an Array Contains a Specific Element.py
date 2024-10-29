# Check if an Array Contains a Specific Element
# Question: Check if an array contains a specific element.
# Example:
# Input: arr = [1, 2, 3, 4, 5], target = 3
# Output: True (because 3 is in the array)


arr = [1, 2, 3, 4, 5]
target = 4
n=len(arr)
res=0
for i in range(n):
    if arr[i]==target:
        res+=target
if res:
    print("True")
else:
    print("False")            
        