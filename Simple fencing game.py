
fencing = ("parade riposte")
hello = input("A fencer is coming to you and she attacks. What do you do? ")
while hello != fencing:
    print ("Idiot, you are dead")
    hello = input("One life lost! Try again")
if hello == fencing:
    print ("Yeah, you survived and made an amazing point")
