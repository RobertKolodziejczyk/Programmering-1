number = 0
for i in range(1, 99999997, 4):
    number += 1/i
for j in range(3, 99999999, 4):
    number -= 1/j
print(number*4)