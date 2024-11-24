# Remove duplicates from a sorted array

# Problem: Remove duplicates in-place from a sorted array and return the new length.
# Example:
# Input: arr = [1, 1, 2, 2, 3]
# Output: 3

arr = [1, 1, 2, 2, 3]
res=[]
left=0
right=len(arr)-1
while left<right:
    if arr[left] not in res:
        res.append(arr[left]) 
    left+=1    
    if arr[right] not in res:
        res.append(arr[right])
    right-=1
print(len(res))    


# time complexity =0(n)