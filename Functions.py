def best(name):
    print(f"{name} är bäst")
name = input("Vad är ditt namn ")
best(name)


def square(number):
    number_2 = number_1 ** 2
    return number_2
number_1 = int(input("Enter a number and this program will square it "))
number_2 = square(number_1)
print(number_2)


def sums(a, b):
    return(a+b)
a = int(input("Enter a number "))
b = int(input("Enter another number "))
c = sums(a, b)
print(f"The sum of your numbers is {c}")


def maximum(a, b, c):
    if a>b and a>c: return a
    elif b>c: return b
    else: return c
a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
max_tal = maximum(a, b, c)
print(f"Det största talet är {max_tal}")

def Palindrome(ord):
    return palindrome_test == palindrome_test[::-1]
palindrome_test = input("Enter a word ")
ans = Palindrome(palindrome_test)
 
if ans:
    print("The word is a palindrome")
else:
    print("The word is not a palindrome")


def is_prime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return "The number is not prime"
  return "The number is prime"
number = int(input("Enter a number and this program will tell if its prime or not "))
a = is_prime(number)
print(a)