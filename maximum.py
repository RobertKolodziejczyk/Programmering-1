def maximum(a, b, c):
    if a>b and a>c: return a
    elif b>c: return b
    else: return c
a = int(input("Enter a number "))
b = int(input("Enter a number "))
c = int(input("Enter a number "))
max_tal = maximum(a, b, c)
print(f"Det största talet är {max_tal}")