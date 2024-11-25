# Count pairs with a given sum in an unsorted array

# Problem: Count pairs with a given sum using two pointers.
# Example:
# Input: arr = [1, 5, 7, -1], target = 6
# Output: 2


arr = [1, 5, 7,4,2,3]
arr.sort()               #[1,2,3,4,5,7]
target = 6

left=0
right=len(arr)-1
count=0
while left<right:
    if arr[left]+arr[right]==target:
        count+=1
        left+=1
        right-=1
    elif arr[left]+arr[right]>target:
        right-=1
    else:
        left+=1
print(count)       




# time complexity=0(n log n)
# space complexity=0(1)
