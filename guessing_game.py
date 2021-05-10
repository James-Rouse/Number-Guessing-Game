import random

print("Welcome to the Number Guessing Game!")
print("There is no HIGHSCORE. This should be easy for you.")
answer_number = random.randrange(1, 11)
player_trys = 1
high_score = "placeholder"

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
        if high_score == "placeholder":
            print("You achieved the HIGHSCORE! Congrats!")
        elif player_trys == 1 and high_score != 1:
            print("Not only did you achieve the HIGHSCORE, but you achieved the best HIGHSCORE possible! Congrats!")
        elif player_trys == 1 and high_score == 1:
            print("You matched the HIGHSCORE! I'd say to try to beat it, but you can't!")
        elif player_trys == high_score:
            print("You matched the HIGHSCORE! Now try to beat it!")
        elif player_trys < high_score:
            print("You achieved the HIGHSCORE! Congrats!")

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
        if high_score == "placeholder" or high_score > player_trys:
            high_score = player_trys
        print("The HIGHSCORE is {}.".format(high_score))
        player_trys = 1
        continue
    else:
        print("We hope you had fun!")
        break
