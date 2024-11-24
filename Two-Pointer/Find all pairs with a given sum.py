# Find all pairs with a given sum

# Problem: Find all pairs in a sorted array whose sum equals a target.
# Example:
# Input: arr = [1, 2, 3, 4, 5], target = 6
# Output: [(1, 5), (2, 4)]

arr = [1, 2, 3, 4, 5]
target = 6
left=0
res=[]
right=len(arr) - 1
while left<right:
    if arr[left]+arr[right]>target:
        right-=1
    elif arr[left]+arr[right]<target: 
        left+=1
    elif arr[left]+arr[right]==target:
          res.append((arr[left],arr[right]))
          left+=1
          right-=1     
print(res)          
