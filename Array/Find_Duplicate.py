# Find Duplicates in an Array

# Problem: Identify all duplicate elements in an integer array.
# Example:
# Input: nums = [1, 2, 3, 4, 2, 3]
# Output: [2, 3]


output=[]
nums = [1, 2, 3, 4, 2, 3]
dec={}

for i in nums:
    if i in dec:
        dec[i]+=1
    else:
        dec[i]=1
output=[]        
for key in dec:
    if dec[key]>1:
        output.append(key)
print(output)        
