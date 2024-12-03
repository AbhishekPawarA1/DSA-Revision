# Find the minimum length subarray with a given sum

# Problem: Find the smallest subarray with a sum >= target.
# Example:
# Input: arr = [2, 3, 1, 2, 4, 5], target = 7
# Output: [4,5]

arr = [2, 3, 1, 2, 4, 5]
target = 7
n=len(arr)
char=[]
for i in range(n):
    res=[]
    for j in range(i,n):
        res.append(arr[j])
        if len(res)>1:
            if sum(res)>=target:
                char=res[:]
print(char)

