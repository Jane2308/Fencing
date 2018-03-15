#Simple maze game by Dianne Jehee

import turtle

wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("A maze game")
wn.setup(700, 700)

#Maakt een pen
class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)

class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)

#maakt de level lijst
levels = [""]

#Eerste level
level_1 = [
"XXXXXXXXXXXXXXXXXXXXXXXXX",
"XX XXXXX   PXXXXXXXXXXXXX",
"XX XXXXX XXXXXXXX XXXXXXX",
"XX       XXXXXXX  XXXXXXX",
"XXXXXXXX XXXX    XXXXXXXX",
"XXXXXXXX XXXX XXXXXXXXXXX",
"XXXXXXXX XXXX XXXXXXXXXXX",
"XXXXXXXX XXXx XXXXXXXXXXX",
"XXXXXXXX      XXXXXXXXXXX",
"XXXXXXXX XXXX      XXXXXX",
"XXXXXXXX XXXXXXXX XXXXXXX",
"XXXXXXXXXXXXXXXXX  XXXXXX",
"XXXXXXXXXXXXXXXXX  XXXXXX",
"XXXXXXXXXXXXXXXXX XXXXXXX",
"XXXXXXXXXXXXXXXXX  XXXXXX",
"XXXXXXXXXXXXXXXXXX XXXXXX",
"XXXXXXXXX          XXXXXX",
"XXXXXXXXXX XXXXXXX XXXXXX",
"XXXXXXXXXX  XXXXXX XXXXXX",
"XXXXXXXXXX         XXXXXX",
"XXXXXXXXXX XXXXXXXXXXXXXX",
"XXXXXXXXXX XXXX XXXXXXXXX",
"XXXXXXXXXX XXXX XXXXXXXXX",
"XXXXXXXXXX      XXXXXXXXX",
"XXXXXXXXXXXXXXXXXXXXXXXXX",
]

#Voegt de maze toe aan maze lijst#
levels.append(level_1)

#Maakt een level setup fucntie
def setup_maze(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            character = level[y][x]
            screen_x = -288 + (x * 24)
            screen_y = 228 - (y * 24)

            if character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()

            if character == "P":
                player.goto(screen_x, screen_y)

pen = Pen()
player = Player()

setup_maze(levels[1])

while True:
    pass
