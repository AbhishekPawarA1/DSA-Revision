# Remove all instances of a specific value

# Problem: Remove all occurrences of a value from an array.
# Example:
# Input: arr = [3, 2, 2, 3], val = 3
# Output: [2, 2]



arr = [3, 2, 2, 3]
val = 3
res=[]
for i in arr:
    if i==val:
        continue
    else:
        res.append(i) 
print(res)   


# time complexity=0(n)
# space complexity=0(n)