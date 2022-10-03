def Palindrome(ord):
    return palindrome_test == palindrome_test[::-1]
palindrome_test = input("Enter a word ")
ans = Palindrome(palindrome_test)
 
if ans:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")