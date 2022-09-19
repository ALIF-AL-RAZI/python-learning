import random

#guessNumber = int(input("Enter your guess between 1 to 10: "))
randomNumber = random.randint(1,10)
x=0
# print(randomNumber)
while(True):
    guessNumber = int(input("Enter your guess between 1 to 10: "))

    if guessNumber != randomNumber:
        print("Your guess is not right.")
        x = x + 1

    else:
        x = x + 1
        print("Your guess is right. You took total ",x,  "attempts")
        break

