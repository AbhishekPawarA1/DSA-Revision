# Check if a string is a palindrome

# Problem: Determine if a string reads the same backward as forward.
# Example:
# Input: "radar"
# Output: True


input="raar"
left=0
right=len(input)-1
ispaindrone=True
while left <= right:
    if input[left] ==input[right]:
        left += 1
        right -= 1
    else:
        ispaindrone=False
        break
if ispaindrone :
    print("True")
else:
    print("False")            