def main():
    import random
    number = random.randint(1,100)
    number_reveal = ("The number was: " + str(number))
    def play_game(guess):
        def give_feedback(number, guess, number_reveal):
            if guess >= 100 or guess <= 1:
                print("Number must be between 1 and 100")
            elif number == guess:
                print("You Win!")
            elif number <= guess:
                print("Your guess was too high. Try again.")
            elif number >= guess:
                print("Your guess was too low. Try again.")
        give_feedback(number, guess, number_reveal)
    def gameLoop():
        lives = 3
        for game in range(lives):
            play_game(int(input("Guess a number from 1 to 100: ")))
            lives -= 1
            while lives == 0:
                print("You lose! " + number_reveal)
                restart = input("Would you like to play again? 'Yes' or 'No': ")
                if restart == "Yes":
                    print(gameLoop())
                elif restart == "No":
                    return("We didn't like you anyways")
    print(gameLoop())
    
    
if __name__ == "__main__":
    main()