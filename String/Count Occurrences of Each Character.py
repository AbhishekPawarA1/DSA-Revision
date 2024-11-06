# Problem: Count the frequency of each character in a string.
# Example:
# plaintext
# Copy code
# Input: "hello"
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}


input="hello"
dic={}
for i in input:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)            