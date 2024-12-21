import random


def gameStart():
    num = random.randint(1,10)
    guess = int(input("Take a guess:"))
    while True:
            if guess > num:
                print("Your guess is to high, try going lower:")
            elif guess < num:
                print("Your guess is to low, try going higher:")
            else:
                print("You got the number! \nCongratulation!!!")
                break
            guess = int(input("Take another guess:"))

#Restart Game if user would like to play
    while True:
        restartGame = input("Do you want to play again? (1: Yes) (2: No): ")
        if restartGame == "1":
            gameStart()
            break  # Break the loop, but gameStart will handle the restart
        elif restartGame == "2":
            print("Thanks for playing! See you next time!")
            return  # Return from the function to stop the game
        else:
            print("Invalid input. Please enter '1' for Yes or '2' for No.")