import random
jackpot=random.randint(1,100)
# print(random.randint(1,100))
guess=int(input("Guess the number"))
counter=1

while guess!= jackpot:
    if guess<jackpot:
        print("guess higher")
    else:
        print("guess lower")

    guess=int(input("Guess the number again \n"))
    counter+=1   


print("you guessed it right \n")
print("you took", counter, "attempts")            