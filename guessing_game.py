import random

print("Welcome to the Number Guessing Game!")
answer_number = random.randrange(10)

try:
    player_guess = input("Pick a number between 1 and 10:  ")
    player_guess = int(player_guess)
    if player_guess < 1 or player_guess > 10:
        print("Please enter a number within the given range.")
except ValueError:
    print("Please enter a number.")

print(player_guess)
