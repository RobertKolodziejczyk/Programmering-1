def hardquiz():
    score = 0

    answer1 = input("What is the most common english word? ").capitalize()
    if answer1 == "The": 
        print("That is correct!") 
        score +=1
    elif answer1 == "": 
        print("Did not submit an answer")
    else: print("That is incorrect")

    answer2 = input("Is English the best language ").capitalize()
    if answer2 == "Yes": 
        print("That is correct!") 
        score +=1
    elif answer2 == "": 
        print("Did not submit an answer")
    else: 
        print("That is incorrect")

    answer3 = input("What is 25*25 ").capitalize()
    if answer3 == "625": 
        print("That is correct!") 
        score +=1
    elif answer3 == "": 
        print("Did not submit an answer")
    else: 
        print("That is incorrect")

    answer4 = input("How do you spell roberts last name ").capitalize()
    if answer4 == "Kolodziejczyk": 
        print("You are correct, you must be Robert") 
        score +=1
    elif answer4 == "": 
        print("Did not submit an answer")
    else: 
        print("You are incorrect")

    print(f"{name} you scored {score}/4")
    playagain = input("Do you want to play again ").capitalize()
    if playagain == "Yes": hardquiz()