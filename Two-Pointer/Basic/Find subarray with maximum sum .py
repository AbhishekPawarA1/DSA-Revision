# Find subarray with maximum sum

# Problem: Find the subarray with the maximum sum.
# Example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: [4, -1, 2, 1]


arr=[-2, 1, -3, 4, -1, 2, 1, -5, 4]
max=0
char=[]
n=len(arr)
for i in range(n):
    res=[]
    for j in range(i,n):
        res.append(arr[j])
        if sum(res)>max:
            max=sum(res)
            char=res[:]
print(char)
