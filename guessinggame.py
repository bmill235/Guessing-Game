import random
number = random.randint(1,100)
number_reveal = ("The number was: " + str(number))
def main():
    print(gameLoop())
    print(restart())

def play_game(guess): 
    give_feedback(number, guess)

def give_feedback(number, guess):
    if guess >= 101 or guess <= 0:
        print("Number must be between 1 and 100")
    elif number == guess:
        print("You Win!")
    elif number <= guess:
        print("Your guess was too high. Try again.")
    elif number >= guess:
        print("Your guess was too low. Try again.")

def restart():
    start_again = input("Would you like to play again? 'Yes' or 'No': ")
    if start_again == "Yes":
        print(gameLoop())
    elif start_again == "No":
        return("Hope you had fun. We didn't like you anyway.")
    
def gameLoop():
    attempts = 0
    attempt_counter = "You have guessed " + str(attempts) + " times."
    lives = 3 
    for game in range(lives):
        play_game(int(input("Guess a number from 1 to 100: ")))
        lives -= 1
        attempts += 1
        print(attempt_counter)
        while lives == 0:
            return("You lose! " + number_reveal)
    
if __name__ == "__main__":
    main()