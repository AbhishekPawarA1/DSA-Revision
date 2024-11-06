# Problem: Write a program to count the number of vowels and consonants in a string.
# Example:
# plaintext
# Copy code
# Input: "hello"
# Output: Vowels: 2, Consonants: 3

input="hello"
Consonants=0
Vowels=0
for i in range(len(input)):
    if input[i]=="a" or input[i]=="e" or input[i]=="i" or input[i]=="o" or input[i]=="u":
        Vowels+=1
    else:
        Consonants+=1 
print("Vowels:",Vowels) 
print("Consonants:",Consonants)          