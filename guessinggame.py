def main():
    import random
    number = random.randint(1,100)
    number_reveal = ("The number was: " + str(number))
    def play_game():
        def give_feedback(number, guess, number_reveal):
            if guess > 100 or guess < 1:
                print("Number must be between 1 and 100")
            elif number == guess:
                print("You Win!")
            elif number <= guess:
                print("Your guess was too high. Try again.")
            elif number >= guess:
                print("Your guess was too low. Try again.")
    def gameLoop():
        lives = 3
        for game in lives:
            play_game(input("Guess a number from 1 to 100."))
            while lives <= 0:
                return "You lose!" + number_reveal
            lives -= 1
    print(gameLoop())
    
if __name__ == "__main__":
    main()