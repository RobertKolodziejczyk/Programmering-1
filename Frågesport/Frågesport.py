from Easy import easyquiz
from Hard import hardquiz
name = input("What is your name? ").capitalize()


difficulty = input("Do you want to play the easy or hard quiz? ").capitalize()
if difficulty == "Easy": easyquiz()
elif difficulty == "Hard": hardquiz()
else: print("Kurwa mac")
