# Partition array into even and odd elements

# Problem: Partition the array such that even elements come first.
# Example:
# Input: arr = [3, 1, 2, 4]
# Output: [2, 4, 3, 1]

arr = [3, 1, 2, 4]
even=[]
odd=[]
for i in arr:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even+odd)        

