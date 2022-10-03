def easyquiz():
    score = 0
    print("Answer these questions with a yes or a no")
    answer1 = input("Is poland best country? ").capitalize()
    if answer1 == "Yes": 
        print("That is correct!") 
        score +=1
    elif answer1 == "No": 
        print("That is incorrect")
    else: 
        print("You have to answer with a yes or a no")

    answer2 = input("Are you poland? ").capitalize()
    if answer2 == "Yes": 
        print("Polska Gurom") 
        score +=1
    elif answer2 == "No": 
        print("Kurwa")
    else: 
        print("You have to answer with a yes or a no")

    answer3 = input("1+2 = 2 yes or no ").capitalize()
    if answer3 == "Yes": 
        print("You are retard") 
    elif answer3 == "No": 
        print("Very good!")
        score +=1
    else: 
        print("You have to answer with a yes or a no")

    answer4 = input("Are you Robert ").capitalize()
    if answer4 == "Yes": 
        print("You are retard") 
        score +=1
    elif answer4 == "No": 
        print("You are not Robert")
    else: 
        print("You have to answer with a yes or a no")

    print(f"{name} you scored {score}/4")
    playagain = input("Do you want to play again ").capitalize()
    if playagain == "Yes": easyquiz()