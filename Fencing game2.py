dead = ("1")
win = ("2")
nope = ("3")
good_try = ("4")
dumb = ("5")

print ("Option 1: Dance")
print ("Option 2: Parade riposte")
print ("Option 3: Beat attack")
print ("Option 4: Attack")
print ("Option 5: Walk backwards")
number = input("A fencer is coming to you and she attacks. What do you do? ")


if number == good_try:# dit is 4
        print("Good try but you lost a point")
        number = input("One life lost! Try again")
if number == dumb:# dit is 5
        print ("Dumb move, you are dead")
        number = input("One life lost! Try again")
if number == nope: # dit is 3
        print ("Nope Tomás! That will not work not on me")
        number = input ("Try again")
if number == win: # dit is 2
         print ("Yeah, you survived and made an amazing point")
if number == dead:# dit is 1
        print ("Idiot, you are dead")
        number = input("One life lost! Try again")
else:
        print ("What the hell did you type?!")
