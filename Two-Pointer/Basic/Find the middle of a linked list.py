# Find the middle of a linked list

# Problem: Return the middle node of a linked list using two pointers.
# Example:
# Input: 1 -> 2 -> 3 -> 4 -> 5
# Output: 3

arr=[1,2,3,4,5,6,7,8,10]
left=0
right=len(arr) - 1

while left<=right:
    if left==right :
        print(arr[left])
    if left==right-1:
        print(arr[left])    
    left+=1
    right-=1 

# time complexity is 0(n)   
# space complexity is 0(1)    
