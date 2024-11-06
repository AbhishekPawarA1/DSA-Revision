# Check for Palindrome

# Problem: Check if a given string reads the same backward as forward.
# Example:
# plaintext
# Copy code
# Input: "madam"
# Output: True

# Input: "hello"
# Output: False

def palindrone(str,n):
    x=str[::-1]
    if str==x:
        return True
    else:
        return False 
    
str="madam"
n=len(str)
output=palindrone(str,n)
print(output)