import random
def main():
    print("Welcome to the Simple Number Guessing Game. The rules are, as the name suggests, simple. Guess a number from 1 to 100. You have 3 lives to do so, and your attempts will be tracked. Good Luck!")
    play_game()
    
def play_game():
    print(gameLoop())
    print(restart())
    
def player_guess(guess):
    print("You guessed " + str(guess))
    
def give_feedback(number, guess, lives):
    if number == guess:
        return "You Win!"
    if lives >= 1:
        if guess >= 101 or guess <= 0:
            return "Number must be between 1 and 100"
        elif number <= guess:
            return "Your guess was too high. Try again."
        elif number >= guess:
            return "Your guess was too low. Try again."
    
def restart():
    start_again = input("Would you like to play again? Type 'Yes' or 'No': ")
    if start_again == "Yes" or start_again == "yes":
        play_game()
    elif start_again == "No" or start_again == "no":
        return("Hope you had fun. Thank you for playing. See you next time.")
    
def gameLoop():    
    number = random.randint(1,100)
    number_reveal = ("The number was: " + str(number))
    lives = 3 
    attempts = 0
    for game in range(lives):
        number_guess = int(input("Guess a number from 1 to 100: "))
        player_guess(number_guess)
        print(give_feedback(number,number_guess, lives))
        lives -= 1
        attempts += 1
        if give_feedback(number,number_guess, lives) == "You Win!":
            restart()
        if attempts == 1:
            attempt_counter = "You have guessed 1 time."
        else:
            attempt_counter = "You have guessed " + str(attempts) + " times."
        print(attempt_counter)
        while lives == 0:
            return("You Lose! " + number_reveal)
            restart()

if __name__ == "__main__":
    main()