import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ").lower()

print("The computer chose", computer,"and the user chose", user +".")
if computer == "rock" and user == "rock":
    print("It's a draw blyat")
elif computer == "rock" and user == "paper":
    print("You win!")
elif computer == "rock" and user == "scissors":
    print("You are trash, bitch")
elif computer == "paper" and user == "rock":
    print("You are trash, bitch")
elif computer == "paper" and user == "paper":
    print("It's a draw blyat")
elif computer == "paper" and user == "scissors":
    print("You win!")
elif computer == "scissors" and user == "rock":
    print("You win")
elif computer == "scissors" and user == "paper":
    print("You are trash, bitch")
elif computer == "scissors" and user == "scissors":
    print("It's a draw blyat")
else: 
    print("??")