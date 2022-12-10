import random

choices = ['r', 'p', 's']
count = 0
computer_score = 0
player_score = 0


def display_final_score():
    print("Computer Score: ", computer_score)
    print("Your score: ", player_score)


def display_choices():
    print("Computer chose: ", computer_choice)
    print("Your choice: ", player_choice)


while count < 5:
    player_choice = input("Choose rock, paper or scissor: Type(r, p or s): ").lower().strip()
    computer_choice = random.choice(choices)

    if player_choice == computer_choice:
        print("It's a tie!! ")
        display_choices()

    elif player_choice == 'r':
        if computer_choice == 'p':
            print("You lost!!")
            display_choices()
            computer_score += 1
        else:
            print("You won!!")
            display_choices() 
            player_score += 1

    elif player_choice == 'p':
        if computer_choice == 's':
            print("You lost!!")
            display_choices()
            computer_score += 1
        else:
            print("You won!!")
            display_choices()
            player_score += 1

    elif player_choice == 's':
        if computer_choice == 'r':
            print("You lost!!")
            display_choices()
            computer_score += 1
        else:
            print("You won!!")
            display_choices()  
            player_score += 1
    else:
        print("Wrong Input!! ")
        continue


    count += 1

    if (count) != 5:
        print(" ")
        print("Let's play again!! ")
        print(" ")


print("\n" + "*"*50 + "\nFinal Score" +"\n"+ "*"*50)

if player_score > computer_score:
    print("You won!! ")
    display_final_score()

elif player_score < computer_score:
    print("You lost!! ")
    display_final_score()

else:
    print("It's a tie!! ")
    display_final_score()

