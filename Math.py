chance = 100
total = 25
mines = int(input("How many mines? "))
Good_tiles = total-mines
while Good_tiles >= 1:
    chance *= Good_tiles/total
    Good_tiles -= 1
    total -= 1
print(chance)