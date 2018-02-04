import random
n = random.randint(1,6)
dice = int(input("Let's play, roll the dice \n choose a number between 1 and 6"))

while n != "dice":
    if dice < n:
        print( "guess is low")
        dice = int(input("choose a number between 1 and 6 "))
    elif dice > n:
        print("guess is high")
        dice = int(input("choose a number between 1 and 6"))
    if dice == n:
        print("you guessed it!")
