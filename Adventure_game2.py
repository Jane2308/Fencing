# Name: Dianne Jehee
# Date: 25-2-2018
# description: Text-based Alpaca adventure game

import time
import random

def displayIntro():
    print("It is the end of a long year of fighting anti alpaca criminals")
    print("You come to crossroads on you way home, one path leads to your alpaca farm")
    print("where you will be rewarded with loads of fluffy hugs")
    print("and the other leads through a zombie apocalypse")
    print()

def choosePath():
    path = ""
    while path != "1" and path != "2": # input validation
        path = input("Which path will you choose? (1 or 2): ")

    return path

def checkPath(chosenPath):
    print("You head down the path")
    time.sleep(2)
    print("There's a sheep nearby that looks familiar, that must be a good sign...")
    time.sleep(2)
    print("But you are getting a creepy feeling....")
    print()
    time.sleep(2)

    correctPath = random.randint(1, 2)

    if chosenPath == str(correctPath):
        print("That creepy feeling was just the feeling of admiration from your alpacas")
        print("Welcome home!")
    else:
        print("Oh no! The zombies are coming! Run for your life......")
        time.sleep(2)
        print("You can't run anymore... Zombies start eating on your limbs and slowly you are")
        print("turning in a zombie")

playAgain = "yes"
while playAgain == "yes" or playAgain == "y":
    displayIntro()
    choice = choosePath()
    checkPath(choice) # choice is equal to "1" or "2"
    playAgain = input("Do you want to play again? (yes or y to continue playing): ")
