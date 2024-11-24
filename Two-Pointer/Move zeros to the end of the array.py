# Move zeros to the end of the array

# Problem: Rearrange an array so that all zeros are at the end.
# Example:
# Input: arr = [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]


arr = [0, 1, 0, 3, 12]
left=0
n=len(arr)
res=[]
zero=[]
for i in range(n):
    if arr[i] !=0:
        res.append(arr[i])
    else:
        zero.append(arr[i])
print(res+zero)                
