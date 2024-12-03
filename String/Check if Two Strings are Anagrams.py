# Problem: Determine if two strings are anagrams (contain the same characters in a different order).
# Example:
# plaintext
# Copy code
# Input: "listen", "silent"
# Output: True

# Input: "hello", "world"
# Output: False

arr1="listen"
arr2="silent"
isanagram=True

# approach 1

if len(arr1) == len(arr2):  
    for char in arr1:
        if arr1.count(char) != arr2.count(char):  # Compare character frequencies
            isanagram = False
            break
else:
    isanagram = False  

if isanagram:
    print("True")
else:
    print("False")        

# time complexity : 0(n2)    
# space complexity :0(1)

from collections import Counter

if Counter(arr1)==Counter(arr2):
    print("True")
else:
    print("False")    


# time complexity : 0(n)    
# space complexity :0(n)    