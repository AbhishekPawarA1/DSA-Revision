# Three Sum Problem

# Problem: Find all unique triplets in the array that sum up to zero.
# Space Complexity: O(1) (constant space if counting results)
# Example:
# Input: arr = [-1, 0, 1, 2, -1, -4]
# Output: [[-1, -1, 2], [-1, 0, 1]]


arr = [-1, 0, 1, 2, -1, -4]
arr.sort()
result=[]
for i in range(len(arr)-2):
    if i > 0 and arr[i] == arr[i - 1]:  # Skip duplicates for the first element
            continue
    low=i+1
    high=len(arr)-1

    while low<high:
        total=arr[i]+arr[low]+arr[high]
        if total==0:
            result.append([arr[i],arr[low],arr[high]])
            low+=1
            high-=1   

        elif total<0:
            low+=1
        else:
            high-=1
print(result)


# time complexity : 0(n2)
# spance complexity : 0(k)