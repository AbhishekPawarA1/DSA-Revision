# Reverse a string

# Problem: Reverse a string using two pointers.
# Example:
# Input: "hello"
# Output: "olleh"


Input= "hello"
Input=list(Input)
left=0
right=len(Input)-1

while left < right:
    Input[left],Input[right]=Input[right],Input[left]
    left+=1
    right-=1
res="".join(Input) 
print(res)

# time Complexity = 0(n)
# Space Complexity = 0(n)


