import random

#guessNumber = int(input("Enter your guess between 1 to 10: "))
randomNumber = random.randint(1,10)

while(True):
    guessNumber = int(input("Enter your guess between 1 to 10: "))

    if guessNumber == randomNumber:
        print("Your guess is right.")
        break
    else:
        print("Your guess is not right.")


