# Problem: Remove all duplicate characters from a string.
# Example:
# plaintext
# Copy code
# Input: "programming"
# Output: "progamin"


input="programming";
res=""
for i in input:
    if i in res:
        continue
    else:
        res+=i
print(res)        