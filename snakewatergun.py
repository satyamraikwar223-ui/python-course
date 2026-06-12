import random

your_score = 0
computor_score = 0
while True:
    computer_choice = random.choice(['snake', 'water', 'gun'])
    user_choice = input("Enter your choice (snake, water, gun): ").lower()

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'snake' and computer_choice == 'water') or \
         (user_choice == 'water' and computer_choice == 'gun') or \
         (user_choice == 'gun' and computer_choice == 'snake'):
        print("You win! YOUR SCORE is: ", your_score + 1)
        your_score += 1
    
    else:
        print("Computer wins! COMPUTER SCORE is: ", computor_score + 1)
        computor_score += 1
    print(f"Computer chose is: {computer_choice}")
    print(f"Your choice is: {user_choice}")

     
    