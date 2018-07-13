import time
import random

def displayIntro():
    print('You are on a beach holiday in Greece')
    print('When you walk along the coast, you see a hot boy')
    print('He looks your way and you decide to go and talk to him')
    print('Will you have a normal conversation or flirt with him?')
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose: talk(1) flirt(2)? :")

    return path

def checkPath(chosenPath):
    print("He looks at you with smoldering eyes while you speak")
    time.sleep(2)
    print("When you are done talking he slowly blinks with his beautiful eyes")
    time.sleep(2)
    print("You start feeling nervous and don't know what to expect")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("Then he smiles at you and asks you if you would like to go on a date")
        print("What a great holiday!")
    else:
        print("Oh no! he looks annoyed")
        time.sleep(2)
        print("The hot guy excuses himself and walks away, leaving you alone")
        print("You just made a fool out of yourself")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")

