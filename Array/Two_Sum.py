# Problem: Given an array of integers and a target integer, 
# find two numbers that add up to the target and return their indices.

nums = [2, 7, 11, 15]
target=9
output=[]
for i in range(len(nums)):
    for j in range(i,len(nums)):
        if nums[i]+nums[j]==target:
            output.append(i)
            output.append(j)       
print(output)


# Output: [0, 1] (because 2 + 7 = 9)   