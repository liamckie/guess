import random as r
import sys

def guess(x):
    rand = r.randint(1, x)
    guess = 0

    while guess != rand:
        guess = int(input(f"Guess a number between 1 and {x} : "))

        if guess > rand:
            print("Lower!")
        elif guess < rand:
            print("Higher!")
        elif guess == rand:
            print("You guessed correctly!")
            break
        else:
            print(f"Please choose a number within the range of 1 and {x}")


def comp_guess(x):
    low = 1
    high = x
    feedback = ""

    while feedback != "c":
        guess = r.randint(low, high)
        feedback = input(f"Is {guess} too (H)igh , too (L)ow , or (C)orrect? : ").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1

    print("Computer guessed correctly!")


def main():
    answer = 0

    while answer != 1 or answer != 2:
        answer = int(input("Choose a game to play :\n" + 
                   "1. You choose to guess a number\n" +
                   "2. The computer guesses a number chosen by you\n" + 
                   "3. Quit\n\n" +
                   ">>> "))
        
        if answer == 1:
            print("\n\n")
            guess_num = int(input("Enter a number to limit the amount of numbers needed to be guessed e.g. Guess a number between 1 and (your limit number) : "))
            guess(guess_num)
            print("\n\n")
            main()
        
        elif answer == 2:
            print("\n\n")
            comp_guess_num = int(input("Enter a number for the computer to guess : "))
            comp_guess(comp_guess_num)
            print("\n\n")
            main()

        elif answer == 3:
            print("\nThank you for playing!\n")
            sys.exit()

main()