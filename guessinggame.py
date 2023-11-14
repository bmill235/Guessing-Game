def main():
    import random
    number = random.randint(1,100)
    number_reveal = ("The number was: " + str(number))
    attempts = 0 
    def play_game(guess):
        def give_feedback(number, guess, number_reveal):
            if guess >= 100 or guess <= 1:
                print("Number must be between 1 and 100")
            elif number == guess:
                print("You Win!")
            elif number <= guess:
                print("Your guess was too high. Try again.")
                print(". You have guessed: ")
                print(str(attempts))
                print(" times")
            elif number >= guess:
                print("Your guess was too low. Try again.")
                print(". You have guessed: ")
                print(str(attempts))
                print(" times")
        give_feedback(number, guess, number_reveal)
    def gameLoop():
        lives = 3
        for game in range(lives):
            play_game(int(input("Guess a number from 1 to 100: ")))
            lives -= 1
            attempts += 1 
            while lives == 0:
                return("You lose! " + number_reveal)
    print(gameLoop())
    
if __name__ == "__main__":
    main()