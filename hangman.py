import random

#Function that prints out the hangingman
def hanging_man(tries):
    if tries == 0:
        return ""

    if tries == 1:
        return """             __________
            |/      |
            |      (_)
            |       |
            |       
            |      
            |
           _|___"""
    if tries == 2:
        return """             __________
            |/      |
            |      (_)
            |      \|
            |       
            |      
            |
           _|___"""
    if tries == 3:
        return """             __________
            |/      |
            |      (_)
            |      \|/
            |       
            |      
            |
           _|___"""
    if tries == 4:
        return """             __________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      
            |
           _|___"""
    if tries == 5:
        return """             __________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / 
            |
           _|___"""
    if tries == 6:
        return """             __________
            |/      |
            |      (_)
            |      \|/
            |       |
            |      / \ 
            |
           _|___"""


"""Function that takes a text file and puts the words in a list. 
Then takes a random word from the list"""
def getfile(file):
    with open(file_choice, encoding='utf-8') as infil:
        words = infil.readlines()
        word = random.choice(words)
        word = word.strip()
    return word

def english_version():
    #Variable that tracks your tries
    tries = 0
    #The variable that prints out an _ for every letter in the word
    word_length = "_" * len(word)
    guessed_letters = []
    #Loop that runs until the user is out of tries or until the player has guessed the word
    while tries < 6 and word_length != word:
        print(word_length, "\n")
        #To prevent printing an empty list
        if len(guessed_letters) > 0:
            print("Your guessed letters are ", *guessed_letters, "\n")
        guess = input("Guess a letter \n").lower()
        if guess in guessed_letters:
            print("You have already guessed that letter")
        #To check if the string consist of only 1 letter
        elif guess.isalpha() and len(guess) == 1:
            if guess in word:
                guessed_letters.append(guess)
                index = 0
                print(hanging_man(tries))
                #Loops through the word to check if the guessed letter is there. 
                while index < len(word):
                    index = word.find(guess, index)
                    if index == -1:
                        break
                    #If the guessed letter is there it adds it to the wordlength at the right index
                    word_length = word_length[:index] + guess + word_length[index+1:]
                    index += 1
            elif guess not in word:
                guessed_letters.append(guess)
                print("Incorrect guess")
                #Increases tries because the player guessed wrong
                tries += 1
                print(hanging_man(tries))
        else:
            print("Your guess must be a letter")

    #Prints out what the word was after the game is over
    print(f"The word was {word}")   
    #Checks if the game was won or lost
    if tries == 6:
        print("The man was hanged and died")
    else:
        print("The man survived")
        

def swedish_version():
    #Variable that tracks your tries
    tries = 0
    #The variable that prints out an _ for every letter in the word
    word_length = "_" * len(word)
    guessed_letters = []
    #Loop that runs until the user is out of tries or until the player has guessed the word
    while tries < 6 and word_length != word:
        print(word_length, "\n")
        #To prevent printing an empty list
        if len(guessed_letters) > 0:
            print("Dina gissade bokstäver är ", *guessed_letters, "\n")
        guess = input("Gissa en bokstav \n").lower()
        if guess in guessed_letters:
            print("Du har redan gissat den bokstaven")
        #To check if the string consist of only 1 letter
        elif guess.isalpha() and len(guess) == 1:
            if guess in word:
                guessed_letters.append(guess)
                index = 0
                #Loops through the word to check if the guessed letter is there. 
                while index < len(word):
                    index = word.find(guess, index)
                    if index == -1:
                        break
                    #if the guessed letter is in the word it adds it to the wordlength at that index
                    word_length = word_length[:index] + guess + word_length[index+1:]
                    index += 1
                    print(hanging_man(tries))
            elif guess not in word:
                guessed_letters.append(guess)
                print("Fel gissning")
                #Increases tries because the player guessed wrong
                tries += 1
                print(hanging_man(tries))
        else:
            print("Din gissning måste innehålla en bokstav")

    #Prints out what the word was after the game is over
    print(f"Ordet var {word}")   
    #Checks if the game was won or lost
    if tries == 6:
        print("Mannen hängdes och dog")
        
    else:
        print("Mannen överlevde")

#Function that decides if the game will be played in english or swedish
Language = input("English or Swedish? ").capitalize()
if Language == "English":
    file_choice = "words.txt"
    word = getfile(file_choice)
    english_version()
elif Language == "Swedish":
    file_choice = "ord.txt"
    word = getfile(file_choice)
    swedish_version()       
else:
    print("English was chosen as the default language")
    file_choice = "words.txt"
    word = getfile(file_choice)
    english_version()

#To check if the player wants to play again
while True:
    playagain = input("Do you want to play again? ").lower()
    if playagain == "yes":
        Language = input("English or Swedish? ").capitalize()
        if Language == "English":
            file_choice = "words.txt"
            word = getfile(file_choice)
            english_version()
        elif Language == "Swedish":
            file_choice = "ord.txt"
            word = getfile(file_choice)
            swedish_version()
        else:
            print("English was chosen as the default language")
            file_choice = "words.txt"
            word = getfile(file_choice)
            english_version()
    else:
        break