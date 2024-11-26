# # Sort an array of 0s, 1s, and 2s

# # Problem: Sort an array containing 0s, 1s, and 2s without using extra space.
# # Example:
# # Input: [2, 0, 2, 1, 1, 0]
# # Output: [0, 0, 1, 1, 2, 2]


# Bubble sort


arr=[2,0,2,1,1,0]
n=len(arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

# time complexity is 0(n2)
# space complexity is 0(1)


# QuickSort Algorithm Implementation

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[-1]

    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)


sorted_arr = quick_sort(arr)
print(sorted_arr)


# time complexity is 0(n log n)
# space complexity is 0(log n)