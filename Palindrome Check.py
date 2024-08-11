#Palindrome Check
#Write a function to check if a given string is a palindrome using a loop. For example, "madam" is a palindrome.
k = input()
if k == k[::-1]:
    print("its palindrome")
else:
    print("its not palindrome")
