def is_prime(n):
  for i in range(2,int(n/2)):
    if (n%i) == 0:
      return False
  return True
number = int(input("Enter a number and this program will tell if its prime or not "))
a = is_prime(number)
print(a)