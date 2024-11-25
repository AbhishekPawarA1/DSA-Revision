# Find the intersection of two sorted arrays

# Problem: Return the intersection of two sorted arrays.
# Example:
# Input: arr1 = [1, 2, 4], arr2 = [2, 4, 6]
# Output: [2, 4]


# Approach 1

arr1 = [1, 2, 4] 
arr2 = [2, 4, 6]

i=0
j=0
res=[]
while i<len(arr1) and j<len(arr2):
    if arr1[i]==arr2[j]:
        res.append(arr1[i])
        i+=1
        j+=1
    elif arr1[i]<arr2[j]:
        i+=1
    else:
        j+=1        
print(res)

# time complexity=0(n + m)
# space complexity=0(1)


# Approach 2

res=[]
for i in arr1:
    if i in arr2:
        res.append(i)
print(res)        


# time complexity=0(n * m)
# space complexity=0(1)

