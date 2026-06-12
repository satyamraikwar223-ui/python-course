i = input("To start the quiz, type 'start' : ")
if i == "start":
    print("Question 1: What is the name of your city ?" , "for 10000 prize money.")
    answer1 = input("Your answer: ")
    if answer1.lower() == "khajuraho":
        print("Correct!" , "you won level one price 10000.")
    elif answer1.lower() == "khajuraho":
        print("Wrong! The correct answer is Khajuraho.")
        print("Better luck next time!")
    else:
         print("Invalid input. Please type 'start' to begin the quiz.")

    print("\nQuestion 2: for which your city is famous?" , "for 50000 prize money.")
    answer2 = input("Your answer: ")
    if answer2.lower() == "monuments":
        print("Correct!" , "you won level one price 50000.")
    else:
        print("Wrong! The correct answer is Monuments.")

    print("\nQuestion 3: What is your colony name ?" , "for 100000 prize money.")
    answer3 = input("Your answer: ")
    if answer3.lower() == "sewagram":
        print("Correct!" , "you won level one price 100000.")
    else:
        print("Wrong! The correct answer is Sewagram.")

print("Thank you for participating in the quiz!" + " Your score is 3/3.")