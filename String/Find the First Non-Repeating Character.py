# Problem: Find the first character that does not repeat in a given string.
# Example:
# plaintext
# Copy code
# # Input: "swiss"
# Output: 'w'

input="swiss";
dec={}
for i in input:
    if i in dec:
        dec[i]+=1
    else:
        dec[i]=1
# print(dec)         
for key in dec:
    if dec[key]==1:
       print(key)
       break

    