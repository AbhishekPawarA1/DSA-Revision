# Merge two sorted arrays

# Problem: Merge two sorted arrays into one sorted array.
# Example:
# Input: arr1 = [1, 3], arr2 = [2, 4]
# Output: [1, 2, 3, 4]



arr1 = [1, 3]
arr2 = [2, 4]


# approach 1

res=arr1+arr2
res.sort()
print(res) 


# time complexity=0(n + m)
# space complexity=0(n + m)



# approach 2



i = 0
j = 0
res = []

# Merging the arrays
while i < len(arr1) or j < len(arr2):
    if i < len(arr1) and (j >= len(arr2) or arr1[i] < arr2[j]):
        res.append(arr1[i])
        i += 1
    elif j < len(arr2) and (i >= len(arr1) or arr1[i] > arr2[j]):
        res.append(arr2[j])
        j += 1
    else:  # arr1[i] == arr2[j]
        res.append(arr1[i])
        i += 1
        j += 1

print(res)



# time complexity=0(n + m)
# space complexity=0(n + m)
