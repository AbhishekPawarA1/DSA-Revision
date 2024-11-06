# Problem: Write a function to reverse a given string.
# Example:
# plaintext

# Input: "hello"
# Output: "olleh"


str="hello"
n=len(str)
res=[]
for i in range(n-1,-1,-1):
    res.append(str[i])
print(*res,sep="")
