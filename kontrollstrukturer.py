import webbrowser
import random

#Skottår
def leap_year(year):
    if leapyear % 4 != 0: 
        return "The year is not a leap year"
    elif leapyear % 100 == 0 and leapyear % 400 != 0:
        return "The year is not a leap year"
    else: return "The year is a leap year"
leapyear = int(input("Enter a number "))
answer = leap_year(leapyear)
print(answer)

#Login
accounts = {}
logged_in = False
tries = 0
while True:
    menyval = input(
        "1. Skapa konto\n"
        "2. Logga in\n"
        "3. Läs en rolig historia\n"
        "4. Logga ut\n"
        "5. Avsluta program\n"
    )
    
    if menyval == "1":
        username = input("What is your username? ")
        password = input("What is your password ")
        if username in accounts:
            print("The account already exists")
        else:
            accounts.update({username: password})

    elif menyval == "2":
        if tries == 3: print("You are out of tries")
        while tries < 3:
            usernamecheck = input("Enter your username ")
            passwordcheck = input("Enter your password ")
            if usernamecheck in accounts: 
                if accounts[usernamecheck] == passwordcheck:
                    print("You are now logged in")
                    logged_in = True
                    break
            if logged_in == False:
                print("Wrong username or password")
                tries += 1

    elif menyval == "3":
        if logged_in == True: 
            print("Since you are logged in, I will show you a very good video")
            webbrowser.open("https://www.youtube.com/watch?v=e3LL4mSrLMs&list=PL09DYqkIdFtX94IYnR_Sabj0ovsy8eVOU&index=9&t=2s")
        else: 
            print("Since you are not logged in, I will show you a bad video")
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

    elif menyval == "4":
        areyousure = input("Are you sure you want to logout? ").capitalize()
        if areyousure == "Yes": 
            print("You are now logged out")
            logged_in = False

    elif menyval == "5":
        break

#Gissa Talet
number = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100 "))
    if guess == number: 
        print("You guessed the correct number") 
        break
    elif guess < number: print("The number is bigger")
    else: print("The number is smaller")