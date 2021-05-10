import random

print("Welcome to the Number Guessing Game!")
answer_number = random.randrange(10)

while True:
    try:
        player_guess = input("Pick a number between 1 and 10:  ")
        player_guess = int(player_guess)
        if player_guess < 1 or player_guess > 10:
            print("Please enter a number within the given range.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue
    
    if player_guess < answer_number:
        print("It is higher!")
        continue
    elif player_guess > answer_number:
        print("It is lower!")
        continue
    else:
        print("You got it!")
        break
