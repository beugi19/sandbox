import random 
number = random.randrange(1, 1000)
guess = input("So I'm thinking of a number between 1 and 1000. Try to guess it: ")
guess=int(guess)
for pos in range(10):
        if guess < number and pos < 9:
            print("Nope, that's not it! Hint: it is higher.")
            guess = int(input("Guess again: "))
            pos = pos + 1
        elif guess > number and pos < 9:
            print("Nope, that's not it! Hint: it is lower.")
            guess = int(input("Guess again: "))
            pos = pos + 1
        elif guess != number:
            print("Too bad, you couldn't get it.  The number was", str(number) + ".")
        else:
            print("\nGreat, you got it in", pos + 1,  "guesses!")
            break

