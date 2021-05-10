import random

print("Welcome to the Number Guessing Game!")
answer_number = random.randrange(1, 11)
player_trys = 0

while True:
    try:
        player_guess = input("Pick a number between 1 and 10: ")
        player_guess = int(player_guess)
        if player_guess < 1 or player_guess > 10:
            print("Please enter a number within the given range.")
            continue
    except ValueError:
        print("Please enter a number.")
        continue
    if player_guess < answer_number:
        print("It is higher!")
        player_trys += 1
        continue
    elif player_guess > answer_number:
        print("It is lower!")
        player_trys += 1
        continue
    else:
        print("You got it! It took you {} tries!".format(player_trys))

    while True:
        play_again = input("Would you like to play again? Yes or no?: ")
        play_again = play_again.lower()
        if play_again == "yes":
            break
        elif play_again == "no":
            break
        else:
            print("Please enter only yes or no!")
            continue

    if play_again == "yes":
        answer_number = random.randrange(1, 11)
        player_trys = 0
        continue
    else:
        print("We hope you had fun!")
        break
