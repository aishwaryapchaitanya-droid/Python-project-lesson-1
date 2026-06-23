import random
possible_action = ['rock', 'paper', 'scissors']
while True:
    
    user_action = input("Enter rock, paper, scissors or quit: ")

    if user_action == 'quit':
        print("Game Over!")
        break

    computer_action = random.choice(possible_action)

    print("You chose: ", user_action)
    print("computer chose: ", computer_action)

    if user_action == computer_action:
        print("Its a tie!")

    elif user_action == 'rock':
        if computer_action == 'scissors':
            print("you win!")
        else:
            print("You lose!")

    elif user_action =='paper':
        if computer_action == 'rock':
            print("You win!")
        else:
            print("You lose!")
    
    elif user_action == 'scissors':
        if computer_action == 'paper':
            print("you win!")
        else:
            print("you lose!")
    
